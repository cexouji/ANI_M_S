# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QApplication, QMainWindow, QButtonGroup, QFileDialog, QTableWidgetItem, QMenu, QToolButton, QMessageBox, QTreeWidgetItem
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon, QPixmap, QColor, QCursor
#from PySide6.QtUiTools import QUiLoader
from ui_AssetManagement_window import Ui_MainWindow
import SendMessageToDD as SMGDD
from SQL_deal import SQL_deal
from WriteToExcel import write_to_excel
import datetime
import json, os
import package_dir
class ATM_UI(QMainWindow):
    def __init__(self, user_limit, producer_name, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('资产任务分配管理窗口')
        self.my_fire_sql = SQL_deal()   # 连接上数据库
        self.DD_send = SMGDD.SEND_MSG()  # 钉钉消息
        self.user_limit = user_limit
        self.producer = producer_name
        self.__connect_set()    # connect设置
        self.__init_param()     # 设置一些参数的初始值
    def __del__(self):
        del self.my_fire_sql
    def __connect_set(self):
        # 创建资产按钮 重置参数按钮
        self.ui.create_asset_btn.clicked.connect(self.create_asset)
        self.ui.reset_param_btn.clicked.connect(self.reset_assets_param)
        # 隐藏表格列的按钮控件关联   关联由单个按钮变为整个按钮组的变化
        self.ui.msr_btngrp.buttonClicked.connect(self.msr_hideColumn)
        #self.ui.mod_btn.clicked.connect(self.hideColumn)#self.ui.shad_btn.clicked.connect(self.hideColumn)#self.ui.rig_btn.clicked.connect(self.hideColumn)
        # 日历部分
        #self.ui.calendarWgt.selectionChanged.connect(self.calendar_sel)
        #self.ui.calendarWgt.clicked.connect(self.calendar_click)   # 点击
        self.ui.calendarWgt.activated.connect(self.calendar_active_click)     # 激活 这里好像双击会激活
        # 创建项目按钮组并且连接
        self.ui.project_btn_grp = QButtonGroup(self)
        self.ui.project_btn_grp.buttonClicked.connect(self.change_project)
        # 新建项目按钮
        self.ui.add_project_btn.clicked.connect(self.add_to_projects)
        self.ui.edit_project_btn.clicked.connect(self.edit_projects_table)
        self.ui.icon_path_toolBtn.clicked.connect(self.get_project_iconfile)
        # 删除项目(慎用)
        self.ui.drop_table_btn.clicked.connect(self.drop_table_and_data)
        # 多项修改
        self.ui.change_lineEdit.returnPressed.connect(self.edit_many_item)
        # 表格修改时
        if self.user_limit == '游客':
            pass
        else:
            self.ui.table_Wgt.cellChanged.connect(self.tablewgt_cell_changed)
            self.ui.table_Wgt.cellDoubleClicked.connect(self.tablewgt_cell_double_click)
        # canshu = ' yao shu chu de nei rong '    # 测试槽函数带参数的方式导入
        # self.ui.producer_list_btn.clicked.connect(partial(self.test,canshu))
        #self.ui.producer_list_btn.clicked.connect(lambda: self.test('参数'))  # 带参数的槽函数
        # 传数据到表格
        self.ui.write_excel_btn.clicked.connect(self.write_excel)
        self.ui.write_sec_btn.clicked.connect(self.show_excel_data)

        self.ui.search_lineEdit.returnPressed.connect(self.screen_all_data)     # 筛选
        #self.ui.producer_list_btn.clicked.connect(self.open_infotable_ui)
        self.ui.mod_fb_btn.clicked.connect(lambda: self.write_to_feedback(11))
        self.ui.shad_fb_btn.clicked.connect(lambda: self.write_to_feedback(18))
        self.ui.rig_fb_btn.clicked.connect(lambda: self.write_to_feedback(25))

        self.ui.add_producer_btn.clicked.connect(self.add_producer)
        self.ui.p_tablewgt.cellChanged.connect(self.p_tablewgt_cell_changed)

        self.ui.search_lineEdit_2.returnPressed.connect(self.show_child)
        self.ui.search_lineEdit_1.returnPressed.connect(self.search_name)
        self.ui.show_producer_btn.clicked.connect(self.write_to_producer_table)
        self.ui.show_htime_btn.clicked.connect(self.show_history_data)
        self.ui.preview_btn.clicked.connect(self.Q_Message_win3)
    def __init_param(self):
        # 初始设置
        self.read_msr_rem()
        self.is_write = False
        self.msr_hideColumn()  # 隐藏表格列的初始化
        self.ui.project_grpBox_gridLayout.setColumnStretch(6, 2)
        self.init_create_project_icon()     # 初始化创建项目图标
        #self.ui.table_Wgt.verticalHeader().setVisible(False)    # 表格隐藏表头
        self.History_Pname = ''     # 初始化历史项目选择记录
        self.table_change_sign = True   # 表格修改标记
        self.reload_num = None  # 刷新执行编号
        self.reload_sign = 2    # 刷新执行标记
        self.cur_project = self.ui.cur_project_name.text()
        self.ui.limit_label.setText(self.user_limit)
        self.ui.producer_label.setText(self.producer)
        self.ui.dockWidget_3.setVisible(0)
        if self.user_limit == '制片':
            self.ui.dockWidget_3.setEnabled(0)
        elif self.user_limit == '组长':
            self.ui.c_groupBox.setEnabled(0)
            self.ui.dockWidget_3.setEnabled(0)
        elif self.user_limit == '组员':
            #self.ui.table_Wgt.hideColumn(26)
            self.ui.mod_fb_btn.setEnabled(0)
            self.ui.shad_fb_btn.setEnabled(0)
            self.ui.rig_fb_btn.setEnabled(0)
            self.ui.c_groupBox.setEnabled(0)
            self.ui.dockWidget_3.setEnabled(0)
        elif self.user_limit == '游客':
            self.ui.mod_fb_btn.setEnabled(0)
            self.ui.shad_fb_btn.setEnabled(0)
            self.ui.rig_fb_btn.setEnabled(0)
            self.ui.c_groupBox.setEnabled(0)
            self.ui.dockWidget_3.setEnabled(0)
        else:
            self.ui.dockWidget_3.setFixedWidth(460)
        pixmap = QPixmap('./icons/logo1.png')
        pix = pixmap.scaledToHeight(60)
        self.ui.logo_label.setPixmap(pix)
        #
        self.color_g = [QColor('#000000'), QColor('#75664d'), QColor('#ffb61e'), QColor('#ae7000'),
                        QColor('#ff3300'), QColor('#f36838'), QColor('#057748'), QColor('#00e500')]
        # tablewgt的右键菜单
        self.ui.table_Wgt.setContextMenuPolicy(Qt.CustomContextMenu)  # 开启自定义菜单 (继承自 QWidget)
        self.ui.table_Wgt.customContextMenuRequested.connect(self.tableWidgetCustomContextMenu)
        table_width = {0: 24, 1: 68, 2: 88, 3: 48}
        for i in table_width:
            self.ui.p_tablewgt.setColumnWidth(i, table_width[i])
        if self.user_limit not in ['制片', 'GM']:
            self.ui.zp_grpBox.setEnabled(0)
            self.ui.p_tablewgt.hideColumn(2)
            self.ui.p_tablewgt.hideColumn(3)
    #-----------------------------------------右键菜单功能-------------------------------------------------
    # 菜单栏信息以及功能
    def tableWidgetCustomContextMenu(self, pos):
        menu = QMenu(self)
        show_my_tasks = menu.addAction('查看我的任务')
        show_all_assets = menu.addAction('查看所有资产')
        reload = menu.addAction('&F刷新')
        menu.addSeparator()
        submit_to_comp = menu.addAction('提交(进)')
        back_to_previous = menu.addAction('返回(退)')
        submit_to_back = menu.addAction('提交(反馈)')
        package_file = menu.addAction('打包文件')
        menu.addSeparator()
        edit_selectedItems = menu.addAction('多项修改')
        submit_selectedItems_to_comp = menu.addAction('多项提交')
        menu.addSeparator()
        view_modback = menu.addAction('查看模型反馈')
        view_shadback = menu.addAction('查看材质反馈')
        view_rigback = menu.addAction('查看绑定反馈')
        view_mod_histime = menu.addAction('查看模型历史时间')
        view_shad_histime = menu.addAction('查看材质历史时间')
        view_rig_histime = menu.addAction('查看绑定历史时间')
        if self.user_limit == 'GM':
            pass
        elif self.user_limit == '制片':
            back_to_previous.setEnabled(0)
            submit_selectedItems_to_comp.setEnabled(0)
        elif self.user_limit == '组长':
            package_file.setEnabled(0)
        else:
            #package_file.setVisible(0)
            package_file.setEnabled(0)
            back_to_previous.setEnabled(0)
            submit_to_back.setEnabled(0)
            edit_selectedItems.setEnabled(0)
            submit_selectedItems_to_comp.setEnabled(0)
            view_mod_histime.setEnabled(0)
            view_shad_histime.setEnabled(0)
            view_rig_histime.setEnabled(0)
            if self.user_limit == '游客':
                submit_to_comp.setEnabled(0)
        # 对应位置显示菜单栏 # mapToGlobal 返回 Point # exec 返回 action
        #action = menu.exec(self.ui.table_Wgt.mapToGlobal(pos))
        action = menu.exec(QCursor.pos())
        item = self.ui.table_Wgt.itemAt(pos)
        if action is show_my_tasks:
            self.show_my_task()
        elif action is edit_selectedItems:
            self.edit_many_item()
        elif action is show_all_assets:
            self.show_all_assets()
        elif action is reload:
            self.reload_table()
        elif action is submit_to_comp:
            self.deal_with_task(item, 'go')
        elif action is back_to_previous:
            self.deal_with_task(item, 'back')
        elif action is submit_to_back:
            self.deal_with_task(item, 'go_feedback')
        elif action is submit_selectedItems_to_comp:
            for i in self.ui.table_Wgt.selectedItems():
                self.deal_with_task(i, 'go')
        elif action is package_file:
            self.package_to_zip(item)
        elif action is view_modback:
            self.ui.detail_plainTextEdit.setPlainText(self.view_detail_info(item, 'mod_fb')) if item else self.set_Text('范围外,请选择某项')
        elif action is view_shadback:
            self.ui.detail_plainTextEdit.setPlainText(self.view_detail_info(item, 'shad_fb')) if item else self.set_Text('范围外,请选择某项')
        elif action is view_rigback:
            self.ui.detail_plainTextEdit.setPlainText(self.view_detail_info(item, 'rig_fb')) if item else self.set_Text('范围外,请选择某项')
        elif action is view_mod_histime:
            self.ui.detail_plainTextEdit.setPlainText(self.view_detail_info(item, 'mod_time_history')) if item else self.set_Text('范围外,请选择某项')
        elif action is view_shad_histime:
            self.ui.detail_plainTextEdit.setPlainText(self.view_detail_info(item, 'shad_time_history')) if item else self.set_Text('范围外,请选择某项')
        elif action is view_rig_histime:
            self.ui.detail_plainTextEdit.setPlainText(self.view_detail_info(item, 'rig_time_history')) if item else self.set_Text('范围外,请选择某项')
        else:
            pass
    # 显示详细信息
    def view_detail_info(self, cur_item, h_title):
        c_id = self.ui.table_Wgt.item(cur_item.row(), 0).text()
        detail_data = self.my_fire_sql.select_title_from_table(self.cur_table_name, h_title, c_id)
        detail_text = detail_data[0] if detail_data[0] else '无信息'
        return detail_text
    def package_to_zip(self, item):
        i_row = item.row()
        en_name = self.ui.table_Wgt.item(i_row, 4).text()
        as_type = self.ui.table_Wgt.item(i_row, 2).text()
        asset_type = self.dir_dic['c_type'] if as_type == '角色' else self.dir_dic['p_type'] if as_type == '道具' else self.dir_dic['s_type'] if as_type == '场景' else self.dir_dic['e_type']
        c_ep = self.ui.table_Wgt.item(i_row, 1).text().rjust(3, '0')     #
        final_path = self.dir_dic['maya'].format(proj=self.cur_project, ep=self.dir_dic['ep'], num=c_ep, type=asset_type,
                                              name=en_name, param1=self.dir_dic['param1'], param2=self.dir_dic['param2'],
                                              param3=self.dir_dic['param3'], letter=self.dir_dic['letter'])
        if os.path.isdir(final_path):
            zipfile_name = ''.join((en_name, '.zip'))
            package_dir.ZIP_file(final_path, zipfile_name)
            self.set_Text('打包完成')
        else:
            self.set_Text('请确认是否存在路径')
    # --------------------------------------------提交与反馈------------------------------------------------
    # 任务处理
    def deal_with_task(self, item, sign):
        if not item:
            return
        i_row = item.row()
        c_id = self.ui.table_Wgt.item(i_row, 0).text()  # cur_column = [0, 2, 3, 5, 6, 12, 13, 19, 20]
        asset_type = self.ui.table_Wgt.item(i_row, 2).text()
        zn_name = self.ui.table_Wgt.item(i_row, 3).text()
        en_name = self.ui.table_Wgt.item(i_row, 4).text()
        M_checked = self.ui.mod_btn.isChecked()
        S_checked = self.ui.shad_btn.isChecked()
        R_checked = self.ui.rig_btn.isChecked()
        column_grp = []
        if M_checked:
            column_grp.append(6)
        if S_checked:
            column_grp.append(13)
        if R_checked:
            column_grp.append(20)
        for i in column_grp:
            stage = '模型' if i == 6 else '材质' if i == 13 else '绑定'
            c_producer = self.ui.table_Wgt.item(i_row, i + 1).text()
            c_state = self.ui.table_Wgt.item(i_row, i).text()
            new_state = self.state_variety(c_state, sign)
            vc = self.ui.table_Wgt.item(i_row, i + 6).text()
            # self.p_leader 组长, self.p_manager 制片
            if c_state == '无':
                self.set_Text(f' {stage} 列的参数不可操作')
                continue
            elif new_state == '未完成' and c_state == '未分配':
                if c_producer:
                    self.ui.table_Wgt.item(i_row, i).setText(new_state)
                    # print(f'组长钉钉发布 {stage} 任务 发送消息给{c_producer}')
                    self.history_time_edit(c_id, i_row, i)  # 修改历史时间
                    writing = f'''{self.p_leader} 发布 {stage}-{asset_type}-{zn_name}-{en_name}-v{vc.rjust(2, '0')} 任务 接收人为 {c_producer}''' \
                        if int(vc) > 0 else f'''{self.p_leader} 发布 {stage}-{asset_type}-{zn_name}-{en_name} 任务 接收人为 {c_producer}'''
                    self.DD_send.send_MSG(writing, self.producer_tel_dict[c_producer])

                else:
                    self.set_Text('没有 组员 目标可以发布')
            elif new_state in ['通过', '已反馈'] and c_state == '待审核':
                self.ui.table_Wgt.item(i_row, i).setText(new_state)
                #print(f'组长钉钉提交 {stage} {new_state} 发送消息给 {c_producer}')
                self.history_time_edit(c_id, i_row, i)  # # 修改历史时间
                writing = f'''{self.p_leader} {new_state} {stage}-{asset_type}-{zn_name}-{en_name}-v{vc.rjust(2, '0')} 任务 接收人为 {c_producer}''' \
                    if int(vc) > 0 else f'''{self.p_leader} {new_state} {stage}-{asset_type}-{zn_name}-{en_name} 任务 接收人为 {c_producer}'''
                self.DD_send.send_MSG(writing, self.producer_tel_dict[c_producer])

            elif new_state == '待反馈' and c_state == '待审核':
                self.ui.table_Wgt.item(i_row, i).setText(new_state)
                #print(f'组长钉钉提交 {stage} 等待导演反馈 发送消息给制片')
                writing = f'''{self.p_leader} 提交 {stage}-{asset_type}-{zn_name}-{en_name}-v{vc.rjust(2, '0')} 任务 等待导演反馈 接收人为 {self.p_manager}''' \
                    if int(vc) > 0 else f'''{self.p_leader} 提交 {stage}-{asset_type}-{zn_name}-{en_name} 任务 等待导演反馈 接收人为 {self.p_manager}'''
                self.DD_send.send_MSG(writing, self.producer_tel_dict[self.p_manager])

            elif new_state == '通过' and c_state == '待反馈':
                self.ui.table_Wgt.item(i_row, i).setText(new_state)
                #print(f'制片钉钉通过 {stage} 发送消息给 {c_producer}')
                writing = f'''{self.p_manager} 已通过 {stage}-{asset_type}-{zn_name}-{en_name}-v{vc.rjust(2, '0')} 任务 接收人为 {c_producer}''' \
                    if int(vc) > 0 else f'''{self.p_manager} 已通过 {stage}-{asset_type}-{zn_name}-{en_name} 任务 接收人为 {c_producer}'''
                self.DD_send.send_MSG(writing, self.producer_tel_dict[c_producer])

            elif new_state == '已反馈' and c_state == '待反馈':
                self.ui.table_Wgt.item(i_row, i).setText(new_state)
                #print(f'制片钉钉发送 {stage} 的导演反馈给组员以及组长')
                writing = f'''{self.p_manager} 已反馈 {stage}-{asset_type}-{zn_name}-{en_name}-v{vc.rjust(2, '0')} 任务 接收人为 {self.p_leader} {c_producer}''' \
                    if int(vc) > 0 else f'''{self.p_manager} 已反馈 {stage}-{asset_type}-{zn_name}-{en_name} 任务 接收人为 {self.p_leader} {c_producer}'''
                self.DD_send.send_MSG(writing, self.producer_tel_dict[self.p_leader], self.producer_tel_dict[c_producer])

            elif new_state == '待审核' and c_state == '未完成':
                if c_producer == self.producer:
                    self.ui.table_Wgt.item(i_row, i).setText(new_state)
                    #print(f'组员钉钉发送 {stage} 待审核消息给组长')
                    writing = f'''{c_producer} 提交 {stage}-{asset_type}-{zn_name}-{en_name}-v{vc.rjust(2, '0')} 任务 等待审核 接收人为 {self.p_leader}''' \
                        if int(vc) > 0 else f'''{c_producer} 提交 {stage}-{asset_type}-{zn_name}-{en_name} 任务 等待审核 接收人为 {self.p_leader}'''
                    self.DD_send.send_MSG(writing, self.producer_tel_dict[self.p_leader])

                else:
                    self.set_Text('你无权限修改别人的任务')
            elif new_state == '待审核' and c_state == '已反馈':
                if c_producer == self.producer:
                    self.ui.table_Wgt.item(i_row, i).setText(new_state)
                    #print(f'组员钉钉发送 {stage} 待审核消息给组长')
                    writing = f'''{c_producer} 提交 {stage}-{asset_type}-{zn_name}-{en_name}-v{vc.rjust(2, '0')} 任务 等待审核 接收人为 {self.p_leader}''' \
                        if int(vc) > 0 else f'''{c_producer} 提交 {stage}-{asset_type}-{zn_name}-{en_name} 任务 等待审核 接收人为 {self.p_leader}'''
                    self.DD_send.send_MSG(writing, self.producer_tel_dict[self.p_leader])

                    self.ui.table_Wgt.item(i_row, i + 6).setText(str(int(vc)+1))
                else:
                    self.set_Text('你无权限修改别人的任务')
            elif new_state == '已上传' and c_state == '通过':
                if c_producer == self.producer:
                    self.ui.table_Wgt.item(i_row, i).setText(new_state)
                    #print(f'组员钉钉发送 {stage} 已上传消息组长和制片')
                    writing = f'''{c_producer} 已上传 {stage}-{asset_type}-{zn_name}-{en_name}-v{vc.rjust(2, '0')} 任务 接收人为 {self.p_leader} {self.p_manager}''' \
                        if int(vc) > 0 else f'''{c_producer} 已上传 {stage}-{asset_type}-{zn_name}-{en_name} 任务 接收人为 {self.p_leader} {self.p_manager}'''
                    self.DD_send.send_MSG(writing, self.producer_tel_dict[self.p_leader], self.producer_tel_dict[self.p_leader])
                else:
                    self.set_Text('你无权限修改别人的任务')
            else:
                self.set_Text('什么都没做')
    # 状态变化条件
    def state_variety(self, task_state, s_num):
        if self.user_limit == '组长':
            if task_state == '未分配':
                if s_num == 'go':
                    new_state = '未完成'
                else:
                    new_state = ''
            elif task_state == '待审核':
                if s_num == 'back':
                    new_state = '已反馈'
                elif s_num == 'go':
                    new_state = '通过'
                else:
                    new_state = '待反馈'
            else:
                new_state = ''
        elif self.user_limit == '制片':
            if task_state == '待反馈':
                if s_num == 'go':
                    new_state = '通过'
                else:
                    new_state = '已反馈'
            else:
                new_state = ''
        elif self.user_limit == 'GM':
            new_state = ''
        else:
            if task_state == '未完成':
                new_state = '待审核'
            elif task_state == '已反馈':
                new_state = '待审核'
            elif task_state == '通过':
                new_state = '已上传'
            else:
                new_state = ''
        return new_state
    #------------------------------------------------------------------------------------------------------
    # 多项编辑item
    def edit_many_item(self):
        a = self.ui.table_Wgt.selectedItems()
        #self.set_Text('')
        if not a:
            self.set_Text('没有选中相关内容')
            return
        c_text = self.ui.change_lineEdit.text()
        if c_text:
            for i in a:
                self.ui.table_Wgt.item(i.row(), i.column()).setText(c_text)
        else:
            self.set_Text('请输入需要修改成的数据')
    # 筛选
    def screen_all_data(self):
        try:
            #cur_project_data = self.my_fire_sql.select_from_table(self.cur_table_name)
            cur_project_data = self.my_fire_sql.select_from_table_to_screen(self.cur_table_name)
        except:
            self.set_Text('还未选项目获取数据')
            return
        cur_text = self.ui.search_lineEdit.text()
        if not cur_text:
            self.reload_table()
            return
        for i in cur_project_data:
            tmp_num = 0
            for j in i:
                if tmp_num:
                    if cur_text.upper() in str(j).upper():
                        self.ui.table_Wgt.showRow(i[0]-1)
                        break
                else:
                    tmp_num = 1
            else:
                self.ui.table_Wgt.hideRow(i[0]-1)
    # --------------------------------------项目图标相关---------------------------------------------
    # 创建项目图标
    def init_create_project_icon(self):
        projects_data = self.my_fire_sql.select_from_table('project_list')
        for i in projects_data:
            project_data = json.loads(i[2])
            t_btn = QToolButton()
            if os.path.exists(project_data['icon_path']):
                t_btn.setIcon(QIcon(project_data['icon_path']))
            else:
                t_btn.setIcon(QIcon('./icons/black.jpg'))
            t_btn.setCheckable(True)
            t_btn.setIconSize(QSize(80, 80))
            t_btn.setText(i[1])
            t_btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
            self.ui.project_grpBox_gridLayout.addWidget(t_btn)
            self.ui.project_btn_grp.addButton(t_btn)
    # 添加项目图标
    def add_project_icon(self, project_name, icon_path):
        t_btn = QToolButton()
        if not os.path.exists(icon_path):
            icon_path = './icons/black.jpg'
        t_btn.setIcon(QIcon(icon_path))
        t_btn.setCheckable(True)
        t_btn.setIconSize(QSize(80, 80))
        t_btn.setText(project_name)
        t_btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.ui.project_grpBox_gridLayout.addWidget(t_btn)
        self.ui.project_btn_grp.addButton(t_btn)
    # ----------------------------------------制片用相关-----------------------------------------------
    # 制片用 重置创建资产参数
    def reset_assets_param(self):
        self.ui.type_cbBox.setCurrentIndex(0)
        self.ui.zn_lineEdit.clear()
        self.ui.en_lineEdit.clear()
        self.ui.ep_lineEdit.clear()
        self.ui.design_of_CBox.setChecked(1)
        self.ui.mod_of_CBox.setChecked(1)
        self.ui.shad_of_CBox.setChecked(1)
        self.ui.rig_of_CBox.setChecked(1)
    # 创建项目中打开选择路径或文件
    # def get_project_base_dir(self):
    #     select_filepath = QFileDialog.getExistingDirectory(caption='选择项目文件夹')
    #     self.ui.base_path_lineEdit.setText(select_filepath)
    def get_project_iconfile(self):
        select_filepath, _ = QFileDialog.getOpenFileName(
            caption='选择文件', filter='*')
        self.ui.icon_path_lineEdit.setText(select_filepath)

    # 制片用创建资产
    def create_asset(self):
        assets_type = self.ui.type_cbBox.currentText()
        zn_name = self.ui.zn_lineEdit.text().strip()
        en_name = self.ui.en_lineEdit.text().strip()
        c_ep = self.ui.ep_lineEdit.text().strip()
        designed = 1 if self.ui.design_of_CBox.isChecked() else 0
        mod_of = 2 if self.ui.mod_of_CBox.isChecked() else 1
        shad_of = 2 if self.ui.shad_of_CBox.isChecked() else 1
        rig_of = 2 if self.ui.rig_of_CBox.isChecked() else 1
        # print(assets_type,zn_name,en_name,designed,mod_of,shad_of,rig_od)
        project = self.ui.cur_project_name.text()
        if project == '请选择项目':
            self.set_Text('请先选择项目')
            return
        if not zn_name or not en_name:
            self.set_Text('英文名或中文名为空')
            return
        else:
            self.my_fire_sql.insert_into_assets(project, assets_type, zn_name, en_name, designed, mod_of, shad_of, rig_of, c_ep)
    # --------------------------------------------------------------------------------------------
    # 添加项目
    def project_json_to_str(self):
        icon_path = self.ui.icon_path_lineEdit.text()
        manager = self.ui.manager_lineEdit.text()
        leader = self.ui.leader_lineEdit.text()
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
                   "leader": leader, "manager": manager}
            return json.dumps(dic, ensure_ascii=0)
        else:
            self.set_Text('请输入完整参数')
            return 0
    def add_to_projects(self):
        proj = self.ui.name_lineEdit.text()
        icon_path = self.ui.icon_path_lineEdit.text()
        if proj:
            self.my_fire_sql.create_assets_table(proj)
            json_str = self.project_json_to_str()
            if json_str:
                tmp = self.my_fire_sql.insert_into_projects(proj, json_str)
                if tmp:
                    self.add_project_icon(proj, icon_path)
            else:
                self.set_Text('请输入完整参数')
        else:
            self.set_Text('请输入项目名称')
            # tmp = self.my_fire_sql.insert_into_projects(p_name, p_icon_path)
            # if tmp:
            #     self.add_project_icon(p_name, p_icon_path)
    # 删除项目!!!!
    def drop_table_and_data(self):
        p_name = self.ui.name_lineEdit.text()
        if p_name:
            for i in self.ui.project_btn_grp.buttons():
                if i.text() == p_name:
                    self.ui.project_btn_grp.removeButton(i)
                    # 根据index获取位置
                    # index = (self.ui.project_grpBox_gridLayout.indexOf(i))
                    # pos = self.ui.project_grpBox_gridLayout.getItemPosition(index)
                    # print(self.ui.project_grpBox_gridLayout.itemAtPosition(pos[0], pos[1]).widget())
                    #takeat = (self.ui.project_grpBox_gridLayout.takeAt(index))
                    #self.ui.project_grpBox_gridLayout.removeItem(takeat)
                    self.ui.project_grpBox_gridLayout.removeWidget(i)
                    i.deleteLater()  # i.setMaximumWidth(0)
                    del(i)      # del(takeat)
                    self.my_fire_sql.drop_table(f'{p_name}_assets')
                    self.my_fire_sql.delete_project_data(p_name)
                    break
            else:
                self.set_Text('没有与该名称对应的项目')
        else:
            self.set_Text('请输入项目名称')
    # 编辑项目
    def edit_projects_table(self):
        proj = self.ui.name_lineEdit.text()
        p_icon_path = self.ui.icon_path_lineEdit.text()
        if proj:
            json_str = self.project_json_to_str()
            if json_str:
                self.my_fire_sql.update_projects_data(proj, json_str)
                for i in self.ui.project_btn_grp.buttons():
                    if i.text() == proj:
                        if os.path.exists(p_icon_path):
                            i.setIcon(QIcon(p_icon_path))
                        else:
                            i.setIcon(QIcon('./icons/black.jpg'))
                        break
            else:
                self.set_Text('请完整输入对应参数')
        else:
            self.set_Text('请输入项目名称')

    # -----------------------------------------------------------------------------------
    #项目图标点击
    def change_project(self, cur_btn):
        self.cur_project = cur_btn.text()   # 当前项目
        self.ui.cur_project_name.setText(self.cur_project)  # 设置
        self.cur_table_name = ''.join((self.cur_project, '_assets'))    # 当前项目表格
        project_data = self.my_fire_sql.select_project_param(self.cur_project)  # 当前项目数据
        self.producer_tel_dict = {i[1]: i[2] for i in self.my_fire_sql.select_from_table('producer_list')}  # 人员名单字典数据
        # 需打开文件路径字典数据
        self.dir_dic = json.loads(project_data[2])
        self.p_leader = self.dir_dic["leader"]
        self.p_manager = self.dir_dic["manager"]
        self.show_my_task()
    # 表格列隐藏的变化条件
    def msr_hideColumn(self):
        M_checked = self.ui.mod_btn.isChecked()
        S_checked = self.ui.shad_btn.isChecked()
        R_checked = self.ui.rig_btn.isChecked()
        for i in [7, 8, 9, 10, 11, 12, 13]:
            self.ui.table_Wgt.showColumn(i - 1) if M_checked else self.ui.table_Wgt.hideColumn(i - 1)
        for i in [14, 15, 16, 17, 18, 19, 20]:
            self.ui.table_Wgt.showColumn(i - 1) if S_checked else self.ui.table_Wgt.hideColumn(i - 1)
        for i in [21, 22, 23, 24, 25, 26, 27]:
            self.ui.table_Wgt.showColumn(i - 1) if R_checked else self.ui.table_Wgt.hideColumn(i - 1)
        font = self.ui.mod_btn.font()
        font.setBold(M_checked)
        self.ui.mod_btn.setFont(font)
        font = self.ui.shad_btn.font()
        font.setBold(S_checked)
        self.ui.shad_btn.setFont(font)
        font = self.ui.rig_btn.font()
        font.setBold(R_checked)
        self.ui.rig_btn.setFont(font)
        self.ui.table_Wgt.resizeColumnsToContents()     # 重置大小
        if self.is_write:
            self.write_msr_rem()
        self.is_write = True
    def calendar_active_click(self, date):
        sel_date = (date.toString('yyyy-MM-dd'))
        sel_Items = self.ui.table_Wgt.selectedItems()   # 日历点击
        if sel_Items:
            for i in sel_Items:
                s_column = i.column()
                if s_column in [9, 16, 23]:
                    i.setText(sel_date)
        else:
            self.ui.change_lineEdit.setText(sel_date)
    # 检查历史项目名称与现在的名称
    def check_history_name(self):
        if self.History_Pname == self.cur_project and self.notify_of and self.reload_sign == self.reload_num:
            self.set_Text('选择的项目与操作相同,不再操作')
            return 1
        else:
            self.reload_sign = self.reload_num
            self.History_Pname = self.cur_project
            self.ui.table_Wgt.setRowCount(0)
    # 显示我的任务
    def show_my_task(self):
        self.reload_sign = 1
        self.reload_num = 1
        if self.cur_project == '请选择项目':
            self.set_Text('请先选择项目')
            return
        if self.ui.table_Wgt.rowCount() == 0 or not self.check_history_name():
            if self.check_table_exists(self.cur_table_name):
                self.write_to_table()
            else:
                self.set_Text('不存在当前选择的项目')
                return
        task_data_g = self.my_fire_sql.select_from_table_to_my_task(self.cur_table_name)
        if self.user_limit == '组员':
            for i in task_data_g:
                if (i[2] == self.producer and i[1] in ['未完成', '已反馈']) or \
                        (i[4] == self.producer and i[3] in ['未完成', '已反馈']) or\
                        (i[6] == self.producer and i[5] in ['未完成', '已反馈']):
                    self.ui.table_Wgt.showRow(i[0]-1)
                else:
                    self.ui.table_Wgt.hideRow(i[0]-1)
        elif self.user_limit == '组长':
            for i in task_data_g:
                if i[1] in ['未分配', '待审核'] or i[3] in ['未分配', '待审核'] or i[5] in ['未分配', '待审核']:
                    self.ui.table_Wgt.showRow(i[0] - 1)
                else:
                    self.ui.table_Wgt.hideRow(i[0] - 1)
        elif self.user_limit == '制片':
            for i in task_data_g:
                if i[1] == '待反馈' or i[3] == '待反馈' or i[5] == '待反馈':
                    self.ui.table_Wgt.showRow(i[0] - 1)
                else:
                    self.ui.table_Wgt.hideRow(i[0] - 1)
        else:
            pass
        self.notify_of = True
    # 显示选择项目的所有资产
    def show_all_assets(self):
        self.reload_num = 0
        if self.cur_project == '请选择项目':
            self.set_Text('请先选择项目')
            return
        if self.check_history_name():
            if self.notify_of:
                return
        if self.check_table_exists(self.cur_table_name):
            self.write_to_table()
        else:
            self.set_Text('不存在当前选择的项目')
        self.notify_of = True
    # 检查选择的项目是否有数据表
    def check_table_exists(self, table_name):
        for i in self.my_fire_sql.show_tables():
            if i == table_name.lower():
            #if i == table_name:        #在linux中使用这个
                return 1
        else:
            return 0
    # 刷新按钮 现在为任务选择的刷新
    def reload_table(self):
        self.notify_of = False
        try:
            self.notify_result(self.reload_num)
        except:
            self.set_Text('没有前置操作')
    # 写入数据到表格
    def write_to_table(self):
        self.cur_project_data = self.my_fire_sql.select_from_table(self.cur_table_name)
        self.table_change_sign = True
        if self.cur_project_data:
            lineNo = 0
            for i in self.cur_project_data:
                self.ui.table_Wgt.insertRow(lineNo)
                for num in range(27):
                    if num in [10, 17, 24]:   # 剩余时间部分
                        if i[num-4] == '已上传':
                            table_item = QTableWidgetItem('完成')
                        elif i[num - 1]:
                            remain_day = (i[num - 1] - datetime.datetime.now()).days + 1
                            if remain_day < 0:
                                table_item = QTableWidgetItem('过期')
                            else:
                                table_item = QTableWidgetItem(''.join((str(remain_day), ' 天')))
                        else:
                            table_item = QTableWidgetItem('')
                    elif i[num] is None:
                        table_item = QTableWidgetItem('')
                    elif num in [11, 18, 25]:
                        if i[num] == '':
                            table_item = QTableWidgetItem('无')
                        else:
                            table_item = QTableWidgetItem('有')
                    elif num in [9, 16, 23]:   # 时间部分
                            table_item = QTableWidgetItem(i[num].strftime('%Y-%m-%d'))
                    else:
                        table_item = QTableWidgetItem(str(i[num]))
                        if num in [6, 13, 20]:
                            color = self.back_color(str(i[num]))
                            table_item.setForeground(color)
                    table_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 居中显示
                    # table_item.setFont(QtGui.QFont("微软雅黑", 12, QFont.Black))  # 设置字体
                    self.ui.table_Wgt.setItem(lineNo, num, table_item)
                lineNo += 1
            self.ui.table_Wgt.resizeColumnsToContents() # 将行显示内容匹配
        self.table_change_sign = False
    # 编辑历史记录
    def history_time_edit(self, c_id, i_row, i):
        history_time = self.cur_project_data[i_row][i + 4]
        end_time = self.ui.table_Wgt.item(i_row, i + 3).text()
        if history_time:
            for j in history_time.split('\n'):
                if j == self.ui.table_Wgt.item(i_row, i + 3).text():
                    break
            else:
                new_his_time = ''.join((history_time, '\n', end_time))
                self.my_fire_sql.update_data(self.cur_table_name, c_id, i + 4, new_his_time)
        else:
            if end_time:
                self.my_fire_sql.update_data(self.cur_table_name, c_id, i + 4, end_time)
    # 表格内容变化触发
    def tablewgt_cell_changed(self, row, column):
        if self.table_change_sign:
            return
        c_id = (self.ui.table_Wgt.item(row, 0).text())
        new_data = (self.ui.table_Wgt.item(row, column).text())
        #print(c_id, new_data)
        if self.user_limit == 'GM':
            self.update_sql_data(self.cur_table_name, c_id, column, new_data)
            return
        if column in [0, 10, 11, 17, 18, 24, 25]:
            self.set_Text('不可直接修改')
        elif column in [1, 2, 3, 4]:
            if self.user_limit == '制片':
                self.update_sql_data(self.cur_table_name, c_id, column, new_data)
            else:
                self.set_Text('无权修改')
        elif column in [6, 13, 20]:
            if self.user_limit == '组员':
                if new_data not in ['4', '8', '待审核', '已上传']:
                    self.set_Text('无权随意修改状态')
                    return
            else:
                if new_data not in ['1', '2', '3', '4', '5', '6', '7', '8', '无', '未分配', '未完成', '待审核', '已反馈', '待反馈',
                                    '通过', '已上传']:
                    self.set_Text('请输入适当的状态')
                    return
            self.update_sql_data(self.cur_table_name, c_id, column, new_data)
            # 修改颜色
            self.table_change_sign = True
            color = self.back_color(new_data)
            self.ui.table_Wgt.item(row, column).setForeground(color)
            self.table_change_sign = False
        elif column in [7, 14, 21]:
            if self.user_limit == '组员':
                self.set_Text('无权修改')
            else:
                if self.ui.table_Wgt.item(row, column - 1).text() == '无':
                    self.set_Text('无法分配人员')
                else:
                    if new_data in self.producer_tel_dict:
                        self.update_sql_data(self.cur_table_name, c_id, column, new_data)
                    else:
                        self.set_Text(f'修改失败, {new_data} 不在人员名单中,如想添加,请联系制片添加对应人员')
        elif column in [8, 9, 15, 16, 22, 23]:
            if self.user_limit == '组员':
                self.set_Text('无权修改')
            else:                           # 5,12,19
                if self.ui.table_Wgt.item(row, (column//10) * 7 + 5).text() == '无':
                    self.set_Text('无法修改时间')
                else:
                    self.update_sql_data(self.cur_table_name, c_id, column, new_data)
        else:
            self.update_sql_data(self.cur_table_name, c_id, column, new_data)
    # 双击表格触发实现的内容
    def tablewgt_cell_double_click(self, row, column):
        if column in [3, 4]:
            if self.Q_Message_win2():
                #final_path = self.dir_dic['MAYA'].format(project=self.cur_project,ep=c_ep,name=en_name,type=asset_type)
                key = 'maya'
            else:
                key = 'ue'
        elif column == 5:
            key = 'design'
        elif column in [11, 18, 25]:
            key = 'backup'
        else:
            return
        en_name = self.ui.table_Wgt.item(row, 4).text()
        as_type = self.ui.table_Wgt.item(row, 2).text()
        #asset_type = 'character' if as_type == '角色' else 'prop' if as_type == '道具' else 'scene'
        asset_type = self.dir_dic['c_type'] if as_type == '角色' else self.dir_dic['p_type'] if as_type == '道具' else self.dir_dic['s_type'] if as_type == '场景' else self.dir_dic['e_type']
        #c_ep = f'''ep{self.ui.table_Wgt.item(row, 26).text().rjust(3, '0')}'''      #
        c_ep = self.ui.table_Wgt.item(row, 1).text().rjust(3, '0')
        try:
            final_path = self.dir_dic[key].format(proj=self.cur_project, ep=self.dir_dic['ep'], num=c_ep, type=asset_type,
                                                  name=en_name, param1=self.dir_dic['param1'], param2=self.dir_dic['param2'],
                                                  param3=self.dir_dic['param2'], letter=self.dir_dic['letter'])
            if os.path.exists(final_path):
                os.startfile(final_path)
            else:
                if self.Q_Message_win(final_path):
                    os.makedirs(final_path)
                    os.startfile(final_path)
        except:
            pass
    def Q_Message_win(self,file_path):
        msgBox = QMessageBox(self)
        msgBox.setWindowTitle('提示')
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText(f"{file_path}")
        msgBox.setInformativeText("路径不存在,你要创建并打开该路径吗?")
        connectButton = msgBox.addButton("确认", QMessageBox.ActionRole)
        abortButton = msgBox.addButton("取消", QMessageBox.ActionRole)
        msgBox.exec()     # 阻塞等待用户输入
        if msgBox.clickedButton() == connectButton:
            return 1
        elif msgBox.clickedButton() == abortButton:
            return 0
    def Q_Message_win2(self):
        msgBox = QMessageBox(self)
        msgBox.setWindowTitle('选择')
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText("选择maya或ue路径")
        connectButton = msgBox.addButton("maya", QMessageBox.ActionRole)
        connect2Button = msgBox.addButton("ue", QMessageBox.ActionRole)
        msgBox.exec()
        if msgBox.clickedButton() == connectButton:
            return 1
        elif msgBox.clickedButton() == connect2Button:
            return 0
    def Q_Message_win3(self):
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
        #msgBox.setIcon(QMessageBox.Question)
        # msg_text = f"设计稿:\t{design}\n反馈:\t{backup}\nue:\t{ue_path}\n资产:\t{maya_path}".format(proj=proj, ep=ep, num="{num}", type="{type}",
        #                                                     param1=param1, param2=param2, param3=param3, letter=letter, name="{name}")
        msg_text = ''.join((f"角色路径\n设计稿:\t{design}\n反馈:\t{backup}\nue:\t{ue_path}\n资产:\t{maya_path}".format(proj=proj, ep=ep, num="{num}",
                                        type=ctype, param1=param1, param2=param2, param3=param3, letter=letter, name="{name}"),
                                f"\n场景路径\n设计稿:\t{design}\n反馈:\t{backup}\nue:\t{ue_path}\n资产:\t{maya_path}".format(proj=proj, ep=ep,num="{num}",
                                        type=stype,param1=param1,param2=param2,param3=param3,letter=letter,name="{name}"),
                                f"\n道具路径\n设计稿:\t{design}\n反馈:\t{backup}\nue:\t{ue_path}\n资产:\t{maya_path}".format(proj=proj, ep=ep, num="{num}",
                                        type=ptype, param1=param1, param2=param2, param3=param3, letter=letter, name="{name}"),
                                f"\n元素路径\n设计稿:\t{design}\n反馈:\t{backup}\nue:\t{ue_path}\n资产:\t{maya_path}".format(proj=proj,ep=ep,num="{num}",
                                        type=etype,param1=param1,param2=param2,param3=param3,letter=letter,name="{name}")))
        msgBox.setText(msg_text)
        msgBox.exec()     # 阻塞等待用户输入
    # 修改数据库以及表格参数
    def update_sql_data(self, table_name, c_id, column, new_data):
        self.my_fire_sql.update_data(table_name, c_id, column, new_data)
    # 显示反馈
    def set_Text(self, text):
        self.ui.statusbar.showMessage(text, 2000)
        #self.ui.detail_plainTextEdit.setPlainText(text)
    # 写入到反馈
    def write_to_feedback(self, column):
        cur_row = self.ui.table_Wgt.currentRow()
        if cur_row == -1:
            self.set_Text('请选择需要写入反馈的项')
        else:
            c_id = self.ui.table_Wgt.item(cur_row, 0).text()
            feedback_text = self.ui.detail_plainTextEdit.toPlainText()
            self.update_sql_data(self.cur_table_name, c_id, column, feedback_text)
    # ---------------------------------------人员名单表/历史名单表-------------------------------------------------
    def write_to_producer_table(self):
        producer_data = self.my_fire_sql.select_from_table('producer_list')
        self.table_change_sign = True
        if self.ui.p_tablewgt.rowCount():
            self.ui.p_tablewgt.setRowCount(0)
        if producer_data:
            lineNo = 0
            for i in producer_data:
                self.ui.p_tablewgt.insertRow(lineNo)
                for num in range(4):
                    table_item = QTableWidgetItem(str(i[num]))
                    table_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.ui.p_tablewgt.setItem(lineNo, num, table_item)
                lineNo += 1
        self.table_change_sign = False
    # 表格变化修改
    def p_tablewgt_cell_changed(self, row, column):
        if self.table_change_sign:
            return
        if self.user_limit not in ['制片', 'GM']:
            self.set_Text('你无权修改')
            return
        c_id = self.ui.p_tablewgt.item(row, 0).text()
        new_data = self.ui.p_tablewgt.item(row, column).text()
        # if new_data in [4, '4', 'GM'] and self.user_limit == '制片':
        #     self.set_Text('你无权修改')
        #     return
        if column in [2, 3, 4]:
            t = self.my_fire_sql.update_producer_data(c_id, column, new_data)
            if t:
                self.set_Text('修改失败,请检查内容')
    # 表格中添加
    def add_producer(self):
        com_text = self.ui.pos_combox.currentText()
        producer_name = self.ui.name_lineEdit_2.text()
        tel_num = self.ui.tel_lineEdit.text()
        self.table_change_sign = True
        if producer_name:
            if len(tel_num) != 11:
                self.table_change_sign = False
                self.set_Text('请查看电话号码是否正确')
                return
            t = self.my_fire_sql.insert_into_producer_list(producer_name, tel_num, com_text)
            if t:
                lineNo = self.ui.p_tablewgt.rowCount()
                self.ui.p_tablewgt.insertRow(lineNo)
                data_g = [str(lineNo + 1), producer_name, tel_num, com_text]
                for num in range(4):
                    table_item = QTableWidgetItem(data_g[num])
                    table_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.ui.p_tablewgt.setItem(lineNo, num, table_item)
            else:
                self.set_Text('已经存在该人员,请勿重复添加')
        self.table_change_sign = False
        self.producer_tel_dict = {i[1]: i[2] for i in self.my_fire_sql.select_from_table('producer_list')}
    # 获得历史记录
    def show_history_data(self):
        if self.cur_project == '请选择项目':
            self.set_Text('请先选择项目')
            return
        history_time_data = self.my_fire_sql.select_from_table_to_histroy(self.cur_table_name)
        self.ui.history_treeWgt.clear()
        characters_item = QTreeWidgetItem(self.ui.history_treeWgt)
        characters_item.setText(0, '角色')
        props_item = QTreeWidgetItem(self.ui.history_treeWgt)
        props_item.setText(0, '道具')
        scenes_item = QTreeWidgetItem(self.ui.history_treeWgt)
        scenes_item.setText(0, '场景')
        env_item = QTreeWidgetItem(self.ui.history_treeWgt)
        env_item.setText(0, '元素')
        for type, zn_name, en_name, mod_ht, shad_ht, rig_ht in history_time_data:
            if type == '角色':
                item = QTreeWidgetItem(characters_item)
            elif type == '道具':
                item = QTreeWidgetItem(props_item)
            elif type == '场景':
                item = QTreeWidgetItem(scenes_item)
            else:
                item = QTreeWidgetItem(env_item)
            item.setText(0, zn_name)
            if mod_ht:
                mod_item = QTreeWidgetItem(item)
                mod_item.setText(0, '模型')
                for i in mod_ht.split('\n'):
                    t_item = QTreeWidgetItem(mod_item)
                    t_item.setText(0, i)
            if shad_ht:
                shad_item = QTreeWidgetItem(item)
                shad_item.setText(0, '材质')
                for i in shad_ht.split('\n'):
                    t_item = QTreeWidgetItem(shad_item)
                    t_item.setText(0, i)
            if rig_ht:
                rig_item = QTreeWidgetItem(item)
                rig_item.setText(0, '绑定')
                for i in rig_ht.split('\n'):
                    t_item = QTreeWidgetItem(rig_item)
                    t_item.setText(0, i)
    def search_name(self):
        if self.cur_project == '请选择项目':
            self.set_Text('请先选择项目')
            return
        param = self.ui.search_lineEdit_1.text()
        if param:
            item = self.ui.p_tablewgt.findItems(param, Qt.MatchRecursive | Qt.MatchWildcard)      # | Qt.MatchFixedString
            tmp = []
            for i in item:
                tmp.append(i.row())
                #self.ui.p_tablewgt.showRow(i.row())
            for i in range(self.ui.p_tablewgt.rowCount()):
                if i in tmp:
                    self.ui.p_tablewgt.showRow(i)
                else:
                    self.ui.p_tablewgt.hideRow(i)
        else:
            for i in range(self.ui.p_tablewgt.rowCount()):
                self.ui.p_tablewgt.showRow(i)
    # 测试输出子目标
    def show_child(self):
        if self.cur_project == '请选择项目':
            self.set_Text('请先选择项目')
            return
        param = self.ui.search_lineEdit_2.text()
        self.ui.history_treeWgt.collapseAll()
        self.ui.history_treeWgt.setCurrentItem(None)
        if param:
            item = self.ui.history_treeWgt.findItems(param,
                                                     Qt.MatchRecursive | Qt.MatchWildcard)  # | Qt.MatchFixedString
            for i in item:
                self.ui.history_treeWgt.setItemSelected(i, 1)
                self.expand_parent(i)
    # 循环找父节点
    def expand_parent(self, item):
        item.setExpanded(1)
        if item.parent():
            item.parent().setExpanded(1)
            self.expand_parent(item.parent())
    # -------------------------------------------------------------------------------------------------
    # 读取写入一些与自身有关的文件
    def read_msr_rem(self):
        try:
            with open('./config_files/msr_switch.txt', 'r', encoding='utf-8') as f:
                a = f.readline()
            m, s, r = a.split(',')
            if m == 'True':
                self.ui.mod_btn.setChecked(1)
            if s == 'True':
                self.ui.shad_btn.setChecked(1)
            if r == 'True':
                self.ui.rig_btn.setChecked(1)
        except:
            pass

    def write_msr_rem(self):
        with open('./config_files/msr_switch.txt', 'w', encoding='utf-8') as f:
            d = ','.join((str(self.ui.mod_btn.isChecked()), str(self.ui.shad_btn.isChecked()),
                          str(self.ui.rig_btn.isChecked())))
            f.write(d)
    # 写入到表格
    def write_excel(self):
        excel_path = self.ui.excel_path_lineEdit.text()
        if self.cur_project == '请选择项目':
            self.set_Text('请先选择项目')
            return
        if os.path.isfile(excel_path):
            #data =
            data = self.my_fire_sql.select_from_table_for_name(self.cur_table_name)
            write_to_excel(self.cur_project, self.dir_dic, excel_path, data)
        else:
            self.set_Text('请输入正确的excel表格路径')
    def show_excel_data(self):
        a = self.ui.table_Wgt.selectedItems()
        print(self.ui.table_Wgt.currentRow())
        tmp = []
        for i in a:
            cur_row = i.row()
            tmp2 = []
            for j in [2, 3, 4, 5, 1]:
                tmp2.append(self.ui.table_Wgt.item(cur_row, j).text())
            tmp.append(tmp2)
        excel_path = self.ui.excel_path_lineEdit.text()
        if self.cur_project == '请选择项目':
            self.set_Text('请先选择项目')
            return
        if os.path.isfile(excel_path):
            write_to_excel(self.cur_project, self.dir_dic, excel_path, tmp)
        else:
            self.set_Text('请输入正确的excel表格路径')
    # 以字典方式来运行方法
    def other(self):
        print('print other')
    def notify_result(self, num):
        numbers = {
            0: self.show_all_assets,
            1: self.show_my_task,
            2: self.other
        }
        method = numbers.get(num, self.other)
        if method:
            method()
    # 输入状态反馈颜色值
    def back_color(self, c_state):
        color = self.color_g[0] if c_state == '无' else self.color_g[1] if c_state == '未分配' else \
                self.color_g[2] if c_state == '未完成' else self.color_g[3] if c_state == '待审核' else \
                self.color_g[4] if c_state == '已反馈' else self.color_g[5] if c_state == '待反馈' else \
                self.color_g[6] if c_state == '通过' else self.color_g[7]
        return color

if __name__ == "__main__":
    app = QApplication([])
    Asset_Managenment = ATM_UI('组长', '张')
    Asset_Managenment.show()
    app.exec()