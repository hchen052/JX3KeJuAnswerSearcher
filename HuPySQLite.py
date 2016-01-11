# -*- coding:utf-8 -*-
# Author : huchen
# MailTo : hchen052@gmail.com
# QQ     :
# Blog   : 
# Create : 2015-08-13
# Version: 1.0
#
# DB-API 2.0 interface for SQLite databases 

import sqlite3
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

DEBUG = False

            
def get_conn(path):
    '''
    方法： 获取到数据库的连接对象
    参数： Path  --   数据库文件的绝对路径
    返回： 当Path为空或不是文件，则返回内存中的数据连接对象
           否则返回硬盘上面该Path下的数据库文件的连接对象
    '''
    conn = sqlite3.connect(unicode(path, 'cp936', 'ignore').encode('utf-8'))
    if os.path.exists(path) and os.path.isfile(path):
        conn.text_factory = str
        return conn
    else:
        conn = sqlite3.connect(':memory:')
        conn.text_factory = str
        return conn
          
        
def get_cursor(conn):
    '''
    方法： 获取数据库的游标对象
    参数： conn  --  数据库的连接对象
    返回： 当conn不为None，则返回该数据库连接对象所创建的游标对象
           否则返回一个内存中数据库连接对象所创建的游标对象
    '''
    if conn is not None:
        return conn.cursor()
    else:
        return get_conn('').cursor()


# 删除表操作
def drop_table(conn, table):
    '''
    方法：  删除数据库中的表
    参数：  conn  --  数据库的连接对象
            table  --  删除的表名称。如果表中存在数据时候，慎用！
    返回：  None
    '''
    if table is not None and table != '':
        sql = 'DROP TABLE IF EXISTS ' + table
        cu = get_cursor(conn)
        if DEBUG:
            print('执行sql:[{}]'.format(sql))
        cu.execute(sql)
        conn.commit()
        print('删除数据库表[{}]成功!'.format(table))
        close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))

  
# 创建表  
def create_table(conn, table, key_infos):
    '''
    方法：  创建数据库表
    参数：  conn  --  数据库的连接对象
            table  --  创建的数据库表的名称
            key_infos  --  创建的表的key描述信息
    返回：  None
    '''
    sql = 'CREATE TABLE %s %s' %(table, key_infos)
    #print sql
    cu = get_cursor(conn)
    if DEBUG:
        print('执行sql:[{}],参数:[{}]'.format(sql, key_infos))
    cu.execute(sql)
    conn.commit()
    print('创建数据库表%s成功!'%table)
    close_all(conn, cu)


def close_all(conn, cu):
    '''
    方法：  关闭数据库游标对象和数据库连接对象
    参数：  conn  --  数据库的连接对象
            cu  --  数据库的游标对象
    返回：  None
    '''
    try:
        if cu is not None:
            cu.close()
    finally:
        if conn is not None:
            conn.close()
            

def EchoTuple(number):
    str = ', '.join(['?' for i in range(0, number)])
    return '(%s)' %str
            
            
###############################################################
####            数据库操作API     START
###############################################################
def save(conn, table, data):
    '''
    方法：  插入数据
    参数：  conn  --  数据库的连接对象
            table  --  数据库表的名称
            data   --  插入的数据，可以是多条数据，也可以是单条数据。
    返回：  None
    '''
    cu = get_cursor(conn)
    if isinstance(data, list):
        for d in data:
            sql = 'INSERT INTO %s values %s' %(table, EchoTuple(len(d)))
            if DEBUG:
                print('执行sql:[{}],参数:[{}]'.format(sql, d))
            cu.execute(sql, d)
            conn.commit()
    else:
        sql = 'INSERT INFO %s values %s' %(table, EchoTuple(len(d)))
        if DEBUG:
            print('执行sql:[{}],参数:[{}]'.format(sql, d))
        cu.execute(sql, d)
        conn.commit()
    close_all(conn, cu)
    
    
def fetchdata(conn, sql):
    '''
    方法：  查询所有数据
    参数：  conn  --  数据库的连接对象
            sql  --  查询命令
    返回：  获取的所有数据 or None
    '''
    if sql is None or sql == '':
        print('the [{}] is empty or equal None!'.format(sql))
        return None
    cu = get_cursor(conn)
    if DEBUG:
        print('执行sql:[{}]'.format(sql))
    cu.execute(sql)
    return cu.fetchall()


def update(conn, sql, data):
    '''更新数据'''
    if sql is not None and sql != '':
        if data is not None:
            cu = get_cursor(conn)
            for d in data:
                if DEBUG:
                    print('执行sql:[{}],参数:[{}]'.format(sql, d))
                cu.execute(sql, d)
                conn.commit()
            close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))

        
def delete(conn, sql, data):
    '''删除数据'''
    if sql is not None and sql != '':
        if data is not None:
            cu = get_cursor(conn)
            for d in data:
                if DEBUG:
                    print('执行sql:[{}],参数:[{}]'.format(sql, d))
                cu.execute(sql, d)
                conn.commit()
            close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))
###############################################################
####            数据库操作CRUD     END
###############################################################            
        
        
###############################################################
####            测试操作     START
###############################################################
def drop_table_test():
    '''删除数据库表测试'''
    print('删除数据库表测试...')
    conn = get_conn(DB_FILE_PATH)
    drop_table(conn, TABLE_NAME)

def create_table_test():
    '''创建数据库表测试'''
    print('创建数据库表测试...')
    #create_table_sql = '''CREATE TABLE `student` (
    #                      `id` int(11) NOT NULL,
    #                      `name` varchar(20) NOT NULL,
    #                      `gender` varchar(4) DEFAULT NULL,
    #                      `age` int(11) DEFAULT NULL,
    #                      `address` varchar(200) DEFAULT NULL,
    #                      `phone` varchar(20) DEFAULT NULL,
    #                       PRIMARY KEY (`id`)
    #                    )'''
    table = 'student'
    key_infos = '''(`id` int(11) NOT NULL,
                    `name` varchar(20) NOT NULL,
                    `gender` varchar(4) DEFAULT NULL,
                    `age` int(11) DEFAULT NULL,
                    `address` varchar(200) DEFAULT NULL,
                    `phone` varchar(20) DEFAULT NULL,
                     PRIMARY KEY (`id`))'''
    conn = get_conn(DB_FILE_PATH)
    create_table(conn, table, key_infos)

def save_test():
    '''保存数据测试...'''
    print('保存数据测试...')
    #save_sql = '''INSERT INTO student values (?, ?, ?, ?, ?, ?)'''
    table = 'student'
    data = [(1, 'Hongten', '男', 20, '广东省广州市', '13423****62'),
            (2, 'Tom', '男', 22, '美国旧金山', '15423****63'),
            (3, 'Jake', '女', 18, '广东省广州市', '18823****87'),
            (4, 'Cate', '女', 21, '广东省广州市', '14323****32')]
    conn = get_conn(DB_FILE_PATH)
    save(conn, table, data)

def fetchall_test():
    '''查询所有数据...'''
    print('查询所有数据...')
    fetchall_sql = '''SELECT * FROM student'''
    conn = get_conn(DB_FILE_PATH)
    data = fetchdata(conn, fetchall_sql)
    for e in range(len(data)):
        print(data[e])
    
def fetchone_test():
    '''查询一条数据...'''
    print('查询一条数据...')
    fetchone_sql = 'SELECT * FROM student WHERE ID = 1 '
    conn = get_conn(DB_FILE_PATH)
    data = fetchdata(conn, fetchone_sql)
    for  e in range(len(data)):
        print(data[e])

def update_test():
    '''更新数据...'''
    print('更新数据...')
    update_sql = 'UPDATE student SET name = ? WHERE ID = ? '
    data = [('HongtenAA', 1),
            ('HongtenBB', 2),
            ('HongtenCC', 3),
            ('HongtenDD', 4)]
    conn = get_conn(DB_FILE_PATH)
    update(conn, update_sql, data)

def delete_test():
    '''删除数据...'''
    print('删除数据...')
    delete_sql = 'DELETE FROM student WHERE NAME = ? AND ID = ? '
    data = [('HongtenAA', 1),
            ('HongtenCC', 3)]
    conn = get_conn(DB_FILE_PATH)
    delete(conn, delete_sql, data)

###############################################################
####            测试操作     END
###############################################################

def init():
    '''初始化方法'''
    #数据库文件绝句路径
    global DB_FILE_PATH
    wkdir = os.getcwd()
    DB_FILE_PATH = os.path.join(wkdir, 'test.db')
    #数据库表名称
    global TABLE_NAME
    TABLE_NAME = 'student'
    #是否打印sql
    global DEBUG
    DEBUG = True
    print('DEBUG : {}'.format(DEBUG))
    #如果存在数据库表，则删除表
    drop_table_test()
    #创建数据库表student
    create_table_test()
    #向数据库表中插入数据
    save_test()
    

def main():
    init()
    fetchall_test()
    print('#' * 50)
    fetchone_test()
    print('#' * 50)
    update_test()
    fetchall_test()
    print('#' * 50)
    delete_test()
    fetchall_test()

if __name__ == '__main__':
    main()        
