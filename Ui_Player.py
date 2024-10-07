# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'player.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QDial, QFrame, QHBoxLayout,
    QLCDNumber, QLabel, QLineEdit, QListView,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSlider, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        icon = QIcon()
        icon.addFile(u":/icons/F:/Download Files/Icon 16x16/fugue-icons-3.5.6/icons/music--plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")

        self.horizontalLayout_4.addWidget(self.listView)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.update_butt = QPushButton(self.centralwidget)
        self.update_butt.setObjectName(u"update_butt")
        icon1 = QIcon()
        icon1.addFile(u":/icons/F:/Download Files/Icon 16x16/fugue-icons-3.5.6/bonus/icons-24/gear.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.update_butt.setIcon(icon1)

        self.verticalLayout_4.addWidget(self.update_butt)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon2 = QIcon()
        icon2.addFile(u":/icons/F:/Download Files/Icon 16x16/fugue-icons-3.5.6/icons/address-book--minus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon2)

        self.verticalLayout_4.addWidget(self.pushButton_2)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_4.addWidget(self.listWidget)

        self.labelImage = QLabel(self.centralwidget)
        self.labelImage.setObjectName(u"labelImage")
        self.labelImage.setScaledContents(False)
        self.labelImage.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.labelImage)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 2)
        self.verticalLayout_4.setStretch(3, 6)

        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.horizontalLayout_4.setStretch(0, 3)
        self.horizontalLayout_4.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelTime = QLabel(self.centralwidget)
        self.labelTime.setObjectName(u"labelTime")
        font = QFont()
        font.setPointSize(20)
        self.labelTime.setFont(font)
        self.labelTime.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.labelTime)

        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_3.addWidget(self.horizontalSlider)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 5)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.prev_butt = QPushButton(self.centralwidget)
        self.prev_butt.setObjectName(u"prev_butt")
        icon3 = QIcon()
        icon3.addFile(u":/icons/F:/Download Files/Icon 16x16/fugue-icons-3.5.6/bonus/icons-shadowless-32/arrow-180.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.prev_butt.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.prev_butt)

        self.playPause_butt = QPushButton(self.centralwidget)
        self.playPause_butt.setObjectName(u"playPause_butt")
        icon4 = QIcon()
        icon4.addFile(u":/icons/F:/Download Files/Icon 16x16/fugue-icons-3.5.6/icons-shadowless/playing-card--arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.playPause_butt.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.playPause_butt)

        self.next_butt = QPushButton(self.centralwidget)
        self.next_butt.setObjectName(u"next_butt")
        self.next_butt.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        icon5 = QIcon()
        icon5.addFile(u":/icons/F:/Download Files/Icon 16x16/fugue-icons-3.5.6/bonus/icons-shadowless-32/arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.next_butt.setIcon(icon5)
        self.next_butt.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.next_butt)

        self.labelSearch = QLabel(self.centralwidget)
        self.labelSearch.setObjectName(u"labelSearch")
        self.labelSearch.setFrameShape(QFrame.Shape.NoFrame)
        self.labelSearch.setFrameShadow(QFrame.Shadow.Plain)

        self.horizontalLayout_2.addWidget(self.labelSearch)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lcdVolume = QLCDNumber(self.centralwidget)
        self.lcdVolume.setObjectName(u"lcdVolume")

        self.verticalLayout_2.addWidget(self.lcdVolume)

        self.dialVolume = QDial(self.centralwidget)
        self.dialVolume.setObjectName(u"dialVolume")

        self.verticalLayout_2.addWidget(self.dialVolume)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ESAY Music", None))
        self.update_butt.setText(QCoreApplication.translate("MainWindow", u"Update Files", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Delete All", None))
        self.labelImage.setText("")
        self.labelTime.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.prev_butt.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.playPause_butt.setText(QCoreApplication.translate("MainWindow", u"Pause / Play", None))
        self.next_butt.setText(QCoreApplication.translate("MainWindow", u"Next", None))
#if QT_CONFIG(shortcut)
        self.next_butt.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.labelSearch.setText(QCoreApplication.translate("MainWindow", u"Search :", None))
    # retranslateUi

