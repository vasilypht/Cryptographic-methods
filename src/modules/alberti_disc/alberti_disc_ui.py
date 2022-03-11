# Form implementation generated from reading ui file 'alberti_disc.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_alberti_disc(object):
    def setupUi(self, alberti_disc):
        alberti_disc.setObjectName("alberti_disc")
        alberti_disc.resize(500, 400)
        self.verticalLayout = QtWidgets.QVBoxLayout(alberti_disc)
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName("verticalLayout")
        self.group_box_input = QtWidgets.QGroupBox(alberti_disc)
        self.group_box_input.setObjectName("group_box_input")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.group_box_input)
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.text_edit_input = QtWidgets.QTextEdit(self.group_box_input)
        self.text_edit_input.setObjectName("text_edit_input")
        self.verticalLayout_34.addWidget(self.text_edit_input)
        self.verticalLayout.addWidget(self.group_box_input)
        self.horizontal_layout_1 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_1.setContentsMargins(8, -1, -1, -1)
        self.horizontal_layout_1.setSpacing(12)
        self.horizontal_layout_1.setObjectName("horizontal_layout_1")
        self.label_key = QtWidgets.QLabel(alberti_disc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_key.sizePolicy().hasHeightForWidth())
        self.label_key.setSizePolicy(sizePolicy)
        self.label_key.setObjectName("label_key")
        self.horizontal_layout_1.addWidget(self.label_key)
        self.line_edit_key = QtWidgets.QLineEdit(alberti_disc)
        self.line_edit_key.setObjectName("line_edit_key")
        self.horizontal_layout_1.addWidget(self.line_edit_key)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontal_layout_1.addItem(spacerItem)
        self.combo_box_mode = QtWidgets.QComboBox(alberti_disc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_box_mode.sizePolicy().hasHeightForWidth())
        self.combo_box_mode.setSizePolicy(sizePolicy)
        self.combo_box_mode.setObjectName("combo_box_mode")
        self.combo_box_mode.addItem("")
        self.combo_box_mode.addItem("")
        self.horizontal_layout_1.addWidget(self.combo_box_mode)
        self.verticalLayout.addLayout(self.horizontal_layout_1)
        self.horizontal_layout_2 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_2.setContentsMargins(8, -1, -1, -1)
        self.horizontal_layout_2.setSpacing(12)
        self.horizontal_layout_2.setObjectName("horizontal_layout_2")
        self.label_key_alphabet_shift = QtWidgets.QLabel(alberti_disc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_key_alphabet_shift.sizePolicy().hasHeightForWidth())
        self.label_key_alphabet_shift.setSizePolicy(sizePolicy)
        self.label_key_alphabet_shift.setObjectName("label_key_alphabet_shift")
        self.horizontal_layout_2.addWidget(self.label_key_alphabet_shift)
        self.spin_box_key_alphabet_shift = QtWidgets.QSpinBox(alberti_disc)
        self.spin_box_key_alphabet_shift.setObjectName("spin_box_key_alphabet_shift")
        self.horizontal_layout_2.addWidget(self.spin_box_key_alphabet_shift)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontal_layout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontal_layout_2)
        self.horizontal_layout_3 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_3.setContentsMargins(8, -1, -1, -1)
        self.horizontal_layout_3.setSpacing(12)
        self.horizontal_layout_3.setObjectName("horizontal_layout_3")
        self.label_iteration_step = QtWidgets.QLabel(alberti_disc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_iteration_step.sizePolicy().hasHeightForWidth())
        self.label_iteration_step.setSizePolicy(sizePolicy)
        self.label_iteration_step.setObjectName("label_iteration_step")
        self.horizontal_layout_3.addWidget(self.label_iteration_step)
        self.spin_box_iteration_step = QtWidgets.QSpinBox(alberti_disc)
        self.spin_box_iteration_step.setMinimum(-99)
        self.spin_box_iteration_step.setObjectName("spin_box_iteration_step")
        self.horizontal_layout_3.addWidget(self.spin_box_iteration_step)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontal_layout_3.addItem(spacerItem2)
        self.button_make = QtWidgets.QPushButton(alberti_disc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_make.sizePolicy().hasHeightForWidth())
        self.button_make.setSizePolicy(sizePolicy)
        self.button_make.setMinimumSize(QtCore.QSize(100, 30))
        self.button_make.setObjectName("button_make")
        self.horizontal_layout_3.addWidget(self.button_make)
        self.verticalLayout.addLayout(self.horizontal_layout_3)
        self.group_box_output = QtWidgets.QGroupBox(alberti_disc)
        self.group_box_output.setObjectName("group_box_output")
        self.verticalLayout_35 = QtWidgets.QVBoxLayout(self.group_box_output)
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.text_edit_output = QtWidgets.QTextEdit(self.group_box_output)
        self.text_edit_output.setReadOnly(True)
        self.text_edit_output.setObjectName("text_edit_output")
        self.verticalLayout_35.addWidget(self.text_edit_output)
        self.verticalLayout.addWidget(self.group_box_output)

        self.retranslateUi(alberti_disc)
        QtCore.QMetaObject.connectSlotsByName(alberti_disc)

    def retranslateUi(self, alberti_disc):
        _translate = QtCore.QCoreApplication.translate
        alberti_disc.setWindowTitle(_translate("alberti_disc", "Form"))
        self.group_box_input.setTitle(_translate("alberti_disc", "Input text"))
        self.label_key.setText(_translate("alberti_disc", "Key:"))
        self.combo_box_mode.setItemText(0, _translate("alberti_disc", "Encrypt"))
        self.combo_box_mode.setItemText(1, _translate("alberti_disc", "Decrypt"))
        self.label_key_alphabet_shift.setText(_translate("alberti_disc", "Key alphabet shift"))
        self.label_iteration_step.setText(_translate("alberti_disc", "Iteration step"))
        self.button_make.setText(_translate("alberti_disc", "Make"))
        self.group_box_output.setTitle(_translate("alberti_disc", "Output text"))
