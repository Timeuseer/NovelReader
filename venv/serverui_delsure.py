# -*- coding: utf-8 -*-



import wx
import wx.xrc
import serverui_dlbook
import pymysql



class delete_sure(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"删除操作", pos=wx.DefaultPosition, size=wx.Size(314, 165),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.Size(314, 165), wx.DefaultSize)

        bSizer34 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText25 = wx.StaticText(self, wx.ID_ANY, u"确认删除？", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText25.Wrap(-1)
        self.m_staticText25.SetFont(wx.Font(20, 70, 90, 90, False, wx.EmptyString))

        bSizer34.Add(self.m_staticText25, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_staticText26 = wx.StaticText(self, wx.ID_ANY, u"点击确认，将删除您所点击的这一行数据！\n若不想删除您本次点击的信息，点击取消！",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText26.Wrap(-1)
        bSizer34.Add(self.m_staticText26, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        m_sdbSizer1 = wx.StdDialogButtonSizer()
        self.m_sdbSizer1OK = wx.Button(self, wx.ID_OK)
        m_sdbSizer1.AddButton(self.m_sdbSizer1OK)
        self.m_sdbSizer1No = wx.Button(self, wx.ID_NO)
        m_sdbSizer1.AddButton(self.m_sdbSizer1No)
        m_sdbSizer1.Realize();

        bSizer34.Add(m_sdbSizer1, 0, wx.ALIGN_CENTER, 5)

        self.SetSizer(bSizer34)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_ACTIVATE, self.yes_click)
        self.Bind(wx.EVT_CLOSE, self.no_click)
        self.m_sdbSizer1No.Bind(wx.EVT_BUTTON, self.n_delete)
        self.m_sdbSizer1OK.Bind(wx.EVT_BUTTON, self.y_delete)

    def __del__(self):
        pass

        # Virtual event handlers, overide them in your derived class

    def yes_click(self, event):
        event.Skip()

    def no_click(self, event):
        event.Skip()

    def n_delete(self, event):
        self.Destroy()

    def y_delete(self, event):
        db = pymysql.connect(host='localhost',
                             user='root', password='xy199491314',
                             database='readbooks', charset='utf8')

        cur = db.cursor()

        cur.execute('delete from book_info where book_name = "%s" and book_auther ="%s"'%(serverui_dlbook.dl_info[1],serverui_dlbook.dl_info[2]))


        db.commit()
        cur.close()
        db.close()
        event.Skip()
        self.Destroy()


