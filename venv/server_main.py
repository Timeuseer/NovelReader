# -*- coding: UTF-8 -*-
import wx
import serverui_login
import sys




class MianWindow(serverui_login.readserverui_login):
    pass





if __name__ == '__main__':
    app = wx.App()

    main_win = MianWindow(None)
    main_win.Show()
    app.MainLoop()
