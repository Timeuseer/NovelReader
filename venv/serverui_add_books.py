# -*- coding: utf-8 -*-



import wx
import wx.xrc
import serverui_main
import serverui_localadd
import serverui_urladd



class add_books(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"添加图书", pos=wx.DefaultPosition, size=wx.Size(434, 674),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        bSizer5.SetMinSize(wx.Size(434, 674))
        self.m_bitmap6 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"../venv/jiange2.jpg", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.Size(-1, 400), 0)
        bSizer5.Add(self.m_bitmap6, 0, 0, 5)

        bSizer5.AddSpacer(20)

        self.add_booksbt = wx.Button(self, wx.ID_ANY, u"从本地导入图书", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.add_booksbt, 0, wx.EXPAND, 5)

        bSizer5.AddSpacer(40)

        self.add_booksbt2 = wx.Button(self, wx.ID_ANY, u"从网上下载图书", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.add_booksbt2, 0, wx.EXPAND, 5)

        bSizer5.AddSpacer(65)

        self.m_button14 = wx.Button(self, wx.ID_ANY, u"返回上一层", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_button14, 0, wx.EXPAND, 5)

        self.SetSizer(bSizer5)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.add_booksbt.Bind(wx.EVT_BUTTON, self.local_book)
        self.add_booksbt2.Bind(wx.EVT_BUTTON, self.url_book)
        self.m_button14.Bind(wx.EVT_BUTTON, self.go_back)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def local_book(self, event):
        app = wx.App()

        main_win = serverui_localadd.local_addbook(None)
        main_win.Show()
        app.MainLoop()

    def url_book(self, event):
        app = wx.App()

        main_win = serverui_urladd.url_addbook(None)
        main_win.Show()
        app.MainLoop()

    def go_back(self, event):
        app = wx.App()

        main_win = serverui_main.readserverui_main(None)
        main_win.Show()
        self.Destroy()
        app.MainLoop()


