# -*- coding: utf-8 -*-



import wx
import wx.xrc




class login_flose1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"登录失败", pos=wx.DefaultPosition, size=wx.Size(286, 113),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        bSizer21 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText12 = wx.StaticText(self, wx.ID_ANY, u"登录失败！", wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.m_staticText12.Wrap(-1)
        self.m_staticText12.SetFont(wx.Font(15, 70, 90, 90, False, wx.EmptyString))

        bSizer21.Add(self.m_staticText12, 0, wx.ALL, 5)

        bSizer3.Add(bSizer21, 0, wx.ALIGN_CENTER, 5)

        bSizer22 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText13 = wx.StaticText(self, wx.ID_ANY, u"您输入的用户名不存在，请重新输入！", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText13.Wrap(-1)
        self.m_staticText13.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))

        bSizer22.Add(self.m_staticText13, 0, wx.ALL, 5)

        bSizer3.Add(bSizer22, 1, wx.ALIGN_CENTER, 5)

        self.SetSizer(bSizer3)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


