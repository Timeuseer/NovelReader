# -*- coding: utf-8 -*-



import wx
import wx.xrc




class register_flose2(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(248, 153), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer18 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText12 = wx.StaticText(self, wx.ID_ANY, u"注册失败！", wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.m_staticText12.Wrap(-1)
        self.m_staticText12.SetFont(wx.Font(15, 70, 90, 90, False, wx.EmptyString))

        bSizer18.Add(self.m_staticText12, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText15 = wx.StaticText(self, wx.ID_ANY, u"您输入的邮箱已经被注册！\n请重新输入新的邮箱地址！", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText15.Wrap(-1)
        bSizer18.Add(self.m_staticText15, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(bSizer18)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


