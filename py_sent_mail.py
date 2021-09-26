#!/usr/bin/env python
# coding=utf-8

import sys
import smtplib
from email.mime.text import MIMEText

def send(mail_info_dic):
  #设置服务器所需信息
  #163邮箱服务器地址
  mail_host = 'smtp.163.com'
  #163用户名
  mail_user = 'your_email_name'
  #密码(部分邮箱为授权码)
  mail_pass = 'your_email_password'
  #邮件发送方邮箱地址
  sender = 'your_email_name@163.com'
  #邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
  to_receivers = mail_info_dic['receivers'].split(",")
  cc_receivers = mail_info_dic['Cc'].split(",") if 'Cc' in mail_info_dic else []
  all_receivers = to_receivers + cc_receivers

  #设置email信息
  #邮件内容设置
  message = MIMEText(mail_info_dic["content"],'plain','utf-8')
  #邮件主题
  message['Subject'] = mail_info_dic["title"]
  #发送方信息
  message['From'] = sender
  #接受方信息
  message['To'] = ";".join(to_receivers)
  message['Cc'] = ";".join(cc_receivers)

  #登录并发送邮件
  try:
    smtpObj = smtplib.SMTP()
    #连接到服务器
    smtpObj.connect(mail_host)
    #登录到服务器
    smtpObj.login(mail_user,mail_pass)
    #发送
    smtpObj.sendmail(sender,all_receivers,message.as_string())
    #退出
    smtpObj.quit()
    print('success')
  except smtplib.SMTPException as e:
    print('error',e) #打印错误

def parser_args(argv, mail_info_dic):
  '''
  echo ${model_data}"/*_38" | mail -s "dssm-video: No fm_feature model data" zhanghua1@corp.netease.com
  python mail.py -s "mail title" receiver1@163.com,receiver2@163.com -c Cc1@163.com,Cc2@163.com -cont "email-content"
  '''
  #mail_info_dic  #title、content、reciver、Cc
  argv_len = len(argv)
  #for i in range(argv_len-1):
  i = 0
  while i <= (argv_len-1):
    flag = argv[i].strip()
    info = ""
    if i < (argv_len-1):
      info = argv[i+1].strip()
    if flag == "-s" and info != "":
      mail_info_dic["title"] = info
      i += 2
    elif flag == "-c" and info != "":
      mail_info_dic["Cc"] = info
      i += 2
    else:
      mail_info_dic["receivers"] = flag
      i += 1
  if ("title" in mail_info_dic) and ("content" in mail_info_dic) and ("receivers" in mail_info_dic):
    return True
  else:
    print ("Error: argv Error!")
    print ('mail -s "mail title" -c Cc1@163.com,Cc2@163.com  receiver1@163.com,receiver2@163.com')
    return False

def achieve_cont_from_stdin(mail_info_dic):
  content = ""
  for line in sys.stdin:
    if line != "":
      content += line
  if content != "":
    mail_info_dic["content"] = content
    return True
  else:
    print ("Error: no content!")
    return False

if __name__ == '__main__':
  mail_info_dic = {}
  if achieve_cont_from_stdin(mail_info_dic):
    if parser_args(sys.argv, mail_info_dic):
      send(mail_info_dic)
  else:
    sys.exit(1)
