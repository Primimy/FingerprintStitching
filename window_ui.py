# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1125, 755)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_L = QVBoxLayout()
        self.verticalLayout_L.setObjectName(u"verticalLayout_L")
        self.horizontalLayout_L1 = QHBoxLayout()
        self.horizontalLayout_L1.setObjectName(u"horizontalLayout_L1")
        self.pushButton_L1 = QPushButton(self.centralwidget)
        self.pushButton_L1.setObjectName(u"pushButton_L1")

        self.horizontalLayout_L1.addWidget(self.pushButton_L1)

        self.label_read1 = QLabel(self.centralwidget)
        self.label_read1.setObjectName(u"label_read1")

        self.horizontalLayout_L1.addWidget(self.label_read1)

        self.horizontalLayout_L1.setStretch(0, 1)
        self.horizontalLayout_L1.setStretch(1, 4)

        self.verticalLayout_L.addLayout(self.horizontalLayout_L1)

        self.line_L1 = QFrame(self.centralwidget)
        self.line_L1.setObjectName(u"line_L1")
        self.line_L1.setFrameShape(QFrame.HLine)
        self.line_L1.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_L.addWidget(self.line_L1)

        self.horizontalLayout_L2 = QHBoxLayout()
        self.horizontalLayout_L2.setObjectName(u"horizontalLayout_L2")
        self.pushButton_L2 = QPushButton(self.centralwidget)
        self.pushButton_L2.setObjectName(u"pushButton_L2")

        self.horizontalLayout_L2.addWidget(self.pushButton_L2)

        self.label_read2 = QLabel(self.centralwidget)
        self.label_read2.setObjectName(u"label_read2")

        self.horizontalLayout_L2.addWidget(self.label_read2)

        self.horizontalLayout_L2.setStretch(0, 1)
        self.horizontalLayout_L2.setStretch(1, 4)

        self.verticalLayout_L.addLayout(self.horizontalLayout_L2)

        self.line_L2 = QFrame(self.centralwidget)
        self.line_L2.setObjectName(u"line_L2")
        self.line_L2.setFrameShape(QFrame.HLine)
        self.line_L2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_L.addWidget(self.line_L2)

        self.horizontalLayout_L3 = QHBoxLayout()
        self.horizontalLayout_L3.setObjectName(u"horizontalLayout_L3")
        self.pushButton_L3 = QPushButton(self.centralwidget)
        self.pushButton_L3.setObjectName(u"pushButton_L3")

        self.horizontalLayout_L3.addWidget(self.pushButton_L3)

        self.label_read3 = QLabel(self.centralwidget)
        self.label_read3.setObjectName(u"label_read3")

        self.horizontalLayout_L3.addWidget(self.label_read3)

        self.horizontalLayout_L3.setStretch(0, 1)
        self.horizontalLayout_L3.setStretch(1, 4)

        self.verticalLayout_L.addLayout(self.horizontalLayout_L3)


        self.horizontalLayout.addLayout(self.verticalLayout_L)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.verticalLayout_R = QVBoxLayout()
        self.verticalLayout_R.setObjectName(u"verticalLayout_R")
        self.gridLayout_R = QGridLayout()
        self.gridLayout_R.setObjectName(u"gridLayout_R")
        self.doubleSpinBox_22 = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_22.setObjectName(u"doubleSpinBox_22")
        self.doubleSpinBox_22.setMinimum(1.000000000000000)
        self.doubleSpinBox_22.setMaximum(50.000000000000000)
        self.doubleSpinBox_22.setSingleStep(0.500000000000000)
        self.doubleSpinBox_22.setValue(7.000000000000000)

        self.gridLayout_R.addWidget(self.doubleSpinBox_22, 1, 1, 1, 1, Qt.AlignHCenter)

        self.comboBox_21 = QComboBox(self.centralwidget)
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.setObjectName(u"comboBox_21")

        self.gridLayout_R.addWidget(self.comboBox_21, 1, 0, 1, 1, Qt.AlignHCenter)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_R.addWidget(self.label_11, 0, 0, 1, 1, Qt.AlignHCenter)

        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setWordWrap(False)

        self.gridLayout_R.addWidget(self.label_12, 0, 1, 1, 1, Qt.AlignHCenter)

        self.checkBox_13 = QCheckBox(self.centralwidget)
        self.checkBox_13.setObjectName(u"checkBox_13")
        self.checkBox_13.setText(u"\u4fdd\u5b58\u7ed3\u679c")

        self.gridLayout_R.addWidget(self.checkBox_13, 0, 2, 1, 1, Qt.AlignHCenter)

        self.pushButton_25 = QPushButton(self.centralwidget)
        self.pushButton_25.setObjectName(u"pushButton_25")

        self.gridLayout_R.addWidget(self.pushButton_25, 1, 2, 1, 1, Qt.AlignHCenter)


        self.verticalLayout_R.addLayout(self.gridLayout_R)

        self.line_R1 = QFrame(self.centralwidget)
        self.line_R1.setObjectName(u"line_R1")
        self.line_R1.setFrameShape(QFrame.HLine)
        self.line_R1.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_R.addWidget(self.line_R1)

        self.label_title = QLabel(self.centralwidget)
        self.label_title.setObjectName(u"label_title")

        self.verticalLayout_R.addWidget(self.label_title, 0, Qt.AlignHCenter)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_R.addWidget(self.label)

        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_R.addWidget(self.horizontalSlider)

        self.verticalLayout_R.setStretch(0, 1)
        self.verticalLayout_R.setStretch(3, 6)

        self.horizontalLayout.addLayout(self.verticalLayout_R)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(2, 2)

        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_L1.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u56fe\u50cf", None))
        self.label_read1.setText("")
        self.pushButton_L2.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u56fe\u50cf", None))
        self.label_read2.setText("")
        self.pushButton_L3.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u56fe\u50cf", None))
        self.label_read3.setText("")
        self.comboBox_21.setItemText(0, QCoreApplication.translate("MainWindow", u"SIFT", None))
        self.comboBox_21.setItemText(1, QCoreApplication.translate("MainWindow", u"ORB", None))
        self.comboBox_21.setItemText(2, QCoreApplication.translate("MainWindow", u"BRISK", None))
        self.comboBox_21.setItemText(3, QCoreApplication.translate("MainWindow", u"AKAZE", None))

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u7279\u5f81\u70b9\u63d0\u53d6", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"RANSAC\u9608\u503c", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u6f14\u793a", None))
        self.label_title.setText("")
        self.label.setText("")
    # retranslateUi

