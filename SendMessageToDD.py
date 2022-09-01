# -*- coding: utf-8 -*-
import json
import urllib.request
from configparser import ConfigParser

class SEND_MSG():
    def __init__(self):
        configparser2 = ConfigParser()
        configparser2.read('./conf/conf.ini')
        read_content = configparser2.items('ddurl')
        self.my_url = read_content[0][1]
    # 获取消息发送
    def send_MSG(self, writing, *tel):
        my_data = {
            "msgtype": "text",
            "text": {"content": ""},
            "at": {"atMobiles": [""],
                   "isAtAll": False}}
        #my_url = "https://oapi.dingtalk.com/robot/send?access_token=a3daa76de84710e0336458f548ade2ea615aebd8202c5819feda3d704b859eb1"
        # 把文案内容写入请求格式中
        my_data["text"]["content"] = writing
        my_data["at"]["atMobiles"] = tel
        self.send_request(self.my_url, my_data)
    # 发送钉钉消息
    def send_request(self, url, datas):
        header = {"Content-Type": "application/json",
                  "Charset": "UTF-8"}
        sendData = json.dumps(datas)  # 将字典类型数据转化为json格式
        sendDatas = sendData.encode("utf-8")  # python3的Request要求data为byte类型
        # 发送请求
        request = urllib.request.Request(url=url, data=sendDatas, headers=header)
        # 将请求发回的数据构建成为文件格式
        opener = urllib.request.urlopen(request)
        # 7、打印返回的结果
        print(opener.read())





if __name__ == "__main__":
    sendmsg = SEND_MSG()
    sendmsg.send_MSG('要发送的任务2','13950880026','15659371527')