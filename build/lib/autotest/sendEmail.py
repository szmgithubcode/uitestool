#!/usr/bin/python
# -*- coding=UTF-8 -*-

import os
import sys
import time
import smtplib

sys.path.append("../..")
sys.path.append("..")
from email import encoders
from com.readConfig import ReadConfig
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase


def find_report():
    currentdir = os.path.split(os.path.realpath(__file__))[0]
    result_dir = os.path.abspath(os.path.join(currentdir, os.pardir)) + '\\result\\report\\'
    result_lists = os.listdir(result_dir)
    result_lists.sort(
        key = lambda fn: os.path.getmtime(result_dir + "\\" + fn) if not os.path.isdir(result_dir + "\\" + fn) else 0)
    # 找到最新生成的文件
    file_new = os.path.join(result_dir, result_lists[-1])
    file_name = str(result_lists[-1])
    return file_new, file_name


def attach_file(msgRoot, file_new, file_name):
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(file_new, 'rb').read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file_name))
    msgRoot.attach(part)


def send_mail():
    """发送测试报告"""
    report_new = find_report()[0]
    report_name = find_report()[1]
    # screen_new = find_screen_zip()[0]
    # screen_name = find_screen_zip()[1]
    mail_from = 'iman@hupu.net'  # 邮箱帐号
    # mail_to=readfile.get_title("MailReceiver")
    # mail_to=[receiver for receiver in readfile.get_title("MailReceiver")]
    # mail_to=['szmingemail@163.com','254901517@qq.com']
    rc = ReadConfig()
    mail_to = [receiver for receiver in rc.get_mail_recipient()]
    file_report = open(report_new, 'rb')
    mail_body = file_report.read()
    file_report.close()
    msgRoot = MIMEMultipart('related')
    # timec = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    # msgRoot['Subject'] = u"automation test report " + timec
    msgRoot['Subject'] = u"自动化测试报告"
    msgRoot['From'] = 'test' + '<' + str(mail_from) + '>'
    msgRoot['To'] = str(mail_to)
    # msgText = MIMEText(mail_body, _subtype = 'html', _charset = 'utf-8')
    msgText = MIMEText("用例执行情况见附件【result.html】", _subtype = 'html', _charset = 'utf-8')
    msgRoot['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    msgRoot.attach(msgText)
    attach_file(msgRoot, report_new, report_name)
    # attach_file(msgRoot, screen_new, screen_name)
    try:
        smtp = smtplib.SMTP()
        smtp.connect('smtp.hupu.net')  # 邮箱服务器
        smtp.login('iman@hupu.net', 'iman2015@hupu.net')  # 邮箱帐号和密码
        smtp.sendmail(mail_from, mail_to, msgRoot.as_string())
        print("send e-mail to success")
        smtp.close()
    except Exception as e:
        print(e)
        sys.exit(1)
