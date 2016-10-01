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