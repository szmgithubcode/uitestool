# coding=utf-8

from com.readConfig import ReadConfig
from appium import webdriver

rc = ReadConfig()
desired_caps = rc.get_desired_caps("DesiredCaps")
remote_url = rc.get_romote_url()
driver = webdriver.Remote(remote_url, desired_caps)


