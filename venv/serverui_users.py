# -*- coding: utf-8 -*-



import wx
import wx.xrc
import wx.grid
import serverui_main
import pymysql



class users(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"已有用户列表", pos=wx.DefaultPosition, size=wx.Size(434, 674),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.load_user()
        user_len = len(self.userinfo)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        bSizer6.SetMinSize(wx.Size(434, 674))
        self.m_grid2 = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid2.CreateGrid(user_len, 7)
        self.m_grid2.EnableEditing(True)
        self.m_grid2.EnableGridLines(True)
        self.m_grid2.EnableDragGridSize(False)
        self.m_grid2.SetMargins(0, 0)

        # Columns
        self.m_grid2.EnableDragColMove(False)
        self.m_grid2.EnableDragColSize(True)
        self.m_grid2.SetColLabelSize(30)
        self.m_grid2.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.m_grid2.EnableDragRowSize(True)
        self.m_grid2.SetRowLabelSize(80)
        self.m_grid2.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance
        self.m_grid2.SetRowLabelValue(0, "1")
        self.m_grid2.SetColLabelValue(0, "用户编号")
        self.m_grid2.SetColLabelValue(1, "用户名")
        self.m_grid2.SetColLabelValue(2, "用户密码")
        self.m_grid2.SetColLabelValue(3, "用户邮箱")
        self.m_grid2.SetColLabelValue(4, "用户电话")
        self.m_grid2.SetColLabelValue(5, "用户最近登录时间")
        self.m_grid2.SetColLabelValue(6, "用户注册时间")
        i = 0
        for x in self.userinfo:
            j = 0
            for y in x:
                self.m_grid2.SetCellValue(i, j, str(y))
                j += 1
            i += 1

        # Cell Defaults
        self.m_grid2.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer6.Add(self.m_grid2, 1, wx.EXPAND, 5)

        bSizer6.AddSpacer(5)

        self.m_button15 = wx.Button(self, wx.ID_ANY, u"返回上一层", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer6.Add(self.m_button15, 0, wx.EXPAND, 5)

        self.SetSizer(bSizer6)
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

    def load_user(self):
        db = pymysql.connect(host='localhost',
                             user='root', password='xy199491314',
                             database='readbooks', charset='utf8')

        cur = db.cursor()

        cur.execute('select * from user_info')
        self.userinfo =list(cur.fetchall())

        cur.close()
        db.close()



