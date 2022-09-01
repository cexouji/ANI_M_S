# -*- coding: utf-8 -*-
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QStyledItemDelegate, QComboBox


class QmyComboBoxDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__itemList = []
        self.__isEditable = False
    def setItems(self, itemList, isEditable=False):
        self.__itemList = itemList
        self.__isEditable = isEditable
    def createEditor(self, parent, option, index):
        editor = QComboBox(parent)
        editor.setFrame(False)
        editor.setEditable(self.__isEditable)
        editor.addItems(self.__itemList)
        return editor
    def setEditorData(self, editor, index):
        model = index.model()
        text = model.data(index, Qt.EditRole)
        editor.setCurrentText(text)
    def setModelDate(self, editor, model, index):
        text = editor.currentText()
        model.setDate(index, text, Qt.EditRole)
    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)