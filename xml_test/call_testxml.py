# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog
from testxml import Ui_MainWindow
import os,csv
from xml.dom import minidom
import time
class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        # 菜单的点击事件，当点击关闭菜单时连接槽函数 close()
        #self.fileCloseAction.triggered.connect(self.close)
        # 菜单的点击事件，当点击打开菜单时连接槽函数 openMsg()
        #self.fileOpenAction.triggered.connect(self.openMsg)
        self.pushButton.clicked.connect(self.openMsg)
        self.pushButton_2.clicked.connect(self.getxml)
    def openMsg(self):
        global directory1
        m = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        s = '2019-12-31 00:00:00'
        if m < s:
            directory1 = QFileDialog.getExistingDirectory(self,
                                                          "选取文件夹",
                                                          "./")  # 起始路径
            # 在状态栏显示文件地址
            self.statusbar.showMessage(directory1)
        else:
            self.statusbar.showMessage("软件已过期，请与作者联系！", 10000)


    def getxml(self):
        try:

            work_dir = directory1
            w_dir = ''.join(list(directory1)[0:2])
            with open(w_dir+'/xml_result.csv', 'a', newline='') as f1:
                writer = csv.writer(f1)
                writer.writerow(("MR任务名称", "EnodeB名称", "EnodeBID", "productSpec", "最大UE数","cellID"))
            for parent, dirnames, filenames in os.walk(work_dir, followlinks=True):
                for filename in filenames:
                    filetype = os.path.splitext(filename)
                    filename1, type = filetype
                    if type =='.xml':
                        file_path = os.path.join(parent, filename)
                        # 使用minidom解析器打开 XML 文档
                        with open(file_path, 'r', encoding='GBK') as fh:
                            dom = minidom.parse(fh)
                            # 加载dom对象元素
                            root = dom.documentElement  # root存储根节点元素的相关属性
                            enodeBs = root.getElementsByTagName('enodeB')
                            for enb in enodeBs:
                                MR_name = root.getAttribute('name')
                                enbname = enb.getAttribute('managedElementType')
                                meid=enb.getAttribute('sdrMeID')
                                ueMaxNum = root.getElementsByTagName('ueMaxNum')[0]
                                #enbids = enb.getElementsByTagName('EnodeBID')

                                #enb1 = enbids[0].getAttribute('eNodeBId')
                                ueMaxNum_data = ueMaxNum.childNodes[0]
                                #enbids = enb.getElementsByTagName('EnodeBID')

                                cellss = enb.getElementsByTagName('cell')
                                for cell in cellss:
                                    mycell = cell.getAttribute('cellID')
                                    MyproductSpec = cell.getAttribute('productSpec')
                                #print(MR_name, enbname, enbid, ueMaxNum_data.data)
                                    with open(w_dir+'/xml_result.csv', 'a', newline='') as f:
                                        writer = csv.writer(f)
                                        writer.writerow((MR_name, enbname, meid, MyproductSpec, ueMaxNum_data.data,mycell))
                        fh.close()
                        # 在状态栏显示文件地址
            self.statusbar.showMessage("结果保存在："+w_dir+"/xml_result.csv")
        except Exception as err:
            self.statusbar.showMessage("请选择xml文件所在文件夹")
            return

app = QApplication(sys.argv)
win = MainForm()
win.show()
sys.exit(app.exec_())
