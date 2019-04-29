import os
from configparser import ConfigParser

current_dir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.abspath(os.path.join(current_dir,os.pardir))+ '\\config.ini'


class MyConfigparser(ConfigParser):
    def __init__(self,defaults=None):
        ConfigParser.__init__(self,defaults=None)

    #optionxform函数自动转换为小写字母，所以需要对optionxform函数进行重写
    def optionxform(self, optionstr):
        return optionstr


class ReadConfig(object):
    def __init__(self):
        self.cf = MyConfigparser()
        self.cf.read(configPath)

    def get_database(self, name):
        return self.cf.get("DATABASE", name)

    def get_mail_recipient(self):
        for item in self.cf.items("MailReceiver"):
            recipient=self.cf.get("MailReceiver",item[0])
            yield recipient

    def get_baseurl(self):
        return self.cf.get("ServerUrl","baseUrl")

    def get_header(self,section):
        my_dict={}
        #根据section把key、value写入字典
        for key_name, value in self.cf.items(section):
            my_dict[key_name] = value
        return my_dict

    def get_desired_caps(self,section):
        my_dict={}
        #根据section把key、value写入字典
        for key_name, value in self.cf.items(section):
            my_dict[key_name] = value
        return my_dict

    def get_romote_url(self):
        return self.cf.get("RomoteURL","remoteUrl")


# rc=ReadConfig()
# print(rc.get_database("host"))
# print([receiver for receiver in rc.get_mail_recipient()])
# print(rc.get_desired_caps("DesiredCaps"))