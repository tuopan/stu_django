# coding:utf-8
# 所有账户相关的都放到这里

def index():
    return 'index'

def login():
    # 从View读取login.html 返回data
    f = file('View/login.html', 'r')
    print f
    data = f.read()
    f.close()
    return data


def mange():
    return 'manage'


def error_404():
    return '404 not find'

url = {
    ('/', index),
    ('/index/', index),
    ('/login/', login),
    ('/mange/', mange),
    ('/404/', error_404),
}
