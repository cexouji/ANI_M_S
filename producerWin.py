# -*- coding: utf-8 -*-

from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, \
    QMessageBox, QAbstractItemView, QLabel
from PySide6.QtCore import Qt, Slot, QItemSelectionModel, QModelIndex
from PySide6.QtGui import QCursor

from QmyComboBoxDelegate import QmyComboBoxDelegate
from ui_Producer_window import Ui_MainWindow
from configparser import ConfigParser
from EmptyDelegate import EmptyDelegate

class myProducerWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__logmysql()
        self.setWindowTitle('人员名单列表')

        #self.changed = True

        self.ui.tableView.setSelectionBehavior(QAbstractItemView.SelectItems)
        #self.ui.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.tableView.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.ui.tableView.setAlternatingRowColors(True)
        self.ui.tableView.verticalHeader().setDefaultSectionSize(22)
        self.ui.tableView.horizontalHeader().setDefaultSectionSize(60)

        self.LabProdNum = QLabel('当前人数:', self)
        self.LabProdNum.setMinimumWidth(180)
        self.ui.statusbar.addWidget(self.LabProdNum)
        #self.ui.open_sql_btn.setText('打开数据库?')
        #print(QSqlDatabase.drivers())
        self.ui.reload_btn.setEnabled(0)

    def __del__(self):
        print("myProducerWindow 对象被删除了")

    def set_limit(self, limit):
        self.limit = limit
        self.on_reload_btn_clicked()
        # if self.changed:
        #     self.changed = False
        # else:
        #     return
        if limit == 'GM':
                self.ui.tableView.setContextMenuPolicy(Qt.CustomContextMenu)  # 开启自定义菜单 (继承自 QWidget)
                self.ui.tableView.customContextMenuRequested.connect(self.tableWidgetCustomContextMenu)
                # self.ui.tableView.horizontalHeader().setContextMenuPolicy(Qt.CustomContextMenu)
                # self.ui.tableView.horizontalHeader().customContextMenuRequested.connect(self.tableWidgetCustomContextMenu2)
                self.tabModel.setEditStrategy(QSqlTableModel.OnFieldChange)     # 设置编辑策略 OnFieldChange 字段值变化就立即更新到数据库 OnRowChange(当前行变化更新到数据库)
                                                                                # OnManualSubmit(所有修改暂时缓存,需要手动调用submitAll()保存所有修改,或reverAll()取消修改)
                strList = ["资产组长", "资产", "动画组长", "动画", "制片"]
                self.__delegatePosition = QmyComboBoxDelegate()
                self.__delegatePosition.setItems(strList, True)
                self.ui.tableView.setItemDelegateForColumn(self.fldNum['position'], self.__delegatePosition)
            # self.ui.tableView.setItemDelegateForColumn(self.fldNum['id'], EmptyDelegate(self))  # 设置不可编辑
        else:
            if not limit in ['制片', 'GM']:
                self.ui.tableView.setColumnHidden(self.fldNum['tel_number'], True)
            self.ui.add_producer_btn.setEnabled(0)
            self.ui.delete_producer_btn.setEnabled(0)
            self.ui.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 所有都为不可编辑
        self.ui.reload_btn.setEnabled(1)
    # def tableWidgetCustomContextMenu2(self,pos):
    #     menu = QMenu(self)
    #     fuzhi = menu.addAction('tttt')
    #     niantie = menu.addAction('ssss')
    #     fuzhi.setChecked(1)
    #     fuzhi.setCheckable(1)
    #
    #     action = menu.exec(QCursor.pos())
    #     item = self.ui.tableView.indexAt(pos)
    #     # if action is fuzhi:
    #     #     print('ttttttt')
    #     if action is niantie:
    #         print('ssssssssss')

    def tableWidgetCustomContextMenu(self, pos):
        menu = QMenu(self)
        fuzhi = menu.addAction('复制')
        niantie = menu.addAction('黏贴')
        # if self.ui.tableView.columnAt(pos.x()) == 0:
        #     show_all_assets111 = menu.addAction('查看看看看')
        action = menu.exec(QCursor.pos())
        item = self.ui.tableView.indexAt(pos)
        if action is fuzhi:
            selindex = (self.ui.tableView.selectedIndexes())
            self.cdata = []
            for i in selindex:
                #print(self.tabModel.record(i.row()).value(i.column()))
                self.cdata.append([i.row(), i.column(), self.tabModel.record(i.row()).value(i.column())])
            print(self.cdata)
        if action is niantie:
            selindex = self.ui.tableView.selectedIndexes()
            if len(self.cdata) == 1 and len(selindex) > 1:
                for i in selindex:
                    self.tabModel.setData(self.tabModel.index(i.row(), i.column()), self.cdata[0][2])
                    self.tabModel.submit()

            if len(self.cdata) > 0:
                crow, ccolumn = selindex[0].row(), selindex[0].column()
                redrownum, redcolumnnum = self.cdata[0][0], self.cdata[0][1]
                for i in self.cdata:
                    self.tabModel.setData(self.tabModel.index(i[0]+crow-redrownum, i[1]+ccolumn-redcolumnnum), i[2])
                    self.tabModel.submit()


            #print(self.tabModel.record(item.row()).value(item.column()))
            #self.show_my_task()
    def __logmysql(self):
        configparser2 = ConfigParser()
        configparser2.read('./conf/conf.ini')
        read_content = configparser2.items('localdb')
        t = dict(read_content)
        # host=t['host'], user=t['user'], password=t['password'], database=t['database'])
        self.DB = QSqlDatabase.addDatabase('QMYSQL')
        self.DB.setDatabaseName(t['database'])
        self.DB.setHostName(t['host'])
        self.DB.setUserName(t['user'])
        self.DB.setPassword(t['password'])
    @Slot()
    def on_add_producer_btn_clicked(self):
        com_text = self.ui.pos_combox.currentText()
        producer_name = self.ui.name_lineEdit_2.text()
        tel_num = self.ui.tel_lineEdit.text()
        if producer_name:
            if len(tel_num) != 11:
                QMessageBox.critical(self, '提示', '请查看电话号码是否正确')
                return
        else:
            QMessageBox.critical(self, '提示', '请输入名字')
            return
        if self.tabModel.rowCount() == 0:
            pass
        else:
            for i in range(self.tabModel.rowCount()):
                aRec = self.tabModel.record(i)
                old_name = aRec.value('name')
                if producer_name == old_name:
                    QMessageBox.critical(self, '提示', '已经存在该人员,请勿重复添加')
                    return
        self.tabModel.insertRow(self.tabModel.rowCount(), QModelIndex())
        curIndex = self.tabModel.index(self.tabModel.rowCount()-1, 1)
        self.selModel.clearSelection()
        self.selModel.setCurrentIndex(curIndex, QItemSelectionModel.Select)
        currow = curIndex.row()
        self.tabModel.setData(self.tabModel.index(currow, self.fldNum["id"]), self.tabModel.rowCount())
        self.tabModel.setData(self.tabModel.index(currow, self.fldNum["name"]), producer_name)
        self.tabModel.setData(self.tabModel.index(currow, self.fldNum["tel_number"]), tel_num)
        self.tabModel.setData(self.tabModel.index(currow, self.fldNum["position"]), com_text)
        if not self.tabModel.submit():
            QMessageBox.critical(self, '提示', '添加失败,请查看是否为编号原因')
        self.LabProdNum.setText(' 当前人数: %d 人' % (self.tabModel.rowCount()))
    @Slot()
    def on_delete_producer_btn_clicked(self):
        curIndex = self.selModel.currentIndex()
        self.tabModel.removeRow(curIndex.row())
        #self.tabModel.deleteRowFromTable(curIndex.row())
        #self.LabProdNum.setText(' 当前人数: %d 人' % (self.tabModel.rowCount()))
    @Slot()
    def on_reload_btn_clicked(self):
        if self.DB.open():
            print('成功打开数据库')
            self.__openTable()
        else:
            print(self.DB.lastError().text())
            print('打开数据库错误')
        return True

    @Slot()
    def on_name_lineEdit_2_returnPressed(self):
        if self.ui.filter_comBox.currentText() == '姓名':
            producer_name = self.ui.name_lineEdit_2.text()
            if producer_name:
                self.tabModel.setFilter(f'name like "%{producer_name}%"')
            else:
                self.tabModel.setFilter('')
    @Slot()
    def on_filter_comBox_currentTextChanged(self):
        if self.ui.filter_comBox.currentText() == '无':
            for i in range(self.tabModel.rowCount()):
                self.ui.tableView.showRow(i)
            self.tabModel.setFilter('')
    @Slot()
    def on_pos_combox_currentTextChanged(self):
        if self.ui.filter_comBox.currentText() == '职位':
            com_text = self.ui.pos_combox.currentText()
            self.tabModel.setFilter('position = "%s"' % com_text)

    def __getFieldNames(self):      # 获取所有字段名称
        emptyRec = self.tabModel.record()       # 获取空记录, 只有字段名
        self.fldNum = {}
        for i in range(emptyRec.count()):
            fieldName = emptyRec.fieldName(i)   # 字段名
            #print(fieldName)
            #self.ui.tableView.addItem(fieldName)
            self.fldNum.setdefault(fieldName)
            self.fldNum[fieldName] = i
        #print(self.fldNum)      # 显示标题字典数据

    def __openTable(self):
        self.tabModel = QSqlTableModel(self, self.DB)    #数据模型
        #self.tabModel.setTable('sxd_assets')        # 设置数据表
        self.tabModel.setTable('producer_list')  # 设置数据表
        self.ui.tableView.setModel(self.tabModel)
        # self.tabModel.setEditStrategy(QSqlTableModel.OnFieldChange)     # 设置编辑策略 OnFieldChange 字段值变化就立即更新到数据库 OnRowChange(当前行变化更新到数据库)
                                                                            # OnManualSubmit(所有修改暂时缓存,需要手动调用submitAll()保存所有修改,或reverAll()取消修改)
        # self.tabModel.setSort(self.tabModel.fieldIndex('id'), Qt.AscendingOrder)    # 排序
        # self.tabModel.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.ui.tableView.verticalHeader().setVisible(False)    # 隐藏表头
        if self.tabModel.select() == False:   # 查询数据失败
            QMessageBox.critical(self, '查询数据失败', '打开数据表错误,出错消息\n'+self.tabModel.lastError().text())
            return
        self.__getFieldNames()
        headerlist = ['id', '名字', '电话', '职位']
        for num, i in enumerate(self.fldNum):
            self.tabModel.setHeaderData(self.fldNum[i], Qt.Horizontal, headerlist[num])
        # 创建界面组件与数据模型字段之间数据映射
        # self.mapper = QDataWidgetMapper()
        # self.mapper.setModel(self.tabModel)
        # self.mapper.setSubmitPolicy(QDataWidgetMapper.AutoSubmit)
        # 界面组件与tabmodel的具体字段之间的联系
        # self.mapper.addMapping(self.)
        self.selModel = QItemSelectionModel(self.tabModel)  # 选择模型
        # self.selModel.currentChanged.connect(self.do_currentChanged)
        # self.selModel.currentRowChanged.connect(self.do_currentRowChanged)
        self.ui.tableView.setModel(self.tabModel)               # 设置数据模型
        self.ui.tableView.setSelectionModel(self.selModel)      # 设置选择模型

        #self.ui.tableView.setColumnHidden(self.fldNum['department'], True)   # 隐藏列
        #self.ui.tableView.setColumnHidden(self.fldNum['position'], True)
        #print(self.tabModel.record(1).value("tel_number"))
        #self.tabModel.setFilter('department = "资产"')
        #self.tabModel.insertRow(self.tabModel.rowCount(), QModelIndex())
        #self.tabModel.removeRow(20)
        self.ui.tableView.resizeColumnsToContents()
        self.LabProdNum.setText(' 当前人数: %d 人' % (self.tabModel.rowCount()))
        #self.tabModel.setFilter('department = "%s"'%('资产'))

if __name__ == '__main__':
    app = QApplication([])
    t = myProducerWindow()
    t.set_limit('GM')
    t.show()
    app.exec()

