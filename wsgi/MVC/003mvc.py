#coding:utf-8
from wsgiref.simple_server import make_server
from Controller.Account import url

def Runserver(environ, start_response):
    #BaseHandler.start_response 基类中实现
    start_response('200 OK',[('Content-type','text/html')] )
    userURL = environ['PATH_INFO']
    func = None
    for item in url:
        if item[0] == userURL:#遍历url中映射的url
           func = item[1]
           break
    #如果没有找到
    if func:
        result = func()
    else:
        result = '404 error'
    return result

def main():
    httpd = make_server('',8008, Runserver)
    print'serving http on Runserver:',Runserver
    httpd.serve_forever()

if __name__ == '__main__':
    main()