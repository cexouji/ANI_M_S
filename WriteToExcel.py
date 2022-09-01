# -*- coding: utf-8 -*-
#import os
from openpyxl import Workbook
def write_to_excel(pro_name, proj_jsondata, excel_path, data):
    wb = Workbook(excel_path)
    ws = wb.create_sheet(pro_name)
    ws.column_dimensions['A'].width = 5
    ws.column_dimensions['B'].width = 20
    ws.column_dimensions['C'].width = 20
    ws.column_dimensions['D'].width = 6
    ws.column_dimensions['E'].width = 8
    ws.column_dimensions['F'].width = 105
    ws.column_dimensions['G'].width = 105
    ws.append(['类型', '中文名', '英文名', '设计稿', '集数', 'maya路径', 'ue路径'])
    for as_type, zn_name, en_name, is_design, t_ep in data:
        asset_type = proj_jsondata['c_type'] if as_type == '角色' else proj_jsondata['p_type'] if as_type == '道具' else proj_jsondata['s_type'] if as_type == '场景' else proj_jsondata['e_type']
        c_ep = str(t_ep).rjust(3, '0')
        filepath = proj_jsondata['maya'].format(proj=pro_name, ep=proj_jsondata['ep'], num=c_ep, type=asset_type,
                                                name=en_name, param1=proj_jsondata['param1'], param2=proj_jsondata['param2'],
                                                param3=proj_jsondata['param3'], letter=proj_jsondata['letter'])
        filepath2 = proj_jsondata['ue'].format(proj=pro_name, ep=proj_jsondata['ep'], num=c_ep, type=asset_type,
                                                name=en_name, param1=proj_jsondata['param1'], param2=proj_jsondata['param2'],
                                                param3=proj_jsondata['param3'], letter=proj_jsondata['letter'])
        ws.append([as_type, zn_name, en_name, is_design, t_ep, filepath, filepath2])
    wb.save(excel_path)



if __name__ == '__main__':
    pass
    # SQL_deal = SQL_deal()
    # excel_path = 'D:\PycharmProjects\pythonProject\Asset_Task_Management\mytest_excel.xlsx'
    # data = SQL_deal.select_from_table_for_name('sxd_assets')
    # #data = 'dsadsa'
    # pro_base_path = 'D:\PycharmProjects\pythonProject'
    # pro_name = 'project_name'
    #write_to_excel(pro_name, pro_base_path, excel_path, data)