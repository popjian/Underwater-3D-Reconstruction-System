from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 500)
        MainWindow.setMinimumSize(QtCore.QSize(900, 500))
        MainWindow.setMaximumSize(QtCore.QSize(900, 500))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(120, 20, 561, 401))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.horizontalLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.table_widget = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.table_widget.setFixedWidth(500)  # 或使用 setMinimumWidth(300)
        self.table_widget.setRowCount(6)  # 设置行数
        self.table_widget.setColumnCount(2)  # 设置列数
        self.table_widget.horizontalHeader().setVisible(False)  # 隐藏水平表头
        self.table_widget.verticalHeader().setVisible(False)  # 隐藏垂直表头
        # 设置QTableWidget的高度
        self.table_widget.setFixedHeight(500)  # 或使用 setMinimumHeight(200)
        self.table_widget.setColumnWidth(0, 250)  # 设置第一列的宽度为150像素
        self.table_widget.setColumnWidth(1, 250)  # 设置第二列的宽度为100像素
        self.table_widget.setObjectName("table_widget")
        self.horizontalLayout.addWidget(self.table_widget, 0, 0, 1, 1)  # 将表格部件添加到布局中并占据整个窗口
        # layout.addWidget(self.table_widget, 0, 0, 1, 1)  # 将表格部件添加到布局中并占据整个窗口
        items_column1 = ['相机数量', '图片数量', '点云数', '观测点数', '平均跟踪长度', '每幅图片平均跟踪点数']
        items_column2 = ['1', '66', '64550', '265791', '4.1176', '4027.14']

        for row, content in enumerate(items_column1):
            item = QTableWidgetItem(content)

            # 设置单元格内容不可编辑
            item.setFlags(item.flags() ^ 2)  # 或 item.setFlags(item.flags() & ~2)

            self.table_widget.setItem(row, 0, item)

        for row, content in enumerate(items_column2):
            item = QTableWidgetItem(content)

            # 设置单元格内容不可编辑
            item.setFlags(item.flags() ^ 2)  # 或 item.setFlags(item.flags() & ~2)

            self.table_widget.setItem(row, 1, item)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Parameter of Reconstruction model"))


