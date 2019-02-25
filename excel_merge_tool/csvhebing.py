#!/usr/bin/env python
# _*_coding:utf-8 _*_
import os,sys
# import glob,csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from testcsv import Ui_MainWindow
import pandas as pd
import time
class MainForm(QMainWindow, Ui_MainWindow):
    global x
    global all_files
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.openFiles)
        self.pushButton_2.clicked.connect(self.getcsv)
        # 菜单的点击事件，当点击关闭菜单时连接槽函数 close()
        #self.fileCloseAction.triggered.connect(self.close)
        # 菜单的点击事件，当点击打开菜单时连接槽函数 openMsg()
        #self.fileOpenAction.triggered.connect(self.openMsg)
    def openMsg(self):
        global directory1
        directory1 = QFileDialog.getExistingDirectory(self,"选取文件夹","./")# 起始路径
        # 在状态栏显示文件地址
        self.statusbar.showMessage(directory1)
    def openFiles(self):
        global all_files
        m = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        s = '2019-12-31 00:00:00'
        if m < s:
            all_files, ok1 = QFileDialog.getOpenFileNames(self, "多文件选择", "/", "所有文件 (*);;表格文件 (*.csv)")
            # all_files= files
            if all_files:
                self.statusbar.showMessage(all_files[0])
        else:
            self.statusbar.showMessage("软件已过期，请与作者联系！", 10000)


    def openXFiles(self):
        global all_files
        files, ok1 = QFileDialog.getOpenFileNames(self, "多文件选择", "/", "表格文件 (*.xlsx)")
        all_files= files

        self.statusbar.showMessage(all_files[0])
    def getcsv(self):
        global all_files
        try:
            w_dir = ''.join(list(all_files[0])[0:2])
            #w_dir = ''.join(list(directory1)[0:2])
            #input_path = directory1.replace("/","\\")
            output_file = w_dir + '/csv_result.csv'
            #all_files = glob.glob(os.path.join(input_path, '*.csv'))
            all_data_frame = []
            for file in all_files:
                filetype = os.path.splitext(file)
                filename, type = filetype

                if type =='.csv':
                    try:
                        data_frame = pd.read_csv(file, encoding='gbk')
                    except Exception as err:
                        pass
                    try:
                         data_frame = pd.read_csv(file, encoding='utf_8_sig')
                    except Exception as err:
                        pass
                elif type =='.xlsx':
                    try:
                        data_frame = pd.read_excel(file)

                    except Exception as err:
                        pass
                elif type == '.xls':
                    try:
                        data_frame = pd.read_excel(file)

                    except Exception as err:
                        pass
                else:
                    self.statusbar.showMessage("请选择表格文件")
                    return
                    # try:
                    #     data_frame = pd.read_excel(file, encoding='gbk')
                    # except Exception as err:
                    #     pass
                all_data_frame.append(data_frame)
            # pandas.concat()函数将数据框数据垂直堆叠(axis=0), 当水平连接数据时(asis=1)
            data_frame_concat = pd.concat(all_data_frame, axis=0, ignore_index=True)
            data_frame_concat.to_csv(output_file,encoding='utf_8_sig', index=False)
            self.statusbar.showMessage("结果保存在：" + w_dir + "/csv_result.csv")
        except Exception as err:
            self.statusbar.showMessage("请选择表格文件")
            return
    def getxls(self):
        global all_files
        w_dir = ''.join(list(all_files[0])[0:2])
        output_file = w_dir + '/csv_result.csv'
        all_data_frame = []
        for file in all_files:
         try:
             data_frame = pd.read_xlsx(file, encoding='gbk')
         except Exception as err:
             pass
         try:
             data_frame = pd.read_xlsx(file, encoding='utf_8_sig')
         except Exception as err:
             pass
         all_data_frame.append(data_frame)
        # pandas.concat()函数将数据框数据垂直堆叠(axis=0), 当水平连接数据时(asis=1)
        data_frame_concat = pd.concat(all_data_frame, axis=0, ignore_index=True)
        data_frame_concat.to_csv(output_file, encoding='utf_8_sig', index=False)
        self.statusbar.showMessage("结果保存在：" + w_dir + "/csv_result.csv")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())