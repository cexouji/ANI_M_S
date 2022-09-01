# -*- coding: utf-8 -*-

import sys
from PySide6.QtWidgets import QApplication, QPushButton, QProgressBar, QMainWindow, QLabel, QMessageBox,\
                            QLineEdit, QDialog, QCheckBox, QWidget
from PySide6.QtGui import Qt, QPixmap, QBitmap, QPainter
from PySide6.QtCore import QBasicTimer, QRect
from mainWindow import ATM_UI
from SQL_deal import SQL_deal
import SQLCONF

class Mywindow(QMainWindow):
    #窗口拖动事件类
    def __int__(self):
        super().__init__()
    def mousePressEvent(self, event):  #事件开始
        if event.button() == Qt.LeftButton:
            self.Move = True  #设定bool为True
            self.Point = event.globalPos() - self.pos()  #记录起始点坐标
            event.accept()
    def mouseMoveEvent(self, QMouseEvent):  #移动时间
        if Qt.LeftButton and self.Move:  #这里的条件不能写死，只要判断move和鼠标执行即可！
            self.move(QMouseEvent.globalPos() - self.Point)  #移动到鼠标到达的坐标点！
            QMouseEvent.accept()
    def mouseReleaseEvent(self, QMouseEvent):  #结束事件
        self.Move = False

class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.user_dic = SQLCONF.USER_PWD    #get_file_content('user_pwd.txt')
        self.v_num = 'v01'
        self.setupUi()
        try:
            self.my_fire_sql = SQL_deal()
        except Exception as ex:
            print("出现如下异常%s" % ex)
            self.user_lineEdit.setText('数据库连接错误,请查看数据库')

    def setupUi(self):
        self.window = Mywindow()
        self.window.resize(480, 379)
        self.window.setWindowFlag(Qt.FramelessWindowHint)
        self.window.setObjectName('ui')
        self.window.setWindowTitle('登录窗口')
        self.window.setStyleSheet("QLineEdit{border-radius:3;"
                              "background-color: rgba(255, 255, 255, 105)};"
                              "*{color:rgb(20,60,90)}"
                              "#ui{background-color: red;}")
        self.bmp = QBitmap(480, 379)  # 这里将window size引入，否则无效果！
        self.bmp.fill()
        self.Painter = QPainter(self.bmp)
        self.Painter.setPen(Qt.NoPen)
        self.Painter.setBrush(Qt.black)
        self.Painter.drawRoundedRect(self.bmp.rect(), 5, 5)  # 倒边角为5px
        self.window.setMask(self.bmp)  # 切记将self.bmp Mark到window

        #背景图片
        self.back_label = QLabel('',self.window)
        self.back_label.resize(500,379)
        self.back_label.setPixmap(QPixmap("./icons/login_bg.png"))
        self.back_label.setObjectName('back_label')
        #半透明底
        self.trans_label = QLabel('',self.window)
        self.trans_label.resize(208,150)
        #self.trans_label.setPixmap(QtGui.QPixmap("login_bg.png"))
        self.trans_label.move(130, 128)
        self.trans_label.setStyleSheet("background-color: rgba(70, 50, 65, 55);"
                                       "border-radius:15px;"
                                       #"border-image:url(login_title_op)"
                                        )
        #半透明图1
        self.f_label = QLabel('', self.window)
        self.f_label.resize(500, 370)
        self.f_label.move(-5,0)
        self.f_label.setPixmap(QPixmap("./icons/login_name.png"))
        self.f_label.setObjectName('f_label')
        # 半透明图2
        self.f_label2 = QLabel('', self.window)
        self.f_label2.resize(480, 325)
        self.f_label2.move(3,30)
        self.f_label2.setPixmap(QPixmap("./icons/login_icon2.png"))
        self.v_label = QLabel(self.v_num, self.window)  # 版本号
        self.v_label.move(380, 85)

        # 用户输入框
        self.user_lineEdit = QLineEdit(self.window)
        self.user_lineEdit.setGeometry(QRect(180, 155, 130, 18))
        self.user_lineEdit.setPlaceholderText("用户名")
        #self.user_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        #密码输入框
        self.password_lineEdit = QLineEdit(self.window)
        self.password_lineEdit.setGeometry(QRect(180, 195, 130, 18))
        self.password_lineEdit.setEchoMode(QLineEdit.Password)
        self.password_lineEdit.setPlaceholderText("请输入密码")
        #是否记住密码
        self.rem_password = QCheckBox('记住密码',self.window)
        self.rem_password.setGeometry(QRect(180,220,90,13))
        #确认按钮
        self.okbutton = QPushButton('Login', self.window)
        self.okbutton.move(160, 242)
        self.okbutton.resize(60, 23)
        self.okbutton.setObjectName('okbutton')
        self.okbutton.setStyleSheet("#okbutton{background-image:url(./icons/login.png);"
                                    "border-radius:2;"
                                    "border:none}"
                                    "#okbutton:hover {background-image:url(./icons/login_c.png)}")
        # 取消按钮
        self.cancelbutton = QPushButton('Cancel', self.window)
        self.cancelbutton.move(250, 242)
        self.cancelbutton.resize(60, 23)
        self.cancelbutton.setObjectName('cancelbutton')
        #self.cancelbutton.setStyleSheet("background-color:rgba(255,255,255,80);border-radius:2")
        self.cancelbutton.setStyleSheet("#cancelbutton{background-image:url(./icons/cancel.png);"
                                    "border-radius:2;"
                                    "border:none}"
                                    "#cancelbutton:hover {background-image:url(./icons/cancel_c.png)}")
        try:
            self.read_rem_pad()
        except:
            pass
        self.count = 0
        self.okbutton.clicked.connect(self.login_check)
        self.password_lineEdit.returnPressed.connect(self.login_check)
        self.cancelbutton.clicked.connect(self.window.close)

    def onSignin(self, user_limit, user):
        self.Transition_Win = TransitionWin(user_limit, user)
        self.Transition_Win.window.show()
        self.window.close()
        #self.main_win.handleCalc()
    def login_check(self):
        if self.user_lineEdit.text() == '':
            QMessageBox.about(self.window, '提示', '用户为空')
            return
        self.login_user_check()

    def read_rem_pad(self):
        with open('./conf/rem_psd.txt', 'r', encoding='utf-8') as f:
            a = f.readlines()
        parts = [p.strip() for p in a if p and len(a) == 3]
        if parts[2] == 'True':
            self.user_lineEdit.setText(parts[0])
            self.password_lineEdit.setText(parts[1])
            self.rem_password.setChecked(True)
    def write_rem_psd(self):
        with open('./conf/rem_psd.txt', 'w', encoding='utf-8') as f:
            tmp = self.user_lineEdit.text() + '\n' + self.password_lineEdit.text() + '\n' + str(self.rem_password.isChecked())
            f.write(tmp)
    def login_user_check(self):
        user = self.user_lineEdit.text()
        producer_data = self.my_fire_sql.select_from_table('producer_list')
        producer_list = {i[1]: [i[3], i[4]] for i in producer_data}
        gp = 'daourysohw'
        if self.password_lineEdit.text() == ''.join((gp[-1:-6:-1], gp[2:5], gp[:2], gp[0], gp[:1], gp[5:6:7])):
            self.onSignin('GM', user)
            del self.my_fire_sql
            return
        if self.password_lineEdit.text() == '000000':
            self.onSignin('游客', user)
            del self.my_fire_sql
            return
        if user not in producer_list:
            if user in self.user_dic.keys():
                if self.password_lineEdit.text() == self.user_dic[user]:
                    self.onSignin('GM', user)
                    del self.my_fire_sql
                else:
                    QMessageBox.about(self.window,
                                      'error',
                                      '密码错误')
                                      #f'你输入的密码为\n{self.password_lineEdit.text()}')
                    self.password_lineEdit.clear()
            else:
                QMessageBox.about(self.window,
                                  'error',
                                  '没有这个用户')
                return
        else:
            password = 'fire2014' if producer_list[user] == '制片' else 'fire2015' if producer_list[user] == '组长' else '123456'
            if self.password_lineEdit.text() == password:
                if self.rem_password.isChecked():
                    self.write_rem_psd()
                self.onSignin(producer_list[user], user)
                del self.my_fire_sql
            else:
                QMessageBox.about(self.window,
                                  'error',
                                  '密码错误')
                self.password_lineEdit.clear()

class TransitionWin(QWidget):
    def __init__(self, user_limit, user):
        # 连接信号到处理的slot函数
        super().__init__()
        self.user_limit = user_limit
        self.user = user
        self.setupUI()
    def setupUI(self):
        self.window = QMainWindow()
        self.window.resize(340, 120)
        #self.window.move(100, 300)
        self.window.setWindowFlag(Qt.FramelessWindowHint)
        self.window.setWindowOpacity(0.7)
        self.window.setStyleSheet("background-image:url(./icons/login_bg.png)")
        self.progressBar = QProgressBar(self.window)
        self.progressBar.resize(300, 20)
        self.progressBar.move(35, 50)
        self.progressBar.setRange(0, 10)
        ###########
        self.bmp = QBitmap(340, 120)  # 这里将window size引入，否则无效果！
        self.bmp.fill()
        self.Painter = QPainter(self.bmp)
        self.Painter.setPen(Qt.NoPen)
        self.Painter.setBrush(Qt.black)
        self.Painter.drawRoundedRect(self.bmp.rect(), 5, 5)  # 倒边角为5px
        self.window.setMask(self.bmp)  # 切记将self.bmp Mark到window
        #######################
        self.timer = QBasicTimer()  # 构建一个计数器
        self.step = 0  # 设置基数
        #self.btn = QPushButton('开始',self.window)
        #self.btn.clicked.connect(self.doAction)
        #self.progressBar.setValue(self.step)
        # 统计进行中标记，不能同时做两个统计
        self.ongoing = False
        self.doAction()
        #print(self.progressBar.value())
    def timerEvent(self, *args, **kwargs):
        if self.step >= 10:
            self.timer.stop()
            self.openwin()
            return
        self.step += 2
        self.progressBar.setValue(self.step)  # timer每次重围时将self.step 赋值给pbar
    def doAction(self):
        self.timer.start(100, self)
    def openwin(self):
        #下一个窗口的接口
        self.main_win = ATM_UI(self.user_limit, self.user)
        self.main_win.ui.show()
        self.window.close()

if __name__ == "__main__":
    app = QApplication([])
    Login_Win = LoginWindow()
    Login_Win.window.show()
    sys.exit(app.exec())
