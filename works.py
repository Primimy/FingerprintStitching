import os
import shutil
import time

import cv2
import matplotlib
import numpy as np
from matplotlib import pyplot as plt


class Stitching:
    images, imagePaths = [], []
    infos = []
    results = []
    kps, des = [], []
    Hs, masks = [], []
    fail = False

    def __init__(self, infos, imagePaths):
        self.images, self.imagePaths = [], []
        self.infos = []
        self.results = []
        self.kps, self.des = [], []
        self.Hs, self.masks = [], []
        self.infos = infos
        self.imagePaths = imagePaths
        self.fail = False

        self.readImages()

    # def histogramEqualization(self):
    #     for i in range(len(self.images)):
    #         lab = cv2.cvtColor(self.images[i], cv2.COLOR_BGR2LAB)
    #         l, a, b = cv2.split(lab)
    #         clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    #         cl = clahe.apply(l)
    #         clahe_l = cv2.merge((cl, a, b))
    #         self.images[i] = cv2.cvtColor(clahe_l, cv2.COLOR_LAB2BGR)

    #     matplotlib.rcParams['font.family'] = 'Microsoft YaHei'
    #     figure = plt.figure(figsize=(10, 9))
    #     from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
    #     canvas = FigureCanvasQTAgg(figure)

    #     for i in range(len(self.images)):
    #         plt.subplot(1, len(self.images), i + 1)
    #         plt.imshow(cv2.cvtColor(self.images[i], cv2.COLOR_BGR2RGB))
    #         plt.title('Histogram Equalization/直方图均衡化')
    #     canvas.draw()
    #     self.results.append(canvas)

    def findFeatures(self):
        method = self.infos[0]
        for image in self.images:
            keypoints, descriptors = None, None
            startPerf = time.perf_counter()
            match method:
                case "sift":
                    sift = cv2.SIFT_create()
                    keypoints, descriptors = sift.detectAndCompute(image, None)
                case "orb":
                    orb = cv2.ORB_create()
                    orb.setMaxFeatures(15000)
                    keypoints, descriptors = orb.detectAndCompute(image, None)
                    descriptors = descriptors.astype(np.float32)
                case "brisk":
                    brisk = cv2.BRISK_create()
                    keypoints, descriptors = brisk.detectAndCompute(image, None)
                    descriptors = descriptors.astype(np.float32)
                case "akaze":
                    akaze = cv2.AKAZE_create()
                    keypoints, descriptors = akaze.detectAndCompute(image, None)
                    descriptors = descriptors.astype(np.float32)
                case _:
                    akaze = cv2.AKAZE_create()
                    keypoints, descriptors = akaze.detectAndCompute(image, None)
            endPerf = time.perf_counter()

            image = cv2.drawKeypoints(
                image, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT
            )
            image = cv2.putText(
                image,
                'method: ' + method,
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2,
            )
            image = cv2.putText(
                image,
                'features: ' + str(len(keypoints)),
                (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2,
            )
            image = cv2.putText(
                image,
                'time: ' + str('{:.2f}'.format((endPerf - startPerf) * 1000)) + 'ms',
                (10, 90),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2,
            )
            self.results.append(image)
            self.kps.append(keypoints)
            self.des.append(descriptors)

    def matchFeatures(self):
        for i in range(len(self.images) - 1):
            flann = cv2.FlannBasedMatcher()
            matches = flann.knnMatch(self.des[i], self.des[i + 1], k=2)
            good_matches = []
            for m, n in matches:
                if m.distance < 0.75 * n.distance:
                    good_matches.append(m)

            pts1 = np.float32([self.kps[i][m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)  # type: ignore
            pts2 = np.float32([self.kps[i + 1][m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)  # type: ignore
            H, mask = cv2.findHomography(pts1, pts2, cv2.RANSAC, float(self.infos[2]))
            matchesMask = mask.ravel().tolist()
            dst = cv2.perspectiveTransform(pts1, H)
            backproj_err = np.sqrt(np.sum((dst - pts2) ** 2, axis=2)).ravel()
            mean_err = np.mean(backproj_err)
            std_err = np.std(backproj_err)
            inliers = [
                matches[i] for i in range(len(matchesMask)) if matchesMask[i] == 1
            ]
            outliers = [
                matches[i] for i in range(len(matchesMask)) if matchesMask[i] == 0
            ]
            draw_params = dict(
                matchColor=(0, 255, 0),
                singlePointColor=(255, 0, 0),
                matchesMask=matchesMask,
                flags=cv2.DrawMatchesFlags_DEFAULT,
            )
            image = cv2.drawMatches(
                self.images[i],
                self.kps[i],
                self.images[i + 1],
                self.kps[i + 1],
                good_matches,
                None,
                **draw_params,
            )
            image = cv2.putText(
                image,
                'method: ' + self.infos[0] + ' threshold: ' + str(self.infos[2]),
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2,
            )
            image = cv2.putText(
                image,
                'inliers: ' + str(len(inliers)) + 'outliers: ' + str(len(outliers)),
                (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2,
            )
            image = cv2.putText(
                image,
                'accuracy: '
                + str('{:.2%}'.format(len(inliers) / (len(inliers) + len(outliers)))),
                (10, 120),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2,
            )
            image = cv2.putText(
                image,
                'avgError: ' + str(mean_err) + ' stdError: ' + str(std_err),
                (10, 150),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2,
            )
            self.results.append(image)
            self.Hs.append(H)
            self.masks.append(mask)

    def filter(self, image, show=False):
        ksize = 15
        sigma = 3
        theta_range = np.arange(0, np.pi, 16)
        imageProcessed = image

        gabor_filters = []
        for theta in theta_range:
            kernel = cv2.getGaborKernel(
                (ksize, ksize), sigma, theta, 10, 1, ktype=cv2.CV_32F
            )
            gabor_filters.append(kernel)

        for kernel in gabor_filters:
            imageProcessed = cv2.filter2D(image, cv2.CV_8UC3, kernel)
        if show:
            matplotlib.rcParams['font.family'] = 'Microsoft YaHei'
            plt.figure(figsize=(10, 9))

            plt.subplot(1, 2, 1)
            plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            plt.title('Original Image/原图')
            plt.subplot(1, 2, 2)
            plt.imshow(imageProcessed)
            plt.title('2D Gabor Filter/2D Gabor滤波器')

            plt.show()
        return imageProcessed

    def stitch(self):
        temp = []
        for i in range(len(self.images) - 1):
            H = self.Hs[i]
            mask = self.masks[i]
            height, width, channels = self.images[i + 1].shape
            imageProcessed = cv2.warpPerspective(self.images[i + 1], H, (width, height))
            imageProcessed = cv2.addWeighted(
                imageProcessed, 0.5, self.images[i + 1], 0.5, 0
            )
            temp.append(imageProcessed)
            try:
                temp[i] = (__import__('stitching').Stitcher().stitch([self.imagePaths[i], self.imagePaths[i + 1]]))
                self.results.append(temp[i])
            except:
                self.fail = True

        kp1, des1 = cv2.SIFT_create().detectAndCompute(temp[0], None)
        kp2, des2 = cv2.SIFT_create().detectAndCompute(temp[1], None)
        matches = cv2.FlannBasedMatcher().knnMatch(des1, des2, k=2)
        good_matches = [m for m, n in matches if m.distance < 0.75 * n.distance]

        H, mask = cv2.findHomography(
            np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2),  # type: ignore
            np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2),  # type: ignore
            cv2.RANSAC,
            float(self.infos[2]),
        )
        warped = cv2.warpPerspective(
            temp[1], H, (temp[0].shape[1] + temp[1].shape[1], temp[0].shape[0])
        )
        self.results.append(
            __import__('stitching').Stitcher().stitch([self.imagePaths[0], self.imagePaths[1], self.imagePaths[2]])
        )

    def _stitcher(self):
        temp = []
        for i in range(len(self.images) - 1):
            H = self.Hs[i]
            mask = self.masks[i]
            # height, width, channels = self.images[i + 1].shape
            imageProcessed = cv2.warpPerspective(
                self.images[i],
                H,
                (
                    self.images[i].shape[1] + self.images[i + 1].shape[1],
                    self.images[i].shape[0],
                ),
            )
            # overlap = abs(self.images[i].shape[1] - imageProcessed.shape[1])
            # alpha = np.linspace(0, 1, overlap)
            # mask = np.concatenate(
            #     [
            #         np.zeros(self.images[i].shape[1] - overlap),
            #         alpha,
            #         np.ones(imageProcessed.shape[1]),
            #     ]
            # )
            # result = self.images[i].shape[1] * mask + imageProcessed * (1 - mask)
            imageProcessed[
                0 : self.images[i + 1].shape[0], 0 : self.images[i + 1].shape[1]
            ] = self.images[i + 1]
            temp.append(imageProcessed)
            self.results.append(imageProcessed)

        # temp[1] = self.images[2]
        kp1, des1 = cv2.SIFT_create().detectAndCompute(temp[0], None)
        kp2, des2 = cv2.SIFT_create().detectAndCompute(temp[1], None)
        matches = cv2.FlannBasedMatcher().knnMatch(des1, des2, k=2)
        good_matches = [m for m, n in matches if m.distance < 0.75 * n.distance]

        H, mask = cv2.findHomography(
            np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2),  # type: ignore
            np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2),  # type: ignore
            cv2.RANSAC,
            float(self.infos[2]),
        )
        warped = cv2.warpPerspective(
            temp[0], H, (temp[0].shape[1] + temp[1].shape[1], temp[1].shape[0])
        )
        # output = cv2.addWeighted(temp[0], 0.5, temp[1], 0.5, 0)
        # warped[0 : temp[1].shape[0], 0 : temp[1].shape[1]] = temp[1]

        self.results.append(warped)
        # self.results.append(output)

    def readImages(self):
        for path in self.imagePaths:
            if os.path.exists(path):
                self.images.append(cv2.imread(path))

    def writeImages(self, path):
        if os.path.exists(path):
            shutil.rmtree(path)
        os.mkdir(path)
        for i in range(len(self.results)):
            cv2.imwrite(path + '/' + str(i) + '.jpg', self.results[i])

    def output(self):
        return self.results,self.fail

    def run(self):
        self.findFeatures()
        self.matchFeatures()
        self.stitch()
        # self._stitcher()
        if self.infos[6]:
            self.writeImages('results')


if __name__ == '__main__':
    s = Stitching(
        ['sift', 'ransac', '7.0', False, False, '', True],
        ['images/a1.jpg', 'images/a2.jpg', 'images/a3.jpg']
        # ['images/weir_1.jpg', 'images/weir_2.jpg', 'images/weir_3.jpg']
        # ['images/t2/1.jpg', 'images/t2/2.jpg', 'images/t2/3.jpg'],
    )
    s.run()
    exit()
