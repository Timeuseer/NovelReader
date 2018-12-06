# -*- coding: utf-8 -*-



import wx
import wx.xrc
import serverui_login
import serverui_add_books
import serverui_books
import serverui_readbook
import serverui_dlbook
import serverui_upbooks



class readserverui_main(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"我趣阅读", pos=wx.DefaultPosition,
                          size=wx.Size(434, 674), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        bSizer4.SetMinSize(wx.Size(434, 674))
        self.m_bitmap4 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"../venv/jiange2.jpg", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.Size(-1, 265), 0)
        bSizer4.Add(self.m_bitmap4, 0, 0, 5)

        bSizer4.AddSpacer(20)

        self.show_user = wx.Button(self, wx.ID_ANY, u"查看书籍", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.show_user, 0, wx.ALIGN_CENTER | wx.EXPAND, 5)

        bSizer4.AddSpacer(25)

        self.show_books = wx.Button(self, wx.ID_ANY, u"阅读书籍", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.show_books, 0, wx.ALIGN_CENTER | wx.EXPAND, 5)

        bSizer4.AddSpacer(25)

        self.add_books = wx.Button(self, wx.ID_ANY, u"添加书籍", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.add_books, 0, wx.EXPAND, 5)

        bSizer4.AddSpacer(25)

        self.delete_books = wx.Button(self, wx.ID_ANY, u"删除书籍", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.delete_books, 0, wx.EXPAND, 5)

        bSizer4.AddSpacer(25)

        self.m_button10 = wx.Button(self, wx.ID_ANY, u"修改书籍", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_button10, 0, wx.EXPAND, 5)

        bSizer4.AddSpacer(25)

        self.out = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.out, 0, wx.EXPAND, 5)

        self.SetSizer(bSizer4)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.show_user.Bind(wx.EVT_BUTTON, self.show_users)
        self.show_books.Bind(wx.EVT_BUTTON, self.show_book)
        self.add_books.Bind(wx.EVT_BUTTON, self.add_book)
        self.delete_books.Bind(wx.EVT_BUTTON, self.del_book)
        self.m_button10.Bind(wx.EVT_BUTTON, self.updata_book)
        self.out.Bind(wx.EVT_BUTTON, self.quit_main)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def show_users(self, event):
        app = wx.App()

        main_win = serverui_books.books(None)
        main_win.Show()
        self.Destroy()
        app.MainLoop()


    def show_book(self, event):
        app = wx.App()

        main_win = serverui_readbook.readBook(None)
        main_win.Show()
        self.Destroy()
        app.MainLoop()


    def add_book(self, event):
        app = wx.App()

        main_win = serverui_add_books.add_books(None)
        main_win.Show()
        self.Destroy()
        app.MainLoop()

    def del_book(self, event):
        app = wx.App()

        main_win = serverui_dlbook.delete_books(None)
        main_win.Show()
        self.Destroy()
        app.MainLoop()

    def updata_book(self, event):
        app = wx.App()

        main_win = serverui_upbooks.update_books(None)
        main_win.Show()
        self.Destroy()
        app.MainLoop()

    def quit_main(self, event):
        app = wx.App()

        main_win = serverui_login.readserverui_login(None)
        main_win.Show()
        self.Destroy()
        app.MainLoop()


