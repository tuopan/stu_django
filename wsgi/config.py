#coding:utf-8
def index():
    return 'index'

def login():
    return 'login'

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


