hello kali!
issue-101----modify bug.

#多人协作
    查看远程库信息，使用git remote -v；

    本地新建的分支如果不推送到远程，对其他人就是不可见的；

    从本地推送分支，使用git push origin branch-name，如果推送失败，先用git pull抓取远程的新提交；

    在本地创建和远程分支对应的分支，使用git checkout -b branch-name origin/branch-name，本地和远程分支的名称最好一致；

    建立本地分支和远程分支的关联，使用git branch --set-upstream branch-name origin/branch-name；

    从远程抓取分支，使用git pull，如果有冲突，要先处理冲突。
#PyQt5程序打包
安装打包程序：pip install pyinstaller
打包程序命令：pyinstaller.exe -F -i D:\个人照片\icon\2019021810170129_easyicon_net_32.ico -w D:\ProgramData\PycharmProjects\pyqt\csvhebing.py
	       pyinstaller.exe -F -i D:\个人照片\icon\2019021810170129_easyicon_net_32.ico -w D:\ProgramData\PycharmProjects\pyqt\call_testxml.py
程序生成路径：C:\Windows\system32\dist\call_testxml.exe

pyinstaller常用参数说明：
–icon=图标路径
-F 打包成一个exe文件
-w 使用窗口，无控制台
-c 使用控制台，无窗口
-D 创建一个目录，里面包含exe以及其他一些依赖性文件
pyinstaller -h 来查看参数
