# Form implementation generated from reading ui file 'vernam.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_vernam(object):
    def setupUi(self, vernam):
        vernam.setObjectName("vernam")
        vernam.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(vernam)
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName("verticalLayout")
        self.group_box_input = QtWidgets.QGroupBox(vernam)
        self.group_box_input.setObjectName("group_box_input")
        self.verticalLayout_40 = QtWidgets.QVBoxLayout(self.group_box_input)
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName("verticalLayout_40")
        self.text_edit_input = QtWidgets.QTextEdit(self.group_box_input)
        self.text_edit_input.setObjectName("text_edit_input")
        self.verticalLayout_40.addWidget(self.text_edit_input)
        self.verticalLayout.addWidget(self.group_box_input)
        self.horizontal_layout_1 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_1.setContentsMargins(8, -1, -1, -1)
        self.horizontal_layout_1.setSpacing(12)
        self.horizontal_layout_1.setObjectName("horizontal_layout_1")
        self.label_key = QtWidgets.QLabel(vernam)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_key.sizePolicy().hasHeightForWidth())
        self.label_key.setSizePolicy(sizePolicy)
        self.label_key.setObjectName("label_key")
        self.horizontal_layout_1.addWidget(self.label_key)
        self.line_edit_key = QtWidgets.QLineEdit(vernam)
        self.line_edit_key.setObjectName("line_edit_key")
        self.horizontal_layout_1.addWidget(self.line_edit_key)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontal_layout_1.addItem(spacerItem)
        self.button_make = QtWidgets.QPushButton(vernam)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_make.sizePolicy().hasHeightForWidth())
        self.button_make.setSizePolicy(sizePolicy)
        self.button_make.setMinimumSize(QtCore.QSize(100, 30))
        self.button_make.setObjectName("button_make")
        self.horizontal_layout_1.addWidget(self.button_make)
        self.verticalLayout.addLayout(self.horizontal_layout_1)
        self.group_box_output = QtWidgets.QGroupBox(vernam)
        self.group_box_output.setObjectName("group_box_output")
        self.verticalLayout_41 = QtWidgets.QVBoxLayout(self.group_box_output)
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName("verticalLayout_41")
        self.text_edit_output = QtWidgets.QTextEdit(self.group_box_output)
        self.text_edit_output.setObjectName("text_edit_output")
        self.verticalLayout_41.addWidget(self.text_edit_output)
        self.verticalLayout.addWidget(self.group_box_output)

        self.retranslateUi(vernam)
        QtCore.QMetaObject.connectSlotsByName(vernam)

    def retranslateUi(self, vernam):
        _translate = QtCore.QCoreApplication.translate
        vernam.setWindowTitle(_translate("vernam", "Form"))
        self.group_box_input.setTitle(_translate("vernam", "Input text"))
        self.label_key.setText(_translate("vernam", "Key:"))
        self.button_make.setText(_translate("vernam", "Make"))
        self.group_box_output.setTitle(_translate("vernam", "Output text"))
