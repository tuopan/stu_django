#coding:utf-8
from wsgiref.simple_server import  make_server
import config

def Runserver(environ, start_response):
    #BaseHandler.start_response 基类中实现
    start_response('200 OK',[('Content-type','text/html')] )
    userURL = environ['PATH_INFO']

    print('-'*20)
    print(userURL)
    return '<h1>hello work</h1>'


def main():
    httpd = make_server('',8000, Runserver)
    print'serving http on Runserver:',Runserver
    httpd.serve_forever()

if __name__ == '__main__':
    main()