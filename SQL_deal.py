# -*- coding: utf-8 -*-
from pymysql import connect
import SQLCONF
from configparser import ConfigParser

class SQL_deal():
    def __init__(self):
        self.link_MySQL()
        self.create_table('project_list', SQLCONF.PROJECTINFO_CREATE)
        self.create_table('producer_list', SQLCONF.PRODUCER_LIST_CREATE)
    def link_MySQL(self):
        #链接数据库
        #t = SQLCONF.SQL_LOG
        configparser2 = ConfigParser()
        configparser2.read('./conf/conf.ini')
        read_content = configparser2.items('localdb')
        t = dict(read_content)
        self.conn = connect(host=t['host'], port=int(t['port']), user=t['user'], password=t['password'], database=t['database'])
        self.cs1 = self.conn.cursor()
    def __del__(self):
        try:
            self.cs1.close()
            self.conn.close()
            print('---------------- link off--------------------')
        except:
            print('-----------------no link--------------------')
    def sql_exe(self, sql_word):
        return self.cs1.execute(sql_word)
    #---------------------------------------增------------------------------------
    def create_table(self, table_name, table_type_conf):
        create_table = '''create table if not exists %s(%s)''' % (table_name, table_type_conf)
        self.sql_exe(create_table)

    def create_assets_table(self, project):
        # 创建资产表
        table_name = f'{project}_assets'
        self.create_table(table_name, SQLCONF.ASSETS_TABLE_CREATE)


    # 插入人员名单数据
    def producer_list_insert(self, name, tel=None):
        check = f'''select name from producer_list where name = '{name}' '''
        self.sql_exe(check)
        tmp = self.cs1.fetchall()
        if tmp:
            print(f'已有人员 {name}')
            return
        if tel:
            in_exe = f'''insert into producer_list values (0,'{name}', '{tel}')'''
        else:
            in_exe = f'''insert into producer_list(name) values ('{name}')'''
        print(in_exe)
        self.sql_exe(in_exe)
        self.conn.commit()
    # 插入资产数据
    def insert_into_assets(self, project, asset_type, cn_name, en_name, design, mod_state, shad_state, rig_state, f_ep):
        table_name = f'{project}_assets'
        check = f'''select en_name from {table_name} where en_name = '{en_name}' '''
        self.sql_exe(check)
        tmp = self.cs1.fetchall()
        if tmp:
            print(f'已有资产 {cn_name}-{en_name}')
            return
        in_exe = f'''insert into {table_name}(asset_type,cn_name,en_name,design,mod_state,shad_state,rig_state,f_ep) 
                    values ('{asset_type}','{cn_name}','{en_name}','{design}','{mod_state}','{shad_state}','{rig_state}','{f_ep}')'''
        self.sql_exe(in_exe)
        print(f'添加资产 {cn_name}-{en_name} 成功')
        self.conn.commit()
    # 插入到项目表
    def insert_into_projects(self, project_name, project_jsondata):
        check = f'''select project_name from project_list where project_name = '{project_name}' '''
        self.sql_exe(check)
        tmp = self.cs1.fetchall()
        if tmp:
            print(f'已有项目 {project_name}')
            return 0
        #in_exe = f'''insert into {table_name} values(0,'{project_name}','JSAN_OBJECT{project_jsondata}')'''
        in_exe = f'''insert into project_list values(0,'{project_name}','{project_jsondata}')'''
        #print(f'''新建项目 {project_name}''')
        self.sql_exe(in_exe)
        self.conn.commit()
        return 1
    # 插入到人员名单
    def insert_into_producer_list(self, producer_name, tel_num, department, position):
        #table_name = 'producer_list'
        check = f'''select name from producer_list where name = '{producer_name}' '''
        self.sql_exe(check)
        tmp = self.cs1.fetchall()
        if tmp:
            print(f'已有人员 {producer_name}')
            return 0
        in_exe = f'''insert into producer_list values(0,'{producer_name}','{tel_num}','{position}')'''
        print(f'''添加人员 {producer_name}, 电话 {tel_num}, 部门 {department}, 职位 {position}''')
        self.sql_exe(in_exe)
        self.conn.commit()
        return 1
    #----------------------删-----------------------------
    def drop_table(self, table_name):
        # 删除数据表-慎用
        drop_table = 'drop table if exists %s' % table_name
        self.sql_exe(drop_table)
        print('已删除数据表%s' % table_name)
    def delete_project_data(self, project_name):
        # 删除项目表中内容-慎用
        delete_data = f'''delete from project_list where project_name='{project_name}' '''
        self.sql_exe(delete_data)
        self.conn.commit()
        print('删除数据表项目表中项目数据 %s' % project_name)
    #----------------------改-----------------------------
    # 修改数据库内容
    def update_data(self, table_name, c_id, c_num, new_data):
        tabel_title = self.desc_table(table_name)
        column_name = tabel_title[c_num]
        update_data_state = '''update %s set %s="%s" where id = %s''' % (table_name, column_name, new_data, c_id)
        try:
            self.sql_exe(update_data_state)
            self.conn.commit()
            print('修改 %s 中 %s 列, id=%s 为 %s 成功' % (table_name, column_name, c_id, new_data))
            return 0
        except:
            print('修改 %s 中 %s 列, id=%s 为 %s 但失败了' % (table_name, column_name, c_id, new_data))
            return 1
    # 修改项目表格
    def update_projects_data(self, project_name, project_jsondata):
            #table_name = 'project_list'
            check = f'''select project_name from project_list where project_name = '{project_name}' '''
            self.sql_exe(check)
            tmp = self.cs1.fetchall()
            if tmp:
                update_exe = f'''update project_list set project_jsondata ='{project_jsondata}'
                where project_name ='{project_name}' '''
                print(f'''修改项目 {project_name} 成功''')
                self.sql_exe(update_exe)
                self.conn.commit()
            else:
                print(f'没有名为{project_name}的项目')
    # 修改人员名单表格
    def update_producer_data(self, c_id, column, new_data):
        table_name = 'producer_list'
        table_title = self.desc_table(table_name)
        column_name = table_title[column]
        update_exe = '''update %s set %s="%s" where id = %s''' % (table_name, column_name, new_data, c_id)
        try:
            self.sql_exe(update_exe)
            self.conn.commit()
            print('修改 %s 中 %s 列, id=%s 为 %s 成功' % (table_name, column_name, c_id, new_data))
            return 0
        except:
            print('修改 %s 中 %s 列, id=%s 为 %s 但失败了' % (table_name, column_name, c_id, new_data))
            return 1
    #----------------------查-----------------------------
    def show_tables(self):
        #列出已有数据表
        self.sql_exe('show tables')
        table_list = []
        for i in self.cs1.fetchall():
            table_list.append(i[0])
        return table_list
    def select_from_table(self, table_name):
        #查询表内数据
        try:
            self.conn.commit()
        except:
            pass
        self.sql_exe('select * from %s' % table_name)
        return self.cs1.fetchall()
    def select_from_table_for_name(self, table_name):
        sel_exe = f'select asset_type,cn_name,en_name,design,f_ep from {table_name} '
        self.sql_exe(sel_exe)
        return self.cs1.fetchall()
    def select_from_table_to_screen(self, table_name):
        sel_exe = f'select id,f_ep,asset_type,cn_name,en_name,design,mod_state,mod_producer,mod_end_time,shad_state,shad_producer,shad_end_time,rig_state,rig_producer,rig_end_time from {table_name} '
        self.sql_exe(sel_exe)
        return self.cs1.fetchall()
    def select_from_table_to_my_task(self, table_name):
        # 筛选用的查询
        try:
            self.conn.commit()
        except:
            pass
        sel_exe = f'select id,mod_state,mod_producer,shad_state,shad_producer,rig_state,rig_producer from {table_name} '
        self.sql_exe(sel_exe)
        return self.cs1.fetchall()
    def select_from_table_to_histroy(self, table_name):
        try:
            self.conn.commit()
        except:
            pass
        sel_exe = f'select asset_type,cn_name,en_name,mod_time_history,shad_time_history,rig_time_history from {table_name} '
        self.sql_exe(sel_exe)
        return self.cs1.fetchall()
    def select_title_from_table(self, table_name, h_title, c_id):
        # 查询表内类型名称数据
        try:
            self.conn.commit()
        except:
            pass
        self.sql_exe('select %s from %s where id=%s' % (h_title, table_name, c_id))
        return self.cs1.fetchone()
    def select_project_param(self, project_name):
        self.sql_exe(f'''select * from project_list where project_name='{project_name}' ''')
        return self.cs1.fetchone()
    def desc_table(self, table_name):
        #查询数据表标题名称
        self.sql_exe('desc %s' % table_name)
        t = []
        for i in self.cs1.fetchall(): t.append(i[0])
        return t
    def count_incomp(self, table_name, type_num):
        #查询某列数据为'未完成'的个数
        type = 'mod_state' if type_num == 3 else 'shader_state' if type_num == 4 else 'rig_state'
        self.sql_exe('select count(*) from %s where %s ="未完成" ' % (table_name, type))
        count = self.cs1.fetchone()
        return count[0]
if __name__ == '__main__':
    test = SQL_deal()
    #test.drop_table('SDP_assets')

    # test.drop_table('SDP_assets')
    # test.drop_table('project_list')
    # test.drop_table('producer_list')
    # test.drop_table('cjyz_assets')
    #
    # test.drop_table('producer_list')
    # test.create_producer_list()     # 人员名单
    # test.create_assets_table('SDP')    # 创建项目 输入项目名称
    #

    # test.insert_assets('SDP',3,'中文名1','yingwenmi1',0,2,1,2)
    # test.insert_assets('SDP',2, '打算的撒', 'Ydsanw1',1, 2, 2, 1)
    # test.producer_list_insert('张陈兄', '15005071072')
    # test.producer_list_insert('李兄', )
    # test.producer_list_insert('张无兄', )
    #print(test.desc_table('SDP_assets'))
    #test.create_producer_list()
    #test.insert_data_to_table()
