# -*- coding: utf-8 -*-

import wx
import wx.xrc
import serverui_readbook




class read_book(wx.Frame):
    x = 0
    def __init__(self, parent,bName,tList,cList):
        self.bName = bName
        self.tList = tList
        self.cList = cList
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u""+bName, pos=wx.DefaultPosition, size=wx.Size(434, 674),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        bSizer7.SetMinSize(wx.Size(434, 674))
        self.bookName = wx.StaticText(self, wx.ID_ANY, u""+self.tList[self.x], wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.ST_NO_AUTORESIZE)
        self.bookName.Wrap(-1)
        bSizer7.Add(self.bookName, 0, wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl13 = wx.TextCtrl(self, wx.ID_ANY, u""+self.cList[self.x][0], wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE)
        bSizer7.Add(self.m_textCtrl13, 1, wx.ALL | wx.EXPAND, 5)

        bSizer39 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button22 = wx.Button(self, wx.ID_ANY, u"上一章", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer39.Add(self.m_button22, 1, wx.ALL, 5)

        self.m_button23 = wx.Button(self, wx.ID_ANY, u"下一章", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer39.Add(self.m_button23, 1, wx.ALL, 5)

        bSizer7.Add(bSizer39, 0, wx.EXPAND, 5)

        self.SetSizer(bSizer7)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button22.Bind(wx.EVT_BUTTON, self.go_back)
        self.m_button23.Bind(wx.EVT_BUTTON, self.go_next)

    def __del__(self):
        app = wx.App()

        main_win = serverui_readbook.readBook(None)
        main_win.Show()
        app.MainLoop()

    # Virtual event handlers, overide them in your derived class
    def go_back(self, event):
        event.Skip()
        self.x = self.x - 1
        if self.x >  - 1:
            self.bookName.SetLabel(self.tList[self.x])
            self.m_textCtrl13.SetValue(self.cList[self.x][0])
        else:
            self.x = self.x + 1

    def go_next(self, event):
        event.Skip()
        self.x = self.x + 1
        if self.x < len(self.cList):
            self.bookName.SetLabel(self.tList[self.x])
            self.m_textCtrl13.SetValue(self.cList[self.x][0])
        else:
            self.x = self.x - 1


if __name__ == '__main__':
    app = wx.App()

    main_win = read_book(None)
    main_win.Show()
    app.MainLoop()


