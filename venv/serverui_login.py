# -*- coding: utf-8 -*-



import wx
import wx.xrc
import serverui_register
import serverui_main
import serverui_loginlose
import serverui_loginlose1
import pymysql



class readserverui_login(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"我趣阅读（服务端）", pos=wx.DefaultPosition,
                          size=wx.Size(434, 674), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer1.SetMinSize(wx.Size(434, 674))
        self.m_bitmap2 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"../venv/jiange2.jpg", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.Size(-1, 300), 0)
        bSizer1.Add(self.m_bitmap2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer1.AddSpacer(5)

        username_main = wx.BoxSizer(wx.HORIZONTAL)

        username_main.SetMinSize(wx.Size(400, 30))
        self.username = wx.StaticText(self, wx.ID_ANY, u"用户名：", wx.DefaultPosition, wx.Size(70, -1), 0)
        self.username.Wrap(-1)
        username_main.Add(self.username, 0, wx.ALL, 5)

        self.username_maintext = wx.TextCtrl(self, wx.ID_ANY, u"请输入管理员邮箱", wx.DefaultPosition, wx.Size(300, -1), 0)
        username_main.Add(self.username_maintext, 0, wx.ALL, 5)

        bSizer1.Add(username_main, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer1.AddSpacer(100)

        password_main = wx.BoxSizer(wx.HORIZONTAL)

        password_main.SetMinSize(wx.Size(400, 30))
        self.password = wx.StaticText(self, wx.ID_ANY, u"密码：", wx.DefaultPosition, wx.Size(70, -1), 0)
        self.password.Wrap(-1)
        password_main.Add(self.password, 0, wx.ALL, 5)

        self.password_maintext = wx.TextCtrl(self, wx.ID_ANY, u"12345", wx.DefaultPosition, wx.Size(300, -1), wx.TE_PASSWORD)
        password_main.Add(self.password_maintext, 0, wx.ALL, 5)

        bSizer1.Add(password_main, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer1.AddSpacer(100)

        le_main = wx.BoxSizer(wx.HORIZONTAL)

        le_main.SetMinSize(wx.Size(300, 50))
        self.login_button = wx.Button(self, wx.ID_ANY, u"登录", wx.DefaultPosition, wx.DefaultSize, 0)
        self.login_button.SetDefault()
        le_main.Add(self.login_button, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        le_main.AddSpacer(100)

        self.register_button = wx.Button(self, wx.ID_ANY, u"注册", wx.DefaultPosition, wx.DefaultSize, 0)
        le_main.Add(self.register_button, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer1.Add(le_main, 1, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.username_maintext.Bind(wx.EVT_TEXT, self.login_username)
        self.password_maintext.Bind(wx.EVT_TEXT, self.login_password)
        self.login_button.Bind(wx.EVT_BUTTON, self.login_in)
        self.register_button.Bind(wx.EVT_BUTTON, self.register)

    def __del__(self):
        pass

    def login_username(self, event):
        event.Skip()

    def login_password(self, event):
        event.Skip()

    # Virtual event handlers, overide them in your derived class
    def login_in(self, event):

        login_user = str()
        login_user += self.username_maintext.GetValue() + ' '
        login_user += self.password_maintext.GetValue()
        login_user = login_user.split(' ')
        self.load_admin(login_user)
        if len(self.admininfo) !=0:
            user_pw = self.admininfo[0][2]
            if login_user[1] == user_pw:
                app = wx.App()

                main_win = serverui_main.readserverui_main(None)
                main_win.Show()
                self.Destroy()
                app.MainLoop()
            else:
                app = wx.App()

                main_win = serverui_loginlose.login_flose(None)
                main_win.Show()
                app.MainLoop()
        else:
            app = wx.App()

            main_win = serverui_loginlose1.login_flose1(None)
            main_win.Show()
            app.MainLoop()


    def register(self, event):
        app = wx.App()

        main_win = serverui_register.readserverui_register(None)
        main_win.Show()
        app.MainLoop()

    def load_admin(self,login_user):
        db = pymysql.connect(host='localhost',
                             user='root', password='xy199491314',
                             database='readbooks', charset='utf8')

        cur = db.cursor()
        cur.execute('select * from admin_info where admin_email = %s',login_user[0])

        self.admininfo =list(cur.fetchall())
        cur.close()
        db.close()






