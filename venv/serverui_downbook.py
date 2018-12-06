# -*- coding: utf-8 -*-


import wx
import wx.xrc
import serverui_urladd


class down_book(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"下载图书...", pos=wx.DefaultPosition, size=wx.Size(409, 292),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer29 = wx.BoxSizer(wx.VERTICAL)

        m_listBox1Choices = [str(x) for x in serverui_urladd.s]

        self.m_listBox1 = wx.ListBox(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(400, 400), m_listBox1Choices, 0)
        bSizer29.Add(self.m_listBox1, 0, wx.ALL, 5)

        self.SetSizer(bSizer29)
        self.Layout()

        self.Centre(wx.BOTH)



    def __del__(self):
        pass


