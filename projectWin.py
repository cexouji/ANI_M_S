# -*- coding: utf-8 -*-
import json
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtWidgets import QApplication, QMainWindow, \
    QMessageBox, QFileDialog
from PySide6.QtCore import Slot, Signal
from ui_Project_window import Ui_MainWindow
from configparser import ConfigParser
import SQLCONF
class myProjectWindow(QMainWindow):
    SENDPROJANDPATH = Signal(str, str, str)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__logmysql()
    def __del__(self):
        print("myProjectWindow 对象被删除了")
    def __logmysql(self):
        configparser2 = ConfigParser()
        configparser2.read('./conf/conf.ini')
        read_content = configparser2.items('localdb')
        t = dict(read_content)
        self.DB = QSqlDatabase.addDatabase('QMYSQL')
        self.DB.setDatabaseName(t['database'])
        self.DB.setHostName(t['host'])
        self.DB.setUserName(t['user'])
        self.DB.setPassword(t['password'])


    def set_edit(self, param):
        self.ui.drop_table_btn.setEnabled(0)
        self.ui.checkBox.setChecked(0)
        if param == 'a':
            self.ui.edit_project_btn.setEnabled(0)
            self.ui.add_project_btn.setEnabled(1)
            self.ui.name_lineEdit.setEnabled(1)
            self.ui.checkBox.setEnabled(0)

            self.reset_projWin()
            self.setWindowTitle('新建项目')
        else:
            self.ui.add_project_btn.setEnabled(0)
            self.ui.edit_project_btn.setEnabled(1)
            self.ui.name_lineEdit.setEnabled(0)
            self.ui.checkBox.setEnabled(1)
            self.setWindowTitle('编辑项目')
            if self.get_proj_data(param):
                return 1
    def reset_projWin(self):
        self.ui.name_lineEdit.setText('')
        self.ui.letter_lineEdit.setText('')
        self.ui.light_leader_lineEdit.setText('')
        self.ui.ani_leader_lineEdit.setText('')
        self.ui.asset_leader_lineEdit.setText('')
        self.ui.manager_lineEdit.setText('')
        self.ui.design_lineEdit.setText('{letter}:/{proj}_Project/01_documents/design/{type}/{name}')
        self.ui.backup_lineEdit.setText('{letter}:/{proj}_Project/01_documents/check/{type}/{name}')
        self.ui.uepath_lineEdit.setText('{letter}:/{proj}_Project/05_UE4/{type}/{name}')
        self.ui.mayapath_lineEdit.setText('{letter}:/{proj}_Project/03_main_prodution/ep000/assets/{type}/{name}')
        self.ui.ep_lineEdit_2.setText('ep')
        self.ui.ctype_lineEdit.setText('characters')
        self.ui.stype_lineEdit.setText('scenes')
        self.ui.ptype_lineEdit.setText('props')
        self.ui.etype_lineEdit.setText('env')
        self.ui.icon_path_lineEdit.setText('')
        self.ui.param1_lineEdit.setText('')
        self.ui.param2_lineEdit.setText('')
        self.ui.param3_lineEdit.setText('')
    def get_proj_data(self, curproj):
        if not self.DB.open():
            QMessageBox.critical(self, '提示', self.DB.lastError().text())
            return
        qry = QSqlQuery(self.DB)
        qry.exec('''SELECT * from project_list''')
        qry.first()
        while qry.isValid():            # id project_name  project_jsondata
            proj_name = qry.value('project_name')
            if curproj.upper() == proj_name.upper():
                #pro_jsondata = qry.value('project_jsondata')
                pro_jsondata = json.loads(qry.value('project_jsondata'))
                self.ui.name_lineEdit.setText(proj_name)
                self.get_curproj_json(pro_jsondata)
                return
            if not qry.next():
                QMessageBox.critical(self, '提示', '找不到该项目')
                return 1
    def get_curproj_json(self, json_data):
        self.ui.icon_path_lineEdit.setText(json_data["icon_path"])
        self.ui.manager_lineEdit.setText(json_data["manager"])
        try:
            self.ui.asset_leader_lineEdit.setText(json_data["asset_leader"])
            self.ui.ani_leader_lineEdit.setText(json_data["ani_leader"])
            self.ui.light_leader_lineEdit.setText(json_data["light_leader"])
        except:
            pass
        self.ui.ep_lineEdit_2.setText(json_data["ep"])
        self.ui.letter_lineEdit.setText(json_data["letter"])
        self.ui.param1_lineEdit.setText(json_data["param1"])
        self.ui.param2_lineEdit.setText(json_data["param2"])
        self.ui.param3_lineEdit.setText(json_data["param3"])
        self.ui.ctype_lineEdit.setText(json_data["c_type"])
        self.ui.stype_lineEdit.setText(json_data["s_type"])
        self.ui.ptype_lineEdit.setText(json_data["p_type"])
        self.ui.etype_lineEdit.setText(json_data["e_type"])
        self.ui.design_lineEdit.setText(json_data["design"])
        self.ui.backup_lineEdit.setText(json_data["backup"])
        self.ui.uepath_lineEdit.setText(json_data["ue"])
        self.ui.mayapath_lineEdit.setText(json_data["maya"])
        # dic = {"ep": ep, "param1": param1, "param2": param2, "param3": param3,
        #        "c_type": ctype, "s_type": stype, "p_type": ptype, "e_type": etype,
        #        "design": design, "backup": backup, "letter": letter,
        #        "ue": ue_path, "maya": maya_path, "icon_path": icon_path,
        #        "asset_leader": asset_leader, "ani_leader": ani_leader,
        #        "light_leader": light_leader, "manager": manager}
        # return json.dumps(dic, ensure_ascii=0)
    def proj_json_to_str(self):
        icon_path = self.ui.icon_path_lineEdit.text()
        manager = self.ui.manager_lineEdit.text()
        asset_leader = self.ui.asset_leader_lineEdit.text()
        ani_leader = self.ui.ani_leader_lineEdit.text()
        light_leader = self.ui.light_leader_lineEdit.text()
        ep = self.ui.ep_lineEdit_2.text()
        letter = self.ui.letter_lineEdit.text()
        param1 = self.ui.param1_lineEdit.text()
        param2 = self.ui.param2_lineEdit.text()
        param3 = self.ui.param3_lineEdit.text()
        ctype = self.ui.ctype_lineEdit.text()
        stype = self.ui.stype_lineEdit.text()
        ptype = self.ui.ptype_lineEdit.text()
        etype = self.ui.etype_lineEdit.text()
        design = self.ui.design_lineEdit.text().replace('\\', '/')
        backup = self.ui.backup_lineEdit.text().replace('\\', '/')
        ue_path = self.ui.uepath_lineEdit.text().replace('\\', '/')
        maya_path = self.ui.mayapath_lineEdit.text().replace('\\', '/')
        if icon_path and ep and ctype and stype and ptype and etype and letter \
                and design and backup and ue_path and maya_path:
            dic = {"ep": ep, "param1": param1, "param2": param2, "param3": param3,
                   "c_type": ctype, "s_type": stype, "p_type": ptype, "e_type": etype,
                   "design": design, "backup": backup, "letter": letter,
                   "ue": ue_path, "maya": maya_path, "icon_path": icon_path,
                   "asset_leader": asset_leader, "ani_leader": ani_leader,
                   "light_leader": light_leader, "manager": manager}
            return json.dumps(dic, ensure_ascii=0)
        else:
            print('请输入完整参数')
            return 0
    @Slot()     # 编辑项目
    def on_edit_project_btn_clicked(self):
        curproj = self.ui.name_lineEdit.text()
        if not self.DB.open():
            QMessageBox.critical(self, '提示', self.DB.lastError().text())
            return
        json_data = self.proj_json_to_str()
        qry = QSqlQuery(self.DB)
        qry.prepare('''UPDATE project_list SET project_jsondata=:project_jsondata WHERE project_name=:project_name''')
        qry.bindValue(':project_jsondata', json_data)
        qry.bindValue(':project_name', curproj)
        self.SENDPROJANDPATH.emit(curproj, self.ui.icon_path_lineEdit.text(), 'edit')
        if not qry.exec():
            QMessageBox.critical(self, '错误', qry.lastError().text())
        else:
            #self.SENDPROJANDPATH.emit(curproj, self.ui.icon_path_lineEdit.text(), 'add')
            QMessageBox.about(self, '提示', '修改成功')
    @Slot()     # 新建项目
    def on_add_project_btn_clicked(self):
        curproj = self.ui.name_lineEdit.text()
        if not curproj:
            QMessageBox.critical(self, '提示', '请输入项目')
            return
        if not self.DB.open():
            QMessageBox.critical(self, '提示', self.DB.lastError().text())
            return
        if curproj.upper() in self.get_project_name():
            QMessageBox.critical(self, '错误', f'warning: 已存在项目{curproj},无法新建该项目')
            return
        json_data = self.proj_json_to_str()
        qry = QSqlQuery(self.DB)
        qry.prepare('''INSERT INTO project_list (project_name, project_jsondata) VALUES(:project_name, :project_jsondata)''')
        qry.bindValue(':project_name', curproj)
        qry.bindValue(':project_jsondata', json_data)
        print(f'项目表中添加了项目 {curproj}')
        if not qry.exec():
            QMessageBox.critical(self, '错误', 'error:'+qry.lastError().text())
        else:
            assets_table_name = f'{curproj}_assets'
            qry.exec('''CREATE TABLE IF NOT EXISTS %s(%s)''' % (assets_table_name, SQLCONF.ASSETS_TABLE_CREATE))
            ani_table_name = f'{curproj}_ani_ep'
            qry.exec('''CREATE TABLE IF NOT EXISTS %s(%s)''' % (ani_table_name, SQLCONF.ANI_PROJ_TABLE_CREATE))
            self.SENDPROJANDPATH.emit(curproj, self.ui.icon_path_lineEdit.text(), 'add')
        #print('点击了新建项目')
    def get_project_name(self):
        qry = QSqlQuery()
        qry.exec('''SELECT project_name from project_list''')
        qry.first()
        proj_list = []
        while qry.isValid():
            proj_list.append(qry.value('project_name'))
            if not qry.next():
                break
        return proj_list
    @Slot()     # 预览路径
    def on_preview_btn_clicked(self):
        proj = self.ui.name_lineEdit.text()
        ep = self.ui.ep_lineEdit_2.text()
        letter = self.ui.letter_lineEdit.text()
        param1 = self.ui.param1_lineEdit.text()
        param2 = self.ui.param2_lineEdit.text()
        param3 = self.ui.param3_lineEdit.text()
        ctype = self.ui.ctype_lineEdit.text()
        stype = self.ui.stype_lineEdit.text()
        ptype = self.ui.ptype_lineEdit.text()
        etype = self.ui.etype_lineEdit.text()
        design = self.ui.design_lineEdit.text().replace('\\', '/')
        backup = self.ui.backup_lineEdit.text().replace('\\', '/')
        ue_path = self.ui.uepath_lineEdit.text().replace('\\', '/')
        maya_path = self.ui.mayapath_lineEdit.text().replace('\\', '/')
        msgBox = QMessageBox(self)
        msgBox.setWindowTitle('路径预览')
        msg_text = ''.join((f"角色路径\n设计稿:\t{design}\n反馈:\t{backup}\nue:\t{ue_path}\n资产:\t{maya_path}".format(proj=proj, ep=ep, num="{num}", type=ctype, param1=param1,
                                                                                                            param2=param2, param3=param3, letter=letter, name="{name}"),
                            f"\n场景路径\n设计稿:\t{design}\n反馈:\t{backup}\nue:\t{ue_path}\n资产:\t{maya_path}".format(proj=proj, ep=ep, num="{num}", type=stype, param1=param1,
                                                                                                              param2=param2, param3=param3, letter=letter, name="{name}"),
                            f"\n道具路径\n设计稿:\t{design}\n反馈:\t{backup}\nue:\t{ue_path}\n资产:\t{maya_path}".format(proj=proj, ep=ep, num="{num}", type=ptype, param1=param1,
                                                                                                              param2=param2, param3=param3, letter=letter, name="{name}"),
                            f"\n元素路径\n设计稿:\t{design}\n反馈:\t{backup}\nue:\t{ue_path}\n资产:\t{maya_path}".format(proj=proj, ep=ep, num="{num}", type=etype, param1=param1,
                                                                                                              param2=param2, param3=param3, letter=letter, name="{name}")))
        msgBox.setText(msg_text)
        msgBox.exec()  # 阻塞等待用户输入
    @Slot()     # 删除项目
    def on_drop_table_btn_clicked(self):
        curproj = self.ui.name_lineEdit.text()
        if not curproj:
            QMessageBox.critical(self, '提示', '请输入项目')
            return
        if not self.DB.open():
            QMessageBox.critical(self, '提示', self.DB.lastError().text())
            return
        if curproj.upper() in self.get_project_name():
            qry = QSqlQuery(self.DB)
            qry.prepare('''DELETE FROM project_list WHERE project_name=:project_name''')
            qry.bindValue(':project_name', curproj)
            print(f'项目表中删除了项目 {curproj}')
            if not qry.exec():
                QMessageBox.critical(self, '错误', 'error:' + qry.lastError().text())
            else:
                assets_table_name = f'{curproj}_assets'
                qry.exec('''DROP TABLE %s''' % (assets_table_name))
                ani_table_name = f'{curproj}_ani_ep'
                qry.exec('''DROP TABLE %s''' % (ani_table_name))
                self.SENDPROJANDPATH.emit(curproj, '', 'del')
            print('点击了删除项目')


        else:
            QMessageBox.critical(self, '提示', f'不存在 {curproj} 该项目')
    @Slot()
    def on_icon_path_toolBtn_clicked(self):
        select_filepath, _ = QFileDialog.getOpenFileName(caption='选择文件', filter='*')
        self.ui.icon_path_lineEdit.setText(select_filepath)

    # 窗口获取数据转化为json
    def project_json_to_str(self):
        icon_path = self.ui.icon_path_lineEdit.text()
        manager = self.ui.manager_lineEdit.text()
        asset_leader = self.ui.asset_leader_lineEdit.text()
        ani_leader = self.ui.ani_leader_lineEdit.text()
        light_leader = self.ui.light_leader_lineEdit.text()
        ep = self.ui.ep_lineEdit_2.text()
        letter = self.ui.letter_lineEdit.text()
        param1 = self.ui.param1_lineEdit.text()
        param2 = self.ui.param2_lineEdit.text()
        param3 = self.ui.param3_lineEdit.text()
        ctype = self.ui.ctype_lineEdit.text()
        stype = self.ui.stype_lineEdit.text()
        ptype = self.ui.ptype_lineEdit.text()
        etype = self.ui.etype_lineEdit.text()
        design = self.ui.design_lineEdit.text().replace('\\', '/')
        backup = self.ui.backup_lineEdit.text().replace('\\', '/')
        ue_path = self.ui.uepath_lineEdit.text().replace('\\', '/')
        maya_path = self.ui.mayapath_lineEdit.text().replace('\\', '/')
        if icon_path and ep and ctype and stype and ptype and etype and letter\
                and design and backup and ue_path and maya_path:
            dic = {"ep": ep, "param1": param1, "param2": param2, "param3": param3,
                   "c_type": ctype, "s_type": stype, "p_type": ptype, "e_type": etype,
                   "design": design, "backup": backup, "letter": letter,
                   "ue": ue_path, "maya": maya_path, "icon_path": icon_path,
                   "asset_leader": asset_leader, "ani_leader": ani_leader,
                   "light_leader": light_leader, "manager": manager}
            return json.dumps(dic, ensure_ascii=0)
        else:
            print('请输入完整参数')
            return 0



if __name__ == '__main__':
    app = QApplication([])
    t = myProjectWindow()
    if not t.set_edit('SSSS'):
        t.show()
        app.exec()

