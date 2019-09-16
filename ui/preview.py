#!/usr/bin/python
# -*- coding:utf-8 -*-
"""widgets preview panel

load preview widgets for view sytle effect

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from res.img_rc import *


class previewWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        tab1 = QWidget(self)
        tab2 = QWidget(self)
        tab3 = QWidget(self)
        tab4 = QWidget(self)
        tab5 = QWidget(self)
        tab6 = QWidget(self)
        self.addTab(tab1, self.tr("Basic"))#,"常用组件"))
        self.addTab(tab2, self.tr("Special"))#,"特别组件"))
        self.addTab(tab3, self.tr("Drawing"))#,"绘图组件"))
        self.addTab(tab4, self.tr("Layout"))#,"布局组件"))
        self.addTab(tab5, self.tr("Container"))#,"容器组件"))
        self.addTab(tab6, self.tr("Advance"))#,"高级组件"))
        self.setupTab1(tab1)
        self.setupTab2(tab2)
        self.setupTab3(tab3)
        self.setupTab4(tab4)
        self.setupTab5(tab5)
        self.setupTab6(tab6)

    # def chTextMode(self, editable):
    #     btns = self.dockColors.findChildren(QPushButton)
    #     if (editable):
    #         self.textEdit.setReadOnly(False)
    #         for b in btns:
    #             b.setEnabled(False)
    #         self.dockColors.setVisible(False)
    #         self.modeLabel.setText("编辑模式")
    #     else:
    #         self.textEdit.setReadOnly(True)
    #         for b in btns:
    #             b.setEnabled(True)
    #         self.dockColors.setVisible(True)
    #         self.modeLabel.setText("配色模式")

    def setupTab1(self, tab1):
        scrollContainer = QVBoxLayout()
        scrollArea = QScrollArea()
        scrollArea.setWidgetResizable(True)
        mainWidget = QWidget()
        layout = QVBoxLayout()
        mainWidget.setLayout(layout)
        mainWidget.setMinimumSize(QSize(420, 800))
        scrollArea.setWidget(mainWidget)
        scrollContainer.addWidget(scrollArea)
        tab1.setLayout(scrollContainer)

        # Label TextBox
        group1 = QGroupBox("Text")
        group1layout = QHBoxLayout()
        group1.setLayout(group1layout)
        layout.addWidget(group1)
        layoutCol1 = QFormLayout()
        layoutCol2 = QFormLayout()
        group1layout.addLayout(layoutCol1)
        group1layout.addLayout(layoutCol2)

        label1 = QLabel("账号(&Id)：")
        text1 = QLineEdit("default")
        label1.setBuddy(text1)
        label2 = QLabel("数据1：")
        text2 = QLineEdit()
        text2.setPlaceholderText("请输入数据")
        lebel3 = QLabel("<b>密码</b>(passward):")
        text3 = QLineEdit("******")
        text3.setEchoMode(QLineEdit.Password)
        label4 = QLabel("网址标签：")
        label5 = QLabel(
            "<a href='https://blog.csdn.net/hustlei/'>hustlei.ml</a>")
        label5.setOpenExternalLinks(True)
        label6 = QLabel("图标标签：")
        label7 = QLabel("图标")
        label7.setPixmap(QPixmap(":img/Flag_BlueHS.png"))
        layoutCol1.addRow(label1, text1)
        layoutCol1.addRow(label2, text2)
        layoutCol1.addRow(lebel3, text3)
        layoutCol1.addRow(label4, label5)
        layoutCol1.addRow(label6, label7)

        text4 = QLineEdit()
        text4.setInputMask("0000-00-00")
        text5 = QLineEdit()
        text5.setInputMask("HH:HH:HH:HH:HH:HH;_")
        text6 = QLineEdit()
        text6.setInputMask("XXXXXX")
        text7 = QLineEdit()
        validator1 = QDoubleValidator()
        validator1.setRange(0, 100)
        validator1.setDecimals(2)
        text7.setValidator(validator1)
        text8 = QLineEdit()
        validator2 = QRegExpValidator()
        reg = QRegExp("[a-zA-Z0-9]+$")
        validator2.setRegExp(reg)
        text8.setValidator(validator2)
        layoutCol2.addRow("日期掩码：", text4)
        layoutCol2.addRow("Mac地址掩码：", text5)
        layoutCol2.addRow("字符掩码：", text6)
        layoutCol2.addRow("实数校验：", text7)
        layoutCol2.addRow("正则表达式校验：", text8)

        text9 = QLineEdit()
        text9.setPlaceholderText("input email")
        text9.setToolTip("please input a email address.")
        model = QStandardItemModel(0, 1, self)
        completer = QCompleter(model, self)
        text9.setCompleter(completer)

        def textch(s):
            if("@" in s):
                return
            strList = [
                "@163.com",
                "@qq.com",
                "@gmail.com",
                "@hotmail.com",
                "@126.com"]
            model.removeRows(0, model.rowCount())
            for i in strList:
                model.insertRow(0)
                model.setData(model.index(0, 0), s + i)
        text9.textChanged.connect(textch)
        text10 = QLineEdit("ReadOnly")
        text10.setReadOnly(True)
        layoutCol1.addRow("自动补全:", text9)
        layoutCol2.addRow("Readonly:", text10)

        # Button
        group2 = QGroupBox("Button")
        group2layout = QVBoxLayout()
        group2.setLayout(group2layout)
        layout.addWidget(group2)
        layoutRow1 = QHBoxLayout()
        layoutRow2 = QHBoxLayout()
        group2layout.addLayout(layoutRow1)
        group2layout.addLayout(layoutRow2)

        btn1 = QPushButton("Button")
        btn2 = QPushButton("IconBtn")
        btn2.setIcon(QIcon(":img/yes.png"))
        btn3 = QPushButton("Disabled")
        btn3.setEnabled(False)
        btn4 = QPushButton("Default")
        btn4.setDefault(True)

        btn5 = QPushButton("Switch")
        btn5.setCheckable(True)
        btn6 = QToolButton()
        # btn6.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        btn6.setText("ToolButton")
        btn6.setPopupMode(QToolButton.MenuButtonPopup)
        m = QMenu()
        m.addAction("action1")
        m.addAction("action2")
        m.addAction("action3")
        btn6.setMenu(m)
        btn7 = QCommandLinkButton("LinkBtn")
        layoutRow1.addWidget(btn1)
        layoutRow1.addWidget(btn2)
        layoutRow1.addWidget(btn3)
        layoutRow1.addWidget(btn4)
        layoutRow2.addWidget(btn5)
        layoutRow2.addWidget(btn6)
        layoutRow2.addWidget(btn7)

        # Checkable Item
        group3 = QGroupBox("Checkable")
        group3Layout = QVBoxLayout()
        layoutRow1 = QHBoxLayout()
        layoutRow2 = QHBoxLayout()
        group3Layout.addLayout(layoutRow1)
        group3Layout.addLayout(layoutRow2)
        group3.setLayout(group3Layout)
        layout.addWidget(group3)

        group3.setCheckable(True)
        ch1 = QRadioButton("Radio")
        ch2 = QRadioButton("Iconradio")
        ch2.setIcon(QIcon(":img/Flag_blueHS.png"))
        ch3 = QRadioButton("Iconradio")
        ch3.setIcon(QIcon(":img/Flag_greenHS.png"))
        ch4 = QRadioButton("Disable")
        ch4.setEnabled(False)
        ch5 = QCheckBox("CheckBox")
        ch6 = QCheckBox("CheckBox")
        ch6.setIcon(QIcon(":img/Flag_blueHS.png"))
        ch7 = QCheckBox("TriState")
        ch7.setTristate(True)
        ch7.setCheckState(Qt.PartiallyChecked)
        ch8 = QCheckBox("Disable")
        ch8.setEnabled(False)
        layoutRow1.addWidget(ch1)
        layoutRow1.addWidget(ch2)
        layoutRow1.addWidget(ch3)
        layoutRow1.addWidget(ch4)
        layoutRow2.addWidget(ch5)
        layoutRow2.addWidget(ch6)
        layoutRow2.addWidget(ch7)
        layoutRow2.addWidget(ch8)

        # Selecting Input
        group4 = QGroupBox("Selectable")
        group4Layout = QVBoxLayout()
        layoutRow1 = QHBoxLayout()
        group4Layout.addLayout(layoutRow1)
        group4.setLayout(group4Layout)
        layout.addWidget(group4)

        s1 = QSpinBox()
        s1.setValue(50)
        s2 = QDoubleSpinBox()
        s2.setRange(0, 1)
        s2.setValue(0.5)
        s3 = QComboBox()
        s3.addItems(["aaa", "bbb", "ccc"])
        s3.setEditable(True)
        s3.setCurrentIndex(2)
        s4 = QComboBox()
        s4.addItems(["aaa", "bbb", "ccc"])
        layoutRow1.addWidget(s1)
        layoutRow1.addWidget(s2)
        layoutRow1.addWidget(s3)
        layoutRow1.addWidget(s4)

        # TextEdit
        group5 = QGroupBox("TextEdit")
        group5Layout = QVBoxLayout()
        group5.setLayout(group5Layout)
        layout.addWidget(group5)

        group5Layout.addWidget(QTextEdit("Text"))

        layout.addStretch(1)

    def setupTab2(self, tab2):
        scrollContainer = QVBoxLayout()
        scrollArea = QScrollArea()
        scrollArea.setWidgetResizable(True)
        mainWidget = QWidget()
        layout = QVBoxLayout()
        mainWidget.setLayout(layout)
        mainWidget.setMinimumSize(QSize(420, 800))
        scrollArea.setWidget(mainWidget)
        scrollContainer.addWidget(scrollArea)
        tab2.setLayout(scrollContainer)

        # Dialog
        group0 = QGroupBox("Dialog")
        group1Layout = QVBoxLayout()
        layoutRow1 = QHBoxLayout()
        layoutRow2 = QHBoxLayout()
        group1Layout.addLayout(layoutRow1)
        group1Layout.addLayout(layoutRow2)
        group0.setLayout(group1Layout)
        layout.addWidget(group0)

        b1 = QPushButton("信息对话框")
        b1.clicked.connect(
            lambda: QMessageBox.information(
                self,
                "Info",
                "这是一条消息",
                QMessageBox.Ok,
                QMessageBox.Ok))
        b2 = QPushButton("提问对话框")
        b2.clicked.connect(
            lambda: QMessageBox.question(
                self,
                "question",
                "确定要执行该操作吗？",
                QMessageBox.No | QMessageBox.Yes,
                QMessageBox.Yes))
        b3 = QPushButton("警告对话框")
        b3.clicked.connect(
            lambda: QMessageBox.warning(
                self,
                "warning",
                "这是一个警告消息",
                QMessageBox.No | QMessageBox.Yes,
                QMessageBox.Yes))
        b4 = QPushButton("出错对话框")
        b4.clicked.connect(
            lambda: QMessageBox.critical(
                self,
                "error",
                "这是一个出错提示",
                QMessageBox.No | QMessageBox.Yes,
                QMessageBox.Yes))
        b5 = QPushButton("关于对话框")
        b5.clicked.connect(
            lambda: QMessageBox.about(
                self, "about", "关于本程序的信息"))
        b6 = QPushButton("输入对话框")
        b6.clicked.connect(lambda: QInputDialog.getInt(self, "输入", "请输入整数"))
        b6.clicked.connect(lambda: QInputDialog.getDouble(self, "输入", "请输入实数"))
        b6.clicked.connect(
            lambda: QInputDialog.getItem(
                self, "输入", "请选择", [
                    "aaa", "bbb"]))
        b7 = QPushButton("颜色对话框")
        b7.clicked.connect(lambda: QColorDialog.getColor())
        b8 = QPushButton("字体对话框")
        b8.clicked.connect(lambda: QFontDialog.getFont())
        b9 = QPushButton("打开对话框")
        b9.clicked.connect(
            lambda: QFileDialog.getOpenFileName(
                self, "open", "", "Text(*.txt *.text)"))
        b10 = QPushButton("保存对话框")
        b10.clicked.connect(lambda: QFileDialog.getSaveFileName())
        layoutRow1.addWidget(b1)
        layoutRow1.addWidget(b2)
        layoutRow1.addWidget(b3)
        layoutRow1.addWidget(b4)
        layoutRow1.addWidget(b5)
        layoutRow2.addWidget(b6)
        layoutRow2.addWidget(b7)
        layoutRow2.addWidget(b8)
        layoutRow2.addWidget(b9)
        layoutRow2.addWidget(b10)

        # DateTime
        group1 = QGroupBox("DateTime")
        group1Layout = QHBoxLayout()
        layoutRow1 = QVBoxLayout()
        layoutRow2 = QVBoxLayout()
        group1Layout.addLayout(layoutRow1)
        group1Layout.addLayout(layoutRow2)
        group1.setLayout(group1Layout)
        layout.addWidget(group1)

        group1.setMaximumHeight(240)
        dt1 = QDateEdit()
        dt1.setDate(QDate.currentDate())
        dt2 = QTimeEdit()
        dt2.setTime(QTime.currentTime())
        dt3 = QDateTimeEdit()
        dt3.setDateTime(QDateTime.currentDateTime())
        dt4 = QDateTimeEdit()
        dt4.setCalendarPopup(True)
        dt5 = QCalendarWidget()
        dt5.setMaximumSize(QSize(250, 240))
        layoutRow1.addWidget(dt1)
        layoutRow1.addWidget(dt2)
        layoutRow1.addWidget(dt3)
        layoutRow1.addWidget(dt4)
        layoutRow2.addWidget(dt5)

        # Slider
        group2 = QGroupBox("Sliders")
        group2Layout = QVBoxLayout()
        layoutRow1 = QHBoxLayout()
        layoutRow2 = QHBoxLayout()
        group2Layout.addLayout(layoutRow1)
        group2Layout.addLayout(layoutRow2)
        group2.setLayout(group2Layout)
        layout.addWidget(group2)

        slider = QSlider()
        slider.setOrientation(Qt.Horizontal)
        slider.setMaximum(100)
        progress = QProgressBar()
        slider.valueChanged.connect(progress.setValue)
        slider.setValue(50)
        scroll1 = QScrollBar()
        scroll2 = QScrollBar()
        scroll3 = QScrollBar()
        scroll1.setMaximum(255)
        scroll2.setMaximum(255)
        scroll3.setMaximum(255)
        scroll1.setOrientation(Qt.Horizontal)
        scroll2.setOrientation(Qt.Horizontal)
        scroll3.setOrientation(Qt.Horizontal)
        c = QLabel("拖动滑块改变颜色")
        c.setAutoFillBackground(True)
        c.setAlignment(Qt.AlignCenter)
        #c.setStyleSheet("border:1px solid gray;")
        c.setStyleSheet("background:rgba(0,0,0,100);")

        def clr():
            # clr=QColor(scroll1.getValue(),scroll2.getValue(),scroll3.getValue(),100)
            # p=QPalette()
            # p.setColor(QPalette.Background,clr)
            # c.setPalette(p)
            c.setStyleSheet("background: rgba({},{},{},100);".format(
                scroll1.value(), scroll2.value(), scroll3.value()))
        scroll1.valueChanged.connect(clr)
        scroll2.valueChanged.connect(clr)
        scroll3.valueChanged.connect(clr)
        scroll1.setValue(128)
        layoutRow1.addWidget(slider)
        layoutRow1.addWidget(progress)
        layCol1 = QVBoxLayout()
        layCol1.addWidget(scroll1)
        layCol1.addWidget(scroll2)
        layCol1.addWidget(scroll3)
        layoutRow2.addLayout(layCol1)
        layoutRow2.addWidget(c)

        # Meter
        group3 = QGroupBox("Meters")
        layRow = QHBoxLayout()
        group3.setLayout(layRow)
        layout.addWidget(group3)

        dial1 = QDial()
        dial2 = QDial()
        dial2.setNotchesVisible(True)
        dial1.valueChanged.connect(dial2.setValue)
        layRow.addWidget(dial1)
        layRow.addWidget(dial2)

        layout.addStretch(1)

    def setupTab3(self, tab3):
        scrollContainer = QVBoxLayout()
        scrollArea = QScrollArea()
        mainWidget = QWidget()
        layout = QVBoxLayout()
        mainWidget.setLayout(layout)
        mainWidget.setMinimumSize(QSize(420, 500))
        scrollArea.setWidget(mainWidget)
        scrollContainer.addWidget(scrollArea)
        tab3.setLayout(scrollContainer)

        # Graphics
        class Drawing1(QWidget):
            def __init__(self, parent=None):
                super().__init__(parent)
                self.setMinimumHeight(170)

            def paintEvent(self, QPaintEvent):
                p = QPainter()
                p.begin(self)

                pen = QPen(Qt.black, 2, Qt.SolidLine)
                p.setPen(pen)
                p.drawLine(20, 15, 150, 15)
                pen.setStyle(Qt.DashLine)
                p.setPen(pen)
                p.drawLine(20, 35, 150, 35)
                pen.setStyle(Qt.DotLine)
                p.setPen(pen)
                p.drawLine(20, 55, 150, 55)
                pen.setStyle(Qt.DashDotLine)
                p.setPen(pen)
                p.drawLine(20, 75, 150, 75)
                pen.setStyle(Qt.DashDotDotLine)
                p.setPen(pen)
                p.drawLine(20, 95, 150, 95)
                pen.setStyle(Qt.CustomDashLine)
                pen.setDashPattern([1, 4, 5, 4])
                p.setPen(pen)
                p.drawLine(20, 115, 150, 115)

                pen.setWidth(1)
                pen.setStyle(Qt.SolidLine)
                p.setPen(pen)
                brush = QBrush(Qt.SolidPattern)
                p.setBrush(brush)
                p.drawRect(180, 10, 40, 30)
                brush = QBrush(Qt.Dense5Pattern)
                p.setBrush(brush)
                p.drawRect(240, 10, 40, 30)
                brush = QBrush(Qt.Dense7Pattern)
                p.setBrush(brush)
                p.drawRect(300, 10, 40, 30)

                brush = QBrush(Qt.green, Qt.HorPattern)
                p.setBrush(brush)
                p.drawRect(180, 50, 40, 30)
                brush = QBrush(Qt.green, Qt.VerPattern)
                p.setBrush(brush)
                p.drawRect(240, 50, 40, 30)
                brush = QBrush(Qt.green, Qt.Dense6Pattern)
                brush = QBrush(Qt.green, Qt.CrossPattern)
                p.setBrush(brush)
                p.drawRect(300, 50, 40, 30)

                brush = QBrush(Qt.blue, Qt.BDiagPattern)
                p.setBrush(brush)
                p.drawRect(180, 90, 40, 30)
                brush = QBrush(Qt.blue, Qt.FDiagPattern)
                p.setBrush(brush)
                p.drawRect(240, 90, 40, 30)
                brush = QBrush(Qt.blue, Qt.DiagCrossPattern)
                p.setBrush(brush)
                p.drawRect(300, 90, 40, 30)

                g = QLinearGradient(180, 130, 220, 160)
                g.setColorAt(0, Qt.red)
                g.setColorAt(1, Qt.blue)
                brush = QBrush(g)
                p.setBrush(brush)
                p.drawRect(180, 130, 40, 30)
                g = QRadialGradient(260, 145, 20)
                g.setColorAt(0, Qt.red)
                g.setColorAt(0.5, Qt.yellow)
                g.setColorAt(1, Qt.blue)
                p.setBrush(g)
                p.drawRect(240, 130, 40, 30)
                g = QConicalGradient(320, 145, 0)
                g.setColorAt(0, Qt.red)
                g.setColorAt(0.4, Qt.yellow)
                g.setColorAt(0.8, Qt.blue)
                g.setColorAt(1, Qt.red)
                p.setBrush(g)
                p.drawRect(300, 130, 40, 30)

                brush = QBrush()
                brush.setTexture(QPixmap(":img/texture.jpg"))
                p.setBrush(brush)
                pen.setColor(Qt.transparent)
                p.setPen(pen)
                p.drawRect(15, 130, 135, 35)

                p.end()

        group1 = QGroupBox("DrawGraphics")
        group1Layout = QHBoxLayout()
        group1.setLayout(group1Layout)
        layout.addWidget(group1)

        draw = Drawing1()
        group1Layout.addWidget(draw)

        # picture
        group2 = QGroupBox("Pictures")
        group2Layout = QHBoxLayout()
        group2.setLayout(group2Layout)
        layout.addWidget(group2)

        pic1 = QLabel()
        pic1.setPixmap(QPixmap(":img/cup.jpg"))
        group2Layout.addWidget(pic1)
        group2Layout.addStretch(1)

        class pic(QWidget):
            def __init__(self):
                super().__init__()
                self.setMinimumSize(QSize(100, 100))

            def paintEvent(self, QPaintEvent):
                p = QPainter()
                p.begin(self)
                img = QPixmap(":img/cup.jpg")
                s = QRect(0, 0, img.width(), img.height())
                self.setFixedSize(img.size())
                # img=QImag(":img/cup.jpg")
                # p.drawImage(0,0,img)
                p.drawPixmap(s, img, s)
                p.end()

        group2Layout.addWidget(pic())
        group2Layout.addStretch(1)

        layout.addStretch(1)

    def setupTab4(self, tab4):
        scrollContainer = QVBoxLayout()
        scrollArea = QScrollArea()
        scrollArea.setWidgetResizable(True)
        mainWidget = QWidget()
        layout = QVBoxLayout()
        mainWidget.setLayout(layout)
        mainWidget.setMinimumSize(QSize(420, 500))
        scrollArea.setWidget(mainWidget)
        scrollContainer.addWidget(scrollArea)
        tab4.setLayout(scrollContainer)

        group1 = QGroupBox("QHBoxLayout布局")
        l = QHBoxLayout()
        for i in range(1, 5):
            l.addWidget(QPushButton("按钮" + str(i)))
        group1.setLayout(l)
        layout.addWidget(group1)

        group2 = QGroupBox("QGridLayout布局")
        l = QGridLayout()
        l.addWidget(QLabel("第一行数据："), 0, 0)
        l.addWidget(QLabel("第二行数据："), 1, 0)
        l.addWidget(QLabel("第三行数据："), 2, 0)
        l.addWidget(QLineEdit(), 0, 1)
        l.addWidget(QLineEdit("0"), 1, 1)
        input = QLineEdit()
        input.setPlaceholderText("请输入：")
        l.addWidget(input, 2, 1)
        text = QTextEdit("这是一个文本框，在QGridLayout中占三行两列。")
        l.addWidget(text, 0, 2, 3, 2)
        group2.setLayout(l)
        layout.addWidget(group2)

        group3 = QGroupBox("QFormLayout布局")
        l = QFormLayout()

        l.addRow("请输入数据：", QLineEdit())
        l.addRow(QLabel("请选择数据："), QSpinBox())
        box = QComboBox()
        box.addItem("Item1"), box.addItem("Item2"), box.addItem("Item3")
        l.addRow("请选择选项：", box)
        group3.setLayout(l)
        layout.addWidget(group3)

        group4 = QGroupBox("Spliter MDI Dock")
        l = QHBoxLayout()
        group4.setLayout(l)
        layout.addWidget(group4)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter2 = QSplitter(Qt.Vertical)
        splitter1.resize(420, 350)
        splitter2.resize(350, 350)
        splitter2.setStretchFactor(0, 1)

        mdi = QMdiArea()
        mdi.addSubWindow(QWidget())
        mdi.addSubWindow(QWidget())
        mdi.cascadeSubWindows()
        w1 = QWidget()
        w2 = QWidget()
        d1 = QDockWidget("dock1", w1)
        d2 = QDockWidget("dock2", w1)
        d1.setAllowedAreas(Qt.LeftDockWidgetArea)
        d1.setFeatures(QDockWidget.AllDockWidgetFeatures |
                       QDockWidget.DockWidgetVerticalTitleBar)
        d2.setFeatures(QDockWidget.DockWidgetVerticalTitleBar)
        d3 = QDockWidget("dock3", w2)
        d4 = QDockWidget("dock4", w2)
        d3.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.TopDockWidgetArea)
        w1.resize(120, 120)
        splitter2.addWidget(w1)
        splitter2.addWidget(w2)
        splitter1.addWidget(mdi)
        splitter1.addWidget(splitter2)
        l.addWidget(splitter1)

        layout.addStretch(1)

    def setupTab5(self, tab):
        scrollContainer = QVBoxLayout()
        scrollArea = QScrollArea()
        mainWidget = QWidget()
        layout = QVBoxLayout()
        mainWidget.setLayout(layout)
        mainWidget.setMinimumSize(QSize(420, 600))
        scrollArea.setWidgetResizable(True)
        scrollArea.setWidget(mainWidget)
        scrollContainer.addWidget(scrollArea)
        tab.setLayout(scrollContainer)

        group = QGroupBox("QGroupBox控件")
        l = QHBoxLayout()
        l.addWidget(QLabel("这是一个QGroupBox控件"))
        group.setLayout(l)
        layout.addWidget(group)

        group = QGroupBox("StackLayout布局")
        l = QHBoxLayout()
        group.setLayout(l)
        list = QListWidget()
        stack = QStackedWidget()
        l.addWidget(list)
        l.addWidget(stack)
        list.currentRowChanged.connect(stack.setCurrentIndex)
        list.addItem("stack1")
        list.addItem("stack2")
        list.addItem("stack3")
        s1 = QGroupBox("stack1")
        s2 = QGroupBox("stack2")
        s3 = QGroupBox("stack3")
        l1 = QLabel("stack1")
        l2 = QLabel("stack2")
        l3 = QLabel("stack3")
        t1 = QLineEdit()
        t2 = QLineEdit()
        t3 = QLineEdit()
        lay1 = QHBoxLayout()
        lay2 = QHBoxLayout()
        lay3 = QHBoxLayout()
        lay1.addWidget(l1)
        lay2.addWidget(l2)
        lay3.addWidget(l3)
        lay1.addWidget(t1)
        lay2.addWidget(t2)
        lay3.addWidget(t3)
        s1.setLayout(lay1)
        s2.setLayout(lay2)
        s3.setLayout(lay3)
        stack.addWidget(s1)
        stack.addWidget(s2)
        stack.addWidget(s3)
        layout.addWidget(group)
        group = QGroupBox("StackLayout布局")

        group = QGroupBox("ToolBox")
        lay = QVBoxLayout()
        group.setLayout(lay)
        layout.addWidget(group)

        t1 = QToolBox()
        w1 = QWidget()
        w2 = QWidget()
        i1 = QVBoxLayout()
        i2 = QVBoxLayout()
        w1.setLayout(i1)
        w2.setLayout(i2)
        i1.addWidget(QLabel("aaaaa"))
        i1.addWidget(QLabel("aaaaa"))
        i1.addWidget(QLabel("aaaaa"))
        i2.addWidget(QLabel("aaaaa"))
        i2.addWidget(QLabel("aaaaa"))
        i1.addStretch(1)
        t1.addItem(w1, "Tab1")
        t1.addItem(w2, "Tab2")
        t1.addItem(QWidget(), "tab3")
        lay.addWidget(t1)

        group = QGroupBox("TabWidget")
        lay = QVBoxLayout()
        lay1 = QHBoxLayout()
        lay2 = QHBoxLayout()
        lay.addLayout(lay1)
        lay.addLayout(lay2)
        group.setLayout(lay)
        layout.addWidget(group)

        t1 = QTabWidget()
        t1.addTab(QWidget(), "tab1")
        t1.addTab(QWidget(), "tab2")
        t1.setTabsClosable(True)
        t1.setMinimumHeight(200)
        t2 = QTabWidget()
        t2.addTab(QWidget(), "tab1")
        t2.addTab(QWidget(), "tab2")
        t2.setTabPosition(QTabWidget.South)
        t2.setTabShape(QTabWidget.Triangular)
        t3 = QTabWidget()
        t3.addTab(QWidget(), "tab1")
        t3.addTab(QWidget(), "tab2")
        t3.setTabPosition(QTabWidget.West)
        t4 = QTabWidget()
        t4.addTab(QWidget(), "tab1")
        t4.addTab(QWidget(), "tab2")
        t4.setTabPosition(QTabWidget.East)
        t3.setMinimumHeight(300)
        lay1.addWidget(t1)
        lay1.addWidget(t2)
        lay2.addWidget(t3)
        lay2.addWidget(t4)

    def setupTab6(self, tab):
        container = QHBoxLayout()
        scrollArea = QScrollArea()
        scrollArea.setWidgetResizable(True)
        w = QWidget()
        w.setMinimumSize(QSize(400, 500))
        layout = QVBoxLayout()
        w.setLayout(layout)
        scrollArea.setWidget(w)
        container.addWidget(scrollArea)
        tab.setLayout(container)

        # List
        lay = QHBoxLayout()
        layout.addLayout(lay)
        list1 = QListWidget()
        list1.addItems(["aaa", "bbb", "ccc"])
        list2 = QListWidget()
        list2.addItem(QListWidgetItem(QIcon(":img/Flag_blueHS.png"), "blue"))
        list2.addItem(QListWidgetItem(QIcon(":img/Flag_redHS.png"), "red"))
        list2.addItem(QListWidgetItem(QIcon(":img/Flag_greenHS.png"), "green"))
        list2.setViewMode(QListWidget.IconMode)
        lay.addWidget(list1)
        lay.addWidget(list2)

        # Table
        lay = QHBoxLayout()
        layout.addLayout(lay)
        t1 = QTableWidget()
        t1.setRowCount(3)
        t1.setColumnCount(3)
        for i in range(3):
            for j in range(3):
                t1.setItem(i, j, QTableWidgetItem(str((i + 1) * (j + 1))))
                t1.item(i, j).setTextAlignment(Qt.AlignCenter)
        t1.setColumnWidth(0, 50)
        t1.setColumnWidth(1, 50)
        t1.setColumnWidth(2, 50)
        t1.setEditTriggers(QTableWidget.AllEditTriggers)
        t2 = QTableWidget()
        t2.setRowCount(3)
        t2.setColumnCount(3)
        t2.setHorizontalHeaderLabels(["Name", "Gender", "Age"])
        t2.setVerticalHeaderLabels(["1st", "2rd", "3th"])
        t2.setItem(0, 0, QTableWidgetItem("july"))
        c = QComboBox()
        c.addItems(["Male", "Famale"])
        t2.setCellWidget(0, 1, c)
        t2.cellWidget(0, 1).setCurrentIndex(1)
        t2.setItem(0, 2, QTableWidgetItem("10"))
        t2.setItem(1, 0, QTableWidgetItem("john"))
        c = QComboBox()
        c.addItems(["Male", "Famale"])
        c.setEditable(True)
        t2.setCellWidget(1, 1, c)
        t2.setItem(1, 2, QTableWidgetItem("11"))
        t2.resizeColumnsToContents()
        t2.setEditTriggers(QTableWidget.EditKeyPressed | QTableWidget.SelectedClicked |
                           QTableWidget.AnyKeyPressed | QTableWidget.DoubleClicked)

        lay.addWidget(t1)
        lay.addWidget(t2)

        # Tree
        lay = QHBoxLayout()
        layout.addLayout(lay)
        tree1 = QTreeWidget()
        tree1.setColumnCount(2)
        tree1.setHeaderLabels(["Key", "Value"])
        node1 = QTreeWidgetItem()
        node1.setText(0, "root")
        node1.setText(1, "0")
        node1.setIcon(0, QIcon(":img/home.png"))
        tree1.addTopLevelItem(node1)
        node11 = QTreeWidgetItem()
        node11.setText(0, "child1")
        icon = QIcon(":img/book_angle.png")
        icon.addPixmap(QPixmap(":img/book_open.png"), QIcon.Normal, QIcon.On)
        node11.setIcon(0, icon)
        nodea = QTreeWidgetItem()
        nodea.setText(0, "red")
        nodea.setBackground(1, QBrush(Qt.red))
        nodeb = QTreeWidgetItem()
        nodeb.setText(0, "gray")
        nodeb.setBackground(1, QBrush(Qt.gray))
        nodec = QTreeWidgetItem()
        nodec.setText(0, "green")
        nodec.setBackground(1, QBrush(Qt.green))
        node11.addChildren([nodea, nodeb, nodec])
        node12 = QTreeWidgetItem()
        node12.setText(0, "child2")
        node12.setText(1, "child2")
        node13 = QTreeWidgetItem()
        node13.setText(0, "child3")
        node13.setText(1, "child3")
        node12.setIcon(0, icon)
        node13.setIcon(0, icon)
        node1.addChild(node11)
        node1.addChild(node12)
        node1.addChild(node13)
        tree1.expand(tree1.model().index(0, 0))
        tree1.expandItem(node11)
        tree2 = QTreeView()
        dir = QDirModel()
        tree2.setModel(dir)
        lay.addWidget(tree1)
        lay.addWidget(tree2)


"""
+ 常用组件:
    - Label
    - LineEdit,TextEdit
    - PushButton,ToolButton,CommandlinkButton
    - RadioButton, CheckButton
    - Combobox,SpinBox,DoubleSpinBox
    - DateEdit,TimeEdit,DateTimeEdit,Calendar
    - Slider,ProgressBar,ScrollBar
    - Dial,LCDNumber,KeySequenceEdit
    - Graphics
+ 布局
    - VBox,HBox
    - Grid
    - Form
    - Spliter
    - DockWidget,MDI
+ 容器组件
    - ScrollArea
    - GroupBox
    - StackedWidget
    - ToolBox
    - TabWidget
+ 高级组件
    - Dialog
        * massagebox,input,file,color
        * https://blog.csdn.net/taiyang1987912/article/details/31770757
    - List
    - Table
    - Tree
"""

if __name__ == "__main__":
    import sys
    import os
    os.chdir(os.path.join(os.path.dirname(__file__), ".."))
    app = QApplication(sys.argv)
    win = previewWidget()
    win.resize(500, 600)
    win.show()
    sys.exit(app.exec())
