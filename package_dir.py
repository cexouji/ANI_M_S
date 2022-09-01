# -*- coding: utf-8 -*-
import zipfile, os
def writeAllFileToZip(absDir,zipFile):
    for f in os.listdir(absDir):
        absFile=os.path.join(absDir, f)
        if os.path.isdir(absFile):
            relFile=absFile[len(os.getcwd())+1:]
            zipFile.write(relFile)
            writeAllFileToZip(absFile, zipFile)
        else: #判断是普通文件，直接写到zip文件中。
            relFile=absFile[len(os.getcwd())+1:]
            zipFile.write(relFile)
    return
def ZIP_file(file_path, zipfile_name):
    file_path_w = file_path.rsplit('/',1)[0]
    zipFilePath=os.path.join(file_path_w, zipfile_name)
    zipFile=zipfile.ZipFile(zipFilePath, "w", zipfile.ZIP_DEFLATED)
    #absDir='D:\PycharmProjects\pythonProject\Asset_Task_Management\dist\login_ATM_ui'
    cwd = os.getcwd()  # 获取当前工作目录
    os.chdir(os.path.dirname(file_path))
    writeAllFileToZip(file_path, zipFile)    # 压缩
    os.chdir(cwd)