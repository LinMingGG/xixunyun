import requests
import json
import os

# 配置开始
user = os.environ["USER"]
account = user.split( )[0] # 账号
password = user.split( )[1] # 密码
school_id = user.split( )[2] # 学校ID
sign_gps = os.environ["SIGN_GPS"]  # 签到坐标（注意小数点取后6位）
longitude = sign_gps.split(",")[0] # 经度
latitude = sign_gps.split(",")[1] # 纬度
data = {
  "account":account,
  "password":password,
  "school_id":school_id,
  "longitude":longitude,
  "latitude":latitude,
  "address_name":os.environ["ADDRESS_NAME"] 
}
headers = {'Content-Type': 'application/json'}

response = requests.post(url='http://xxy.kuileii.cn/release/xixunyun', headers=headers, data=json.dumps(data))
print(response.json())
wdnmd=response.json()
print(wdnmd)

SCKEY=os.environ["SCKEY"]
if len(SCKEY) >= 1:
  url = 'https://sc.ftqq.com/'+SCKEY+'.send'
  requests.post(url, data={"text": "习讯云签到提醒", "desp": response.json()})

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
fromaddrs = '\u0031\u0038\u0033\u0030\u0036\u0030\u0039\u0032\u0035\u0032\u0033\u0040\u0031\u0036\u0033\u002e\u0063\u006f\u006d'
password2 = '\u0045\u0059\u0049\u0050\u0042\u004e\u0056\u004f\u0054\u004b\u0045\u004b\u0050\u0059\u0042\u0053'  
toaddrs = os.environ["EMAIL"]
def mail():
    ret = True
    try:
        msg = MIMEText(wdnmd, 'plain', 'utf-8')
        msg['From'] = formataddr(["习讯云签到提醒", fromaddrs])  # 发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["习讯云自动签到程序", toaddrs])  # 收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "习讯云自动签到提醒"  # 邮件的主题

        server = smtplib.SMTP_SSL("smtp.163.com",)  # qq邮箱SMTP服务器，端口是25
        server.login(fromaddrs, password2)  # 发件人邮箱账号、邮箱密码
        server.sendmail(fromaddrs, [toaddrs, ], msg.as_string())  # 发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        #ret = False
    #return ret
#ret = mail()
#if ret:
  # print("邮件发送成功")
#else:
    #print("邮件发送失败")
