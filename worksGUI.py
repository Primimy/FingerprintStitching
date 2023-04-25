import sys

import cv2
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QFile, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
                               QFileDialog, QFrame, QGridLayout, QHBoxLayout,
                               QLabel, QMainWindow, QPushButton, QSizePolicy,
                               QSpinBox, QStatusBar, QVBoxLayout, QWidget)
from qt_material import apply_stylesheet

from window_ui import Ui_MainWindow
from works import Stitcher


class Main(QMainWindow, Ui_MainWindow):
    imagePaths = ['', '', '']
    infos = ['sift', 'ransac', '7.0', False, False, '图1+图2', False]
    results = []
    titleString = [
        '特征点 图1',
        '特征点 图2',
        '特征点 图3',
        '特征点匹配 图1+图2',
        '特征点匹配 图1+图3',
        '拼接结果 图1+图2',
        '拼接结果 图2+图3',
        '拼接结果 全部',
    ]

    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_L1.clicked.connect(lambda: self.readImage('L1'))
        self.ui.pushButton_L2.clicked.connect(lambda: self.readImage('L2'))
        self.ui.pushButton_L3.clicked.connect(lambda: self.readImage('L3'))
        self.ui.checkBox_13.stateChanged.connect(self.ifSaveImage)
        self.ui.comboBox_21.currentTextChanged.connect(self.setFeature)
        self.ui.doubleSpinBox_22.valueChanged.connect(self.setRansacThreshold)
        self.ui.horizontalSlider.valueChanged.connect(self.changeContent)
        self.ui.pushButton_25.clicked.connect(self.stitch)

    def readImage(self, buttonLocation):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "选择图片", "", 'Image files (*.png *.jpg)'
        )
        pixmap = QPixmap(file_path)
        if file_path == '':
            return
        if buttonLocation == 'L1':
            self.ui.label_read1.setPixmap(
                pixmap.scaled(
                    self.ui.label_read1.size(),
                    aspectMode=Qt.AspectRatioMode.KeepAspectRatio,
                )
            )
            self.imagePaths[0] = file_path
        elif buttonLocation == 'L2':
            self.ui.label_read2.setPixmap(
                pixmap.scaled(
                    self.ui.label_read2.size(),
                    aspectMode=Qt.AspectRatioMode.KeepAspectRatio,
                )
            )
            self.imagePaths[1] = file_path
        elif buttonLocation == 'L3':
            self.ui.label_read3.setPixmap(
                pixmap.scaled(
                    self.ui.label_read3.size(),
                    aspectMode=Qt.AspectRatioMode.KeepAspectRatio,
                )
            )
            self.imagePaths[2] = file_path

    def ifShowMessage(self, state):
        if state == Qt.CheckState.Checked.value:
            self.infos[3] = True
        else:
            self.infos[3] = False

    def ifFilter(self, state):
        if state == Qt.CheckState.Checked.value:
            self.infos[4] = True
        else:
            self.infos[4] = False

    def ifEqualization(self, state):
        if state == Qt.CheckState.Checked.value:
            self.infos[6] = True
        else:
            self.infos[6] = False

    def ifSaveImage(self, state):
        if state == Qt.CheckState.Checked.value:
            self.infos[6] = True
        else:
            self.infos[6] = False

    def setFeature(self, feature):
        self.infos[0] = feature

    def setMatch(self, match):
        self.infos[5] = match

    def setRansacThreshold(self, threshold):
        self.infos[2] = threshold

    def stitch(self):
        imagePaths = ['', '', '']
        results = []
        from PySide6.QtGui import QImage

        s = Stitcher(self.infos, self.imagePaths)
        s.run()
        output = s.output()
        for image in output:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            qimg = QImage(
                image.data,
                image.shape[1],
                image.shape[0],
                image.shape[1] * 3,
                QImage.Format_RGB888,  # type: ignore
            )
            self.results.append(QPixmap(qimg))
        self.ui.label.setPixmap(
            self.results[0].scaled(
                self.ui.label.size(),
                aspectMode=Qt.AspectRatioMode.KeepAspectRatio,
            )
        )
        self.ui.label_title.setText(self.titleString[0])
        self.ui.horizontalSlider.setMaximum(len(self.results) - 1)

    def changeContent(self, value):
        self.ui.label.setPixmap(
            self.results[value].scaled(
                self.ui.label.size(),
                aspectMode=Qt.AspectRatioMode.KeepAspectRatio,
            )
        )
        self.ui.label_title.setText(self.titleString[value])


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Main()
    window.show()
    sys.exit(app.exec())
