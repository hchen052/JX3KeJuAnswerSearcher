# -*- coding:utf-8 -*-
# Author : huchen
# MailTo : harold86@126.com
# QQ     :
# Blog   : 
# Create : 2015-08-13
# Version: 1.0
  
# 剑网3科举考试答案查询器
# 目前题目数量为1588条

import re
import sys
import os
from pypinyin import lazy_pinyin
import codecs
import HuPySQLite


# 数据库的绝对路径
DB_FILE_PATH = ''
# 数据库名称
DB_FILE_NAME = 'JX3KeJuTiKu.db'
# 表名称
DB_TABLE_NAME = 'jx3keju'
# 科举答案导入文件(txt格式)
# q: _________，众妙之门。  a: 玄之又玄
KEJU_TXT = 'JX3KeJuDaAn_All.txt'

# 重新编码字符.
#
# 将字符串strw从utf-8编码转换成ENCODE_TYPE编码.
def recode(strw):
    import platform
    sysstr = platform.system()
    if sysstr.lower() == 'windows':
        ENCODE_TYPE = sys.getfilesystemencoding()
        return strw.decode('utf-8').encode(ENCODE_TYPE)
    else:
        return strw


def SearchQuestionByPinyin(pinyin):
    """
    方法：  通过拼音的方式来搜索题目，并打印答案。
    参数：  pinyin  :  题目的首字母
    返回：  data  ：  所有符合规则的题目及答案    
    """
    global DB_FILE_PATH
    global DB_FILE_NAME
    global DB_TABLE_NAME
    if DB_FILE_PATH == '':
        DB_FILE_PATH = os.getcwd()
    db_file = os.path.join(DB_FILE_PATH, DB_FILE_NAME)
    cx = HuPySQLite.get_conn(db_file)
    cu = cx.cursor()
    sql = '''select question, answer from %s where que_pinyin glob "*%s*"'''%(DB_TABLE_NAME, pinyin)
    cu.execute(sql)
    data = cu.fetchall()
    cu.close()
    cx.close()
    return data
    
    
def SearchMain(pinyin):
    rtstr = ''
    pinyin = str(pinyin)
    data = SearchQuestionByPinyin(pinyin.lower())
    if len(data) == 0:
        rtstr += u'%>_<%没找到你的题目，请重试！\n'
    else:
        i = 0
        for value in data:
            q = value[0]
            a = value[1]
            i += 1
            rtstr += u'%2d. %s\n' %(i, q)
            rtstr += u'    答案：%s\n' %a
    return rtstr    
    
    
if __name__ == '__main__':
    SearchMain()
