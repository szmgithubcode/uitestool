from setuptools import find_packages, setup
setup(
    name='autotest',
    version='0.0.1',
    description='autotest',
    author='szmgithubcode',#作者
    author_email='13023297816@163.com',
    url='https://github.com/szmgithubcode/uitestool/',
    #packages=find_packages(),
    packages=['autotest'],  #这里是所有代码所在的文件夹名称
    install_requires=['requests'],
)