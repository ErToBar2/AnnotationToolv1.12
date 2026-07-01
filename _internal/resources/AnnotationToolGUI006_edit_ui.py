# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AnnotationToolGUI006_edit.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QDockWidget, QFrame, QGraphicsView,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1173, 685)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"    background-color: #00407A;\n"
"}\n"
"\n"
"QDockWidget {\n"
"    background-color: #52BDEB;\n"
"    border: grey;\n"
"}\n"
"\n"
"QDockWidget::title {\n"
"    background-color: #1D8EB0;\n"
"    color: white;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border-radius: 10px; /* Rounded corners */\n"
"    padding: 5px;\n"
"    background-color: grey; /* Default color */\n"
"    color: white;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.status_label = QLabel(self.centralwidget)
        self.status_label.setObjectName(u"status_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.status_label.sizePolicy().hasHeightForWidth())
        self.status_label.setSizePolicy(sizePolicy)
        self.status_label.setMinimumSize(QSize(0, 22))
        self.status_label.setMaximumSize(QSize(16777215, 20))
        self.status_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.status_label)

        self.image_label = QLineEdit(self.centralwidget)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setMaximumSize(QSize(16777212, 16777215))

        self.verticalLayout.addWidget(self.image_label)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_4)

        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.graphicsView)

        self.bottomToolbar = QWidget(self.centralwidget)
        self.bottomToolbar.setObjectName(u"bottomToolbar")
        self.bottomToolbar.setStyleSheet(u"QPushButton:checked {\n"
"    background-color: #4FB9E9; /* Color when button is active */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1D8EB0; /* Color when hovering over button */\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(self.bottomToolbar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(11, 4, -1, 1)
        self.Qbutton_previous = QPushButton(self.bottomToolbar)
        self.Qbutton_previous.setObjectName(u"Qbutton_previous")

        self.horizontalLayout.addWidget(self.Qbutton_previous)

        self.Qbutton_draw_box = QPushButton(self.bottomToolbar)
        self.Qbutton_draw_box.setObjectName(u"Qbutton_draw_box")

        self.horizontalLayout.addWidget(self.Qbutton_draw_box)

        self.Qbutton_grey = QPushButton(self.bottomToolbar)
        self.Qbutton_grey.setObjectName(u"Qbutton_grey")

        self.horizontalLayout.addWidget(self.Qbutton_grey)

        self.Qbutton_erase = QPushButton(self.bottomToolbar)
        self.Qbutton_erase.setObjectName(u"Qbutton_erase")

        self.horizontalLayout.addWidget(self.Qbutton_erase)

        self.Qbutton_checked = QPushButton(self.bottomToolbar)
        self.Qbutton_checked.setObjectName(u"Qbutton_checked")

        self.horizontalLayout.addWidget(self.Qbutton_checked)

        self.Qbutton_exclude = QPushButton(self.bottomToolbar)
        self.Qbutton_exclude.setObjectName(u"Qbutton_exclude")

        self.horizontalLayout.addWidget(self.Qbutton_exclude)

        self.Qbutton_next = QPushButton(self.bottomToolbar)
        self.Qbutton_next.setObjectName(u"Qbutton_next")

        self.horizontalLayout.addWidget(self.Qbutton_next)


        self.verticalLayout.addWidget(self.bottomToolbar)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1173, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.rightDockWidget = QDockWidget(MainWindow)
        self.rightDockWidget.setObjectName(u"rightDockWidget")
        self.rightDockWidget.setLayoutDirection(Qt.LeftToRight)
        self.rightDockWidget.setAutoFillBackground(False)
        self.rightDockWidget.setStyleSheet(u"/* Styles for QPushButton when checked (active state) */\n"
"QPushButton:checked {\n"
"    /* Remove background-color to preserve label-specific color */\n"
"    border: 3px solid #4FB9E9; /* Add a distinct border to indicate active state */\n"
"}\n"
"\n"
"\n"
"\n"
"/* General QPushButton styling */\n"
"QPushButton {\n"
"    /* Optional: Set default padding */\n"
"    padding: 5px;\n"
"    /* Optional: Set default border */\n"
"    border: 1px solid transparent;\n"
"    /* Optional: Set border radius for rounded corners */\n"
"    border-radius: 10px;\n"
"	color: black;\n"
"}\n"
"")
        self.rightDockWidget.setFloating(False)
        self.rightDockWidget.setFeatures(QDockWidget.DockWidgetVerticalTitleBar)
        self.rightDockWidget.setAllowedAreas(Qt.RightDockWidgetArea)
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName(u"dockWidgetContents_2")
        self.verticalLayout_3 = QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.QWidget_PreloadingImages = QWidget(self.dockWidgetContents_2)
        self.QWidget_PreloadingImages.setObjectName(u"QWidget_PreloadingImages")

        self.verticalLayout_3.addWidget(self.QWidget_PreloadingImages)

        self.pushButton_user = QPushButton(self.dockWidgetContents_2)
        self.pushButton_user.setObjectName(u"pushButton_user")

        self.verticalLayout_3.addWidget(self.pushButton_user)

        self.line_2 = QFrame(self.dockWidgetContents_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.verticalLayout_Buttons = QVBoxLayout()
        self.verticalLayout_Buttons.setObjectName(u"verticalLayout_Buttons")
        self.verticalLayout_Buttons.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_Buttons.addItem(self.verticalSpacer)


        self.verticalLayout_3.addLayout(self.verticalLayout_Buttons)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Qbutton_addLabel = QPushButton(self.dockWidgetContents_2)
        self.Qbutton_addLabel.setObjectName(u"Qbutton_addLabel")
        self.Qbutton_addLabel.setEnabled(True)
        self.Qbutton_addLabel.setStyleSheet(u"/* Styles for QPushButton when hovered */\n"
"QPushButton:hover {\n"
"    background-color: #1D8EB0; /* Color when hovering over button */\n"
"}")

        self.verticalLayout_4.addWidget(self.Qbutton_addLabel)

        self.Qbutton_Label_99 = QPushButton(self.dockWidgetContents_2)
        self.Qbutton_Label_99.setObjectName(u"Qbutton_Label_99")
        self.Qbutton_Label_99.setStyleSheet(u"/* Styles for QPushButton when hovered */\n"
"QPushButton:hover {\n"
"    background-color: #1D8EB0; /* Color when hovering over button */\n"
"}")

        self.verticalLayout_4.addWidget(self.Qbutton_Label_99)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)

        self.Qbutton_pixel_annotation_polygon = QPushButton(self.dockWidgetContents_2)
        self.Qbutton_pixel_annotation_polygon.setObjectName(u"Qbutton_pixel_annotation_polygon")
        self.Qbutton_pixel_annotation_polygon.setStyleSheet(u"/* Styles for QPushButton when hovered */\n"
"QPushButton:hover {\n"
"    background-color: #1D8EB0; /* Color when hovering over button */\n"
"}")

        self.verticalLayout_4.addWidget(self.Qbutton_pixel_annotation_polygon)

        self.pushButton_Qbutton_undo_polygon = QPushButton(self.dockWidgetContents_2)
        self.pushButton_Qbutton_undo_polygon.setObjectName(u"pushButton_Qbutton_undo_polygon")

        self.verticalLayout_4.addWidget(self.pushButton_Qbutton_undo_polygon)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_4.addItem(self.horizontalSpacer)

        self.Qbutton_edit_annotations = QPushButton(self.dockWidgetContents_2)
        self.Qbutton_edit_annotations.setObjectName(u"Qbutton_edit_annotations")

        self.verticalLayout_4.addWidget(self.Qbutton_edit_annotations)

        self.verticalSpacer_6 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.textEdit_labels = QTextEdit(self.dockWidgetContents_2)
        self.textEdit_labels.setObjectName(u"textEdit_labels")
        self.textEdit_labels.setEnabled(True)
        self.textEdit_labels.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.verticalLayout_4.addWidget(self.textEdit_labels)

        self.line = QFrame(self.dockWidgetContents_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.Qbutton_load_ttls = QPushButton(self.dockWidgetContents_2)
        self.Qbutton_load_ttls.setObjectName(u"Qbutton_load_ttls")

        self.verticalLayout_4.addWidget(self.Qbutton_load_ttls)

        self.line_6 = QFrame(self.dockWidgetContents_2)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_6)

        self.pushButton_export = QPushButton(self.dockWidgetContents_2)
        self.pushButton_export.setObjectName(u"pushButton_export")
        self.pushButton_export.setStyleSheet(u"/* Styles for QPushButton when hovered */\n"
"QPushButton:hover {\n"
"    background-color: #1D8EB0; /* Color when hovering over button */\n"
"}")

        self.verticalLayout_4.addWidget(self.pushButton_export)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)

        self.rightDockWidget.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.rightDockWidget)
        self.leftDockWidget = QDockWidget(MainWindow)
        self.leftDockWidget.setObjectName(u"leftDockWidget")
        self.leftDockWidget.setStyleSheet(u"QPushButton:checked {\n"
"    background-color: #4FB9E9; /* Color when button is active */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1D8EB0; /* Color when hovering over button */\n"
"}\n"
"")
        self.leftDockWidget.setFloating(False)
        self.leftDockWidget.setFeatures(QDockWidget.DockWidgetVerticalTitleBar)
        self.leftDockWidget.setAllowedAreas(Qt.LeftDockWidgetArea)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout_2 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.dockWidgetContents)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.line_3 = QFrame(self.dockWidgetContents)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_3)

        self.Qbutton_directory = QPushButton(self.dockWidgetContents)
        self.Qbutton_directory.setObjectName(u"Qbutton_directory")

        self.verticalLayout_2.addWidget(self.Qbutton_directory)

        self.Qbutton_labels_dir = QPushButton(self.dockWidgetContents)
        self.Qbutton_labels_dir.setObjectName(u"Qbutton_labels_dir")

        self.verticalLayout_2.addWidget(self.Qbutton_labels_dir)

        self.line_5 = QFrame(self.dockWidgetContents)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_5)

        self.Qbutton_load_model = QPushButton(self.dockWidgetContents)
        self.Qbutton_load_model.setObjectName(u"Qbutton_load_model")

        self.verticalLayout_2.addWidget(self.Qbutton_load_model)

        self.Qbutton_runYolo = QPushButton(self.dockWidgetContents)
        self.Qbutton_runYolo.setObjectName(u"Qbutton_runYolo")

        self.verticalLayout_2.addWidget(self.Qbutton_runYolo)

        self.textEdit = QTextEdit(self.dockWidgetContents)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy2)
        self.textEdit.setMinimumSize(QSize(0, 270))
        self.textEdit.setMaximumSize(QSize(16777215, 260))
        self.textEdit.setSizeIncrement(QSize(0, 260))
        self.textEdit.setBaseSize(QSize(0, 260))

        self.verticalLayout_2.addWidget(self.textEdit)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_5)

        self.Qbutton_updateValues = QPushButton(self.dockWidgetContents)
        self.Qbutton_updateValues.setObjectName(u"Qbutton_updateValues")

        self.verticalLayout_2.addWidget(self.Qbutton_updateValues)

        self.QButton_toggleRevision = QPushButton(self.dockWidgetContents)
        self.QButton_toggleRevision.setObjectName(u"QButton_toggleRevision")

        self.verticalLayout_2.addWidget(self.QButton_toggleRevision)

        self.widget = QWidget(self.dockWidgetContents)
        self.widget.setObjectName(u"widget")
        self.line_4 = QFrame(self.widget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(0, 0, 256, 3))
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.widget)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_2)

        self.scrollArea = QScrollArea(self.dockWidgetContents)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 254, 69))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.leftDockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.leftDockWidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AnnotationTool v1.12", None))
        self.status_label.setText(QCoreApplication.translate("MainWindow", u"Status: ", None))
        self.Qbutton_previous.setText(QCoreApplication.translate("MainWindow", u"Previous (A)", None))
        self.Qbutton_draw_box.setText(QCoreApplication.translate("MainWindow", u"Annotate (W)", None))
        self.Qbutton_grey.setText(QCoreApplication.translate("MainWindow", u"Visibility (Space)", None))
        self.Qbutton_erase.setText(QCoreApplication.translate("MainWindow", u"Eraser (S)", None))
        self.Qbutton_checked.setText(QCoreApplication.translate("MainWindow", u"Checked (Q)", None))
        self.Qbutton_exclude.setText(QCoreApplication.translate("MainWindow", u"Exclude (E)", None))
        self.Qbutton_next.setText(QCoreApplication.translate("MainWindow", u"Next (D)", None))
        self.rightDockWidget.setWindowTitle(QCoreApplication.translate("MainWindow", u"Label tools", None))
#if QT_CONFIG(tooltip)
        self.pushButton_user.setToolTip(QCoreApplication.translate("MainWindow", u"Click to edit username.txt.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_user.setText(QCoreApplication.translate("MainWindow", u"User: ", None))
        self.Qbutton_addLabel.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(tooltip)
        self.Qbutton_Label_99.setToolTip(QCoreApplication.translate("MainWindow", u"Black label with class index 99 to edit images", None))
#endif // QT_CONFIG(tooltip)
        self.Qbutton_Label_99.setText(QCoreApplication.translate("MainWindow", u"Delete pixels", None))
#if QT_CONFIG(tooltip)
        self.Qbutton_pixel_annotation_polygon.setToolTip(QCoreApplication.translate("MainWindow", u"Polygon annotationfor masks", None))
#endif // QT_CONFIG(tooltip)
        self.Qbutton_pixel_annotation_polygon.setText(QCoreApplication.translate("MainWindow", u"Polygon", None))
        self.pushButton_Qbutton_undo_polygon.setText(QCoreApplication.translate("MainWindow", u"Undo Polygon", None))
        self.Qbutton_edit_annotations.setText(QCoreApplication.translate("MainWindow", u"Edit Annotations", None))
#if QT_CONFIG(tooltip)
        self.Qbutton_load_ttls.setToolTip(QCoreApplication.translate("MainWindow", u"Switch between the view modes", None))
#endif // QT_CONFIG(tooltip)
        self.Qbutton_load_ttls.setText(QCoreApplication.translate("MainWindow", u"Load .ttls", None))
#if QT_CONFIG(tooltip)
        self.pushButton_export.setToolTip(QCoreApplication.translate("MainWindow", u"Export the annotation labels accordinbg to the selected export_chunks and revision_status", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_export.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.leftDockWidget.setWindowTitle(QCoreApplication.translate("MainWindow", u"Setup tools", None))
        self.label.setText("")
#if QT_CONFIG(tooltip)
        self.Qbutton_directory.setToolTip(QCoreApplication.translate("MainWindow", u"Chose a directory containing an \"images\" and \"labels\" folder", None))
#endif // QT_CONFIG(tooltip)
        self.Qbutton_directory.setText(QCoreApplication.translate("MainWindow", u"Load image directory", None))
#if QT_CONFIG(tooltip)
        self.Qbutton_labels_dir.setToolTip(QCoreApplication.translate("MainWindow", u"Chose a directory containing an \"images\" and \"labels\" folder", None))
#endif // QT_CONFIG(tooltip)
        self.Qbutton_labels_dir.setText(QCoreApplication.translate("MainWindow", u"Select labels directory", None))
#if QT_CONFIG(tooltip)
        self.Qbutton_load_model.setToolTip(QCoreApplication.translate("MainWindow", u"Excluded from standalone research build", None))
#endif // QT_CONFIG(tooltip)
        self.Qbutton_load_model.setText(QCoreApplication.translate("MainWindow", u"YOLO excluded", None))
#if QT_CONFIG(tooltip)
        self.Qbutton_runYolo.setToolTip(QCoreApplication.translate("MainWindow", u"Excluded from standalone research build", None))
#endif // QT_CONFIG(tooltip)
        self.Qbutton_runYolo.setText(QCoreApplication.translate("MainWindow", u"YOLO excluded", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; text-decoration: underline;\">Settings:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">sort_images_sequentially = True</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">auto_next = true # false (use lower case)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                        "text-indent:0px;\">keyboard = QWERTZ</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">boundingBoxEdgeSize = 4</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">greyCurtainTransparency = 150</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">bufferImages = True</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /><span style=\" font-weight:600; text-decoration: underline;\">Export:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">export_chunks = 0 # 0= all chunks , otherwise first and last e.g.  1,2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-"
                        "indent:0px;\">revision_status = 3    # 0 = unchecked, 1=checked,  2=excluded, 3=all</p>\n"
"</body></html>", None))
#if QT_CONFIG(tooltip)
        self.Qbutton_updateValues.setToolTip(QCoreApplication.translate("MainWindow", u"Update the values in the text box", None))
#endif // QT_CONFIG(tooltip)
        self.Qbutton_updateValues.setText(QCoreApplication.translate("MainWindow", u"Update values", None))
#if QT_CONFIG(tooltip)
        self.QButton_toggleRevision.setToolTip(QCoreApplication.translate("MainWindow", u"Switch between the view modes", None))
#endif // QT_CONFIG(tooltip)
        self.QButton_toggleRevision.setText(QCoreApplication.translate("MainWindow", u"All images (Ctrl)", None))
    # retranslateUi

