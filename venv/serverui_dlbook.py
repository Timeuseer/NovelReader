# -*- coding: utf-8 -*-


import wx
import wx.xrc
import wx.grid
import serverui_main
import serverui_delsure
import pymysql


global dl_info
dl_info =  list()

class delete_books(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"删除图书", pos=wx.DefaultPosition, size=wx.Size(434, 674),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.Size(434, 674), wx.DefaultSize)

        bSizer34 = wx.BoxSizer(wx.VERTICAL)

        bSizer34.SetMinSize(wx.Size(434, 674))
        self.m_bitmap9 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"../venv/jiange3.jpg", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.Size(-1, 50), 0)
        bSizer34.Add(self.m_bitmap9, 0, 0, 5)

        m_choice1Choices = [u"按书籍类型查找", u"按书籍名查找", u"按书籍作者查找"]
        self.m_choice1 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0)
        self.m_choice1.SetSelection(2)
        bSizer34.Add(self.m_choice1, 0, wx.EXPAND | wx.ALL, 5)

        bSizer35 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_textCtrl12 = wx.TextCtrl(self, wx.ID_ANY, u"请输入书籍相关信息", wx.DefaultPosition, wx.Size(-1, 30), 0)
        bSizer35.Add(self.m_textCtrl12, 1, wx.ALL, 5)

        self.m_button23 = wx.Button(self, wx.ID_ANY, u"查找", wx.DefaultPosition, wx.Size(50, 30), 0)
        bSizer35.Add(self.m_button23, 0, wx.ALL, 5)

        bSizer34.Add(bSizer35, 0, wx.EXPAND, 5)

        self.m_grid3 = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid3.CreateGrid(199, 7)
        self.m_grid3.EnableEditing(True)
        self.m_grid3.EnableGridLines(True)
        self.m_grid3.EnableDragGridSize(False)
        self.m_grid3.SetMargins(0, 0)

        # Columns
        self.m_grid3.EnableDragColMove(False)
        self.m_grid3.EnableDragColSize(True)
        self.m_grid3.SetColLabelSize(30)
        self.m_grid3.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.m_grid3.EnableDragRowSize(True)
        self.m_grid3.SetRowLabelSize(80)
        self.m_grid3.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance
        self.m_grid3.SetRowLabelValue(0, "1")
        self.m_grid3.SetColLabelValue(0, "图书编号")
        self.m_grid3.SetColLabelValue(1, "图书名")
        self.m_grid3.SetColLabelValue(2, "图书作者")
        self.m_grid3.SetColLabelValue(3, "图书路径")
        self.m_grid3.SetColLabelValue(4, "图书图片")
        self.m_grid3.SetColLabelValue(5, "图书类型")
        self.m_grid3.SetColLabelValue(6, "图书添加时间")

        # Cell Defaults
        self.m_grid3.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer34.Add(self.m_grid3, 1, wx.EXPAND | wx.ALL, 5)

        self.m_button24 = wx.Button(self, wx.ID_ANY, u"返回上一层", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer34.Add(self.m_button24, 0, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer34)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_choice1.Bind(wx.EVT_CHOICE, self.select_type)
        self.m_textCtrl12.Bind(wx.EVT_TEXT, self.book_info)
        self.m_button23.Bind(wx.EVT_BUTTON, self.select_book)
        self.m_button24.Bind(wx.EVT_BUTTON, self.go_back)
        self.m_grid3.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.del_book)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def select_type(self, event):

        event.Skip()

    def book_info(self, event):
        event.Skip()

    def select_book(self, event):
        index = self.m_choice1.GetCurrentSelection()
        self.info = self.m_textCtrl12.GetValue()
        if index == 0:
            self.type ='book_type'
        elif index == 1:
            self.type = 'book_name'
        else:
            self.type = 'book_auther'

        self.m_grid3.ClearGrid()
        self.load_book()

        event.Skip()

    def load_book(self):
        db = pymysql.connect(host='localhost',
                             user='root', password='xy199491314',
                             database='readbooks', charset='utf8')

        cur = db.cursor()
        print(self.type,self.info)
        cur.execute('select * from book_info where %s="%s"'%(self.type,self.info))

        self.bookinfo = list(cur.fetchall())
        i = 0
        for x in self.bookinfo:
            j = 0
            for y in x:
                self.m_grid3.SetCellValue(i, j, str(y))
                j += 1
            i += 1

        cur.close()
        db.close()

    def del_book(self, event):
        global dl_info

        for x in range(7):
            dl_info.append(self.m_grid3.GetCellValue(event.GetRow(),x))

        if self.m_grid3.GetCellValue(event.GetRow(),0) != None:
            app = wx.App()

            main_win = serverui_delsure.delete_sure(None)
            main_win.Show()
            app.MainLoop()

        event.Skip()

    def go_back(self, event):
        app = wx.App()

        main_win = serverui_main.readserverui_main(None)
        main_win.Show()
        self.Destroy()
        app.MainLoop()


