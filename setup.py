#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
# Author : Hu Chen
# MailTo : hchen052@gmail.com
# QQ     :
# Blog   :
# Github : https://github.com/hchen052/JX3KeJuAnswerSearcher
# Create : 2015-08-13
# Version: 1.0
#
# py2exe setup config

from distutils.core import setup
import py2exe

from glob import glob

# 定义需要包含进工程的文件.
data_files = [("Microsoft.VC90.CRT",
               glob('Microsoft.VC90.CRT\*.*')),
              (".\\", glob("JX3KeJuTiKu.db"))]

# 环境相关，具体可参见py2exe首页.
includes = ["encodings", "encodings.*"]   

# 编译选项.
options = {"py2exe":{"includes":["sip"]}}

# 编译规则.
setup(
    version='0.1.1',
    description=u"剑网3科举答案查询器",
    name=u"剑网叁科举查询器",
    data_files=data_files,
    options=options,
    zipfile=None,
    #windows=[{"script":'jx3kejusearcher.py'}])
    windows=[{"script": 'jx3kejusearcher.py', "icon_resources": [(1, r"icons\pp.ico")]}])
