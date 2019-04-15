from setuptools import find_packages, setup
setup(
    name='guacapyClientRest',
    version='0.0.1',
    description='Python REST API client for Guacamole 0.9.13 version',
    author='author',#作者
    author_email='xxxxxxxx@163.com',
    url='https://github.com/xxxxx',
    #packages=find_packages(),
    packages=['guacapyClientRest'],  #这里是所有代码所在的文件夹名称
    install_requires=['requests'],
)