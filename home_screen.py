# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerfBlstK.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class homeScreenWindow(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(865, 702)
        Form.setAutoFillBackground(True)
        Form.setStyleSheet(u"background-color: darkblue;")
        self.verticalLayoutWidget_2 = QWidget(Form)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(560, 100, 281, 571))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.startall_btn = QPushButton(self.verticalLayoutWidget_2)
        self.startall_btn.setObjectName(u"startall_btn")
        self.startall_btn.setMinimumSize(QSize(0, 100))
        font = QFont()
        font.setFamily(u"Noto Sans")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.startall_btn.setFont(font)
        self.startall_btn.setStyleSheet(u"background-color : blue")

        self.verticalLayout_2.addWidget(self.startall_btn)

        self.startsel_btn = QPushButton(self.verticalLayoutWidget_2)
        self.startsel_btn.setObjectName(u"startsel_btn")
        self.startsel_btn.setMinimumSize(QSize(0, 100))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setWeight(75)
        self.startsel_btn.setFont(font1)
        self.startsel_btn.setStyleSheet(u"background-color : blue")

        self.verticalLayout_2.addWidget(self.startsel_btn)

        self.reports_btn = QPushButton(self.verticalLayoutWidget_2)
        self.reports_btn.setObjectName(u"reports_btn")
        self.reports_btn.setMinimumSize(QSize(0, 100))
        self.reports_btn.setFont(font1)
        self.reports_btn.setStyleSheet(u"background-color : blue")

        self.verticalLayout_2.addWidget(self.reports_btn)

        self.exit_btn = QPushButton(self.verticalLayoutWidget_2)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setMinimumSize(QSize(0, 100))
        self.exit_btn.setFont(font1)
        self.exit_btn.setStyleSheet(u"background-color : blue")

        self.verticalLayout_2.addWidget(self.exit_btn)

        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 891, 71))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamily(u"Hack")
        font2.setPointSize(11)
        font2.setItalic(True)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setIndent(0)

        self.verticalLayout.addWidget(self.label_2)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))
        font3 = QFont()
        font3.setFamily(u"Hack")
        font3.setPointSize(25)
        font3.setBold(False)
        font3.setItalic(True)
        font3.setWeight(50)
        font3.setKerning(True)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setIndent(0)

        self.verticalLayout.addWidget(self.label)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 90, 461, 581))
        font4 = QFont()
        font4.setKerning(True)
        self.groupBox.setFont(font4)
        self.groupBox.setAutoFillBackground(False)
        self.listWidget = QListWidget(self.groupBox)
        __qlistwidgetitem = QListWidgetItem(self.listWidget)
        __qlistwidgetitem.setCheckState(Qt.Unchecked);
        __qlistwidgetitem.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem1.setCheckState(Qt.Unchecked);
        __qlistwidgetitem1.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem2.setCheckState(Qt.Unchecked);
        __qlistwidgetitem3 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem3.setCheckState(Qt.Unchecked);
        __qlistwidgetitem3.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem4 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem4.setCheckState(Qt.Unchecked);
        __qlistwidgetitem4.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem5 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem5.setCheckState(Qt.Unchecked);
        __qlistwidgetitem5.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem6 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem6.setCheckState(Qt.Unchecked);
        __qlistwidgetitem6.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem7 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem7.setCheckState(Qt.Unchecked);
        __qlistwidgetitem7.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem8 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem8.setCheckState(Qt.Unchecked);
        __qlistwidgetitem8.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem9 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem9.setCheckState(Qt.Unchecked);
        __qlistwidgetitem9.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem10 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem10.setCheckState(Qt.Unchecked);
        __qlistwidgetitem10.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem11 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem11.setCheckState(Qt.Unchecked);
        __qlistwidgetitem11.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem12 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem12.setCheckState(Qt.Unchecked);
        __qlistwidgetitem12.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem13 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem13.setCheckState(Qt.Unchecked);
        __qlistwidgetitem13.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem14 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem14.setCheckState(Qt.Unchecked);
        __qlistwidgetitem14.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem15 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem15.setCheckState(Qt.Unchecked);
        __qlistwidgetitem15.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem16 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem16.setCheckState(Qt.Unchecked);
        __qlistwidgetitem16.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem17 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem17.setCheckState(Qt.Unchecked);
        __qlistwidgetitem17.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem18 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem18.setCheckState(Qt.Unchecked);
        __qlistwidgetitem18.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem19 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem19.setCheckState(Qt.Unchecked);
        __qlistwidgetitem19.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem20 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem20.setCheckState(Qt.Unchecked);
        __qlistwidgetitem20.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem21 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem21.setCheckState(Qt.Unchecked);
        __qlistwidgetitem21.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem22 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem22.setCheckState(Qt.Unchecked);
        __qlistwidgetitem22.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(0, 40, 461, 491))
        font5 = QFont()
        font5.setFamily(u"Noto Sans")
        font5.setPointSize(13)
        font5.setItalic(False)
        font5.setKerning(True)
        self.listWidget.setFont(font5)
        self.listWidget.setStyleSheet(u"background-color : black")
        self.listWidget.setTabKeyNavigation(False)
        self.listWidget.setProperty("showDropIndicator", True)
        self.listWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.listWidget.setTextElideMode(Qt.ElideNone)
        self.listWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.listWidget.setViewMode(QListView.ListMode)
        self.verticalLayoutWidget_3 = QWidget(self.groupBox)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 0, 431, 41))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName(u"label_3")
        font6 = QFont()
        font6.setFamily(u"Hack")
        font6.setPointSize(20)
        font6.setBold(True)
        font6.setWeight(75)
        font6.setKerning(True)
        self.label_3.setFont(font6)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.toggleall_btn = QPushButton(self.groupBox)
        self.toggleall_btn.setObjectName(u"toggleall_btn")
        self.toggleall_btn.setGeometry(QRect(0, 540, 459, 31))
        font7 = QFont()
        font7.setPointSize(11)
        font7.setKerning(True)
        self.toggleall_btn.setFont(font7)
        self.toggleall_btn.setStyleSheet(u"background-color : blue")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.startall_btn.setText(QCoreApplication.translate("Form", u"PLAY ALL", None))
        self.startsel_btn.setText(QCoreApplication.translate("Form", u"PLAY SELECTED", None))
        self.reports_btn.setText(QCoreApplication.translate("Form", u"REPORTS", None))
        self.exit_btn.setText(QCoreApplication.translate("Form", u"EXIT", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Military Aviation Cognitive Testing", None))
        self.label.setText(QCoreApplication.translate("Form", u"notMACT v1.0 by Ando", None))
        self.groupBox.setTitle("")

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Form", u"Airborne Numerical", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Form", u"Angles, Bearings & Degrees", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Form", u"Auditory Capacity", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Form", u"Cognitive Updating", None));
        ___qlistwidgetitem4 = self.listWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("Form", u"Colours, Letters & Numbers", None));
        ___qlistwidgetitem5 = self.listWidget.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("Form", u"Digit Recognition", None));
        ___qlistwidgetitem6 = self.listWidget.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("Form", u"Directions & Distances", None));
        ___qlistwidgetitem7 = self.listWidget.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("Form", u"Dynamic Projection", None));
        ___qlistwidgetitem8 = self.listWidget.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("Form", u"Instrument Comprehension", None));
        ___qlistwidgetitem9 = self.listWidget.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("Form", u"Numerical Operations", None));
        ___qlistwidgetitem10 = self.listWidget.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("Form", u"Rapid Tracking", None));
        ___qlistwidgetitem11 = self.listWidget.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("Form", u"Sensory Motor Apparatus", None));
        ___qlistwidgetitem12 = self.listWidget.item(12)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("Form", u"Situational Awareness", None));
        ___qlistwidgetitem13 = self.listWidget.item(13)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("Form", u"Spacial Integration", None));
        ___qlistwidgetitem14 = self.listWidget.item(14)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("Form", u"System Logic", None));
        ___qlistwidgetitem15 = self.listWidget.item(15)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("Form", u"Table Reading", None));
        ___qlistwidgetitem16 = self.listWidget.item(16)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("Form", u"Target Recogniton", None));
        ___qlistwidgetitem17 = self.listWidget.item(17)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("Form", u"Trace 1", None));
        ___qlistwidgetitem18 = self.listWidget.item(18)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("Form", u"Trace 2", None));
        ___qlistwidgetitem19 = self.listWidget.item(19)
        ___qlistwidgetitem19.setText(QCoreApplication.translate("Form", u"Verbal Logic", None));
        ___qlistwidgetitem20 = self.listWidget.item(20)
        ___qlistwidgetitem20.setText(QCoreApplication.translate("Form", u"Visual Search ", None));
        ___qlistwidgetitem21 = self.listWidget.item(21)
        ___qlistwidgetitem21.setText(QCoreApplication.translate("Form", u"Visualisation", None));
        ___qlistwidgetitem22 = self.listWidget.item(22)
        ___qlistwidgetitem22.setText(QCoreApplication.translate("Form", u"Vigilance", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.label_3.setText(QCoreApplication.translate("Form", u"Tests:", None))
        self.toggleall_btn.setText(QCoreApplication.translate("Form", u"Toggle All", None))
    # retranslateUi

