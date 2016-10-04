1.视频和文档  ===>  3个小项目


2.时间

10.1-----准备阶段.
	1.搭建环境. 
		1.db问题
			1.sqlite3不是内部命令
				在http://www.sqlite.org/download.html页面下载，
				sqlite-tools-win32-x86-3140200.zip并解压，
				添加至环境变量. (必须知道sqlite3.exe)

		2.测试第一个app

			1.创建app并添加到settings.py中.
				a.python manage.py startapp learn
				b.修改mysite/mysite/settings.py 中的INSTALLED_APPS

			django 就能自动找到app中的模板件
			(appname/templates/下的文件)和
			静态⽂件(app-name/static/中的文件)

			2.定义视图函数并添加到项目中个urls.py中	

				a.learn这个录中,把views.py
					实现处理函数.  打开进入learn项目的处理函数。


				b.让网址和函数关联

				修改mysite/mysite/urls.py中的urlpatterns定义了映射关系.
				url(r'^learn/$', 'learn.views.index', name='home'),
				测试:	
				http://127.0.0.1:8000/learn/


	2.下载视频.
	3.搬家

10.2 完成第一个

10.3  打印出来django两份资料

10.4  完成项目

10.5  总结.

10.6  去北大完.


1.路由 
	
===================================
http://www.ziqiangxuetang.com/django/
01.Django 基础教程
02.Django 简介
03.Django 环境搭建
04.Django 基本命令
05.Django 视图与网址
06.Django 视图与网址进阶
07.Django URL name 详解.
08.Django 模板
09.Django 模板进阶
10.Django 模型(数据库)
11.Django 自定义Filed
12.Django 数据表更改
13.Django QuerySetAPI
14.Django 后台
15.Django 表单
16.Django 配置
17.Django 静态文件
18.Django 部署(Apache)
19.Django 部署(Nginx)
20.Django 发送邮件

Django中级教程

21.Django 数据导入
22.Django 数据迁移
23.Django 多数据库联用
24.Django 用户注册系统
25.Django 缓存系统
26.Django 生成静态网页
27.Django 安全
28.Django 国际化
29.Django session
30.Django 传递数据给js
31.Django Ajax
32.Django Ajax CSRF认证
33.Django Sitemap 站点地图
34.Django 只用Django数据库
35.Django 通用视图
36.Django 上下文管理器
37.Django 中间件
39.Django 微信接口
40.Django 单元测试

Django 项目实战
1.开发内容管理系统
2.其他(书中写)

Django 应用分享

1.Django CMS
2.Python/Django 二维码.