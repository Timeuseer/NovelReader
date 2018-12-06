# -*- coding: utf-8 -*-

import wx
import wx.xrc
import serverui_localadd
import pymysql



class ladd_lose(wx.Frame):

    def __init__(self, parent):
        trr = '上传失败'

        if serverui_localadd.tr != None:
            trr = serverui_localadd.tr
        print(serverui_localadd.err)

        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title='图书上传失败', pos=wx.DefaultPosition,
                          size=wx.Size(275, 155), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer18 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText12 = wx.StaticText(self, wx.ID_ANY, trr, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.m_staticText12.Wrap(-1)
        self.m_staticText12.SetFont(wx.Font(15, 70, 90, 90, False, wx.EmptyString))

        bSizer18.Add(self.m_staticText12, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText15 = wx.StaticText(self, wx.ID_ANY, serverui_localadd.err, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText15.Wrap(-1)
        bSizer18.Add(self.m_staticText15, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(bSizer18)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


