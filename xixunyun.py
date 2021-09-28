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

SCKEY=os.environ["SCKEY"]
if len(SCKEY) >= 1:
  url = 'https://sc.ftqq.com/'+SCKEY+'.send'
  requests.post(url, data={"text": "习讯云签到提醒", "desp": response.json()})

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
fromaddrs = '1036933769@qq.com'
password2 = 'szxnazldaowdbead'  
toaddrs = os.environ["EMAIL"]
def mail():
    ret = True
    try:
        msg = MIMEText(sign_request.text, 'plain', 'utf-8')
        msg['From'] = formataddr(["习讯云签到提醒", fromaddrs])  # 发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["习讯云自动签到程序", toaddrs])  # 收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "习讯云自动签到提醒"  # 邮件的主题

        server = smtplib.SMTP_SSL("smtp.qq.com",port=465)  # qq邮箱SMTP服务器，端口是25
        server.login(fromaddrs, password2)  # 发件人邮箱账号、邮箱密码
        server.sendmail(fromaddrs, [toaddrs, ], msg.as_string())  # 发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret
ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")
