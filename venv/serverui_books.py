# -*- coding: utf-8 -*-



import wx
import wx.xrc
import wx.grid
import serverui_main
import pymysql




class books(wx.Frame):

    def __init__(self, parent):
        self.load_book()
        col_len = len(self.bookinfo)
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"已有图书列表", pos=wx.DefaultPosition, size=wx.Size(434, 674),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        bSizer7.SetMinSize(wx.Size(434, 674))
        self.book_grid = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.book_grid.CreateGrid(col_len, 7)
        self.book_grid.EnableEditing(True)
        self.book_grid.EnableGridLines(True)
        self.book_grid.SetGridLineColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_APPWORKSPACE))
        self.book_grid.EnableDragGridSize(False)
        self.book_grid.SetMargins(0, 0)

        # Columns
        self.book_grid.EnableDragColMove(False)
        self.book_grid.EnableDragColSize(True)
        self.book_grid.SetColLabelSize(30)
        self.book_grid.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.book_grid.EnableDragRowSize(True)
        self.book_grid.SetRowLabelSize(80)
        self.book_grid.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance
        self.book_grid.SetRowLabelValue(0, "1")
        self.book_grid.SetColLabelValue(0, "图书编号")
        self.book_grid.SetColLabelValue(1, "图书名")
        self.book_grid.SetColLabelValue(2, "图书作者")
        self.book_grid.SetColLabelValue(3, "图书路径")
        self.book_grid.SetColLabelValue(4, "图书图片")
        self.book_grid.SetColLabelValue(5, "图书类型")
        self.book_grid.SetColLabelValue(6, "图书添加时间")
        i = 0
        for x in self.bookinfo:
            j = 0
            for y in x:
                self.book_grid.SetCellValue(i, j, str(y))
                j += 1
            i += 1
        # Cell Defaults
        self.book_grid.SetDefaultCellFont(wx.Font(10, 70, 90, 90, False, wx.EmptyString))
        self.book_grid.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer7.Add(self.book_grid, 1, wx.EXPAND, 5)

        bSizer7.AddSpacer(5)

        self.m_button15 = wx.Button(self, wx.ID_ANY, u"返回上一层", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.m_button15, 0, wx.EXPAND, 5)

        self.SetSizer(bSizer7)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button15.Bind(wx.EVT_BUTTON, self.go_back)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def go_back(self, event):
        app = wx.App()

        main_win = serverui_main.readserverui_main(None)
        main_win.Show()
        self.Destroy()
        app.MainLoop()

    def load_book(self):
        db = pymysql.connect(host='localhost',
                             user='root', password='xy199491314',
                             database='readbooks', charset='utf8')

        cur = db.cursor()

        cur.execute('select * from book_info')

        self.bookinfo =list(cur.fetchall())

        cur.close()
        db.close()


