# -*- coding: utf-8 -*-


import wx
import wx.xrc
import serverui_registerlose
import serverui_registerlose1
import serverui_registerlose2
import pymysql

user_info = []

class readserverui_register(wx.Frame):

    def __init__(self, parent):
        global user_info
        user_info = []
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"管理员注册", pos=wx.DefaultPosition, size=wx.Size(434, 674),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        bSizer2.SetMinSize(wx.Size(434, 674))
        self.m_bitmap2 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"../venv/jiange3.jpg", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.Size(-1, 300), 0)
        bSizer2.Add(self.m_bitmap2, 0, 0, 5)

        bSizer2.AddSpacer(20)

        username_register = wx.BoxSizer(wx.HORIZONTAL)

        username_register.SetMinSize(wx.Size(400, 30))
        self.username = wx.StaticText(self, wx.ID_ANY, u"用户名：", wx.DefaultPosition, wx.Size(80, -1), 0)
        self.username.Wrap(-1)
        username_register.Add(self.username, 0, wx.ALL, 5)



        self.username_registertext = wx.TextCtrl(self, wx.ID_ANY, u"", wx.DefaultPosition, wx.Size(300, -1), 0)
        username_register.Add(self.username_registertext, 0, wx.ALL, 5)

        bSizer2.Add(username_register, 0, wx.ALIGN_CENTER, 5)

        bSizer2.AddSpacer(20)



        password_register = wx.BoxSizer(wx.HORIZONTAL)

        password_register.SetMinSize(wx.Size(400, 30))
        self.password = wx.StaticText(self, wx.ID_ANY, u"密码：", wx.DefaultPosition, wx.Size(80, -1), 0)
        self.password.Wrap(-1)
        password_register.Add(self.password, 0, wx.ALL, 5)

        self.password_registertext = wx.TextCtrl(self, wx.ID_ANY, u"", wx.DefaultPosition, wx.Size(300, -1), wx.TE_PASSWORD)
        password_register.Add(self.password_registertext, 0, wx.ALL, 5)

        bSizer2.Add(password_register, 0, wx.ALIGN_CENTER, 5)

        bSizer2.AddSpacer(20)

        password2_register = wx.BoxSizer(wx.HORIZONTAL)

        password2_register.SetMinSize(wx.Size(400, 30))
        self.password = wx.StaticText(self, wx.ID_ANY, u"确认密码：", wx.DefaultPosition, wx.Size(80, -1), 0)
        self.password.Wrap(-1)
        password2_register.Add(self.password, 0, wx.ALL, 5)

        self.password_registertext2 = wx.TextCtrl(self, wx.ID_ANY, u"", wx.DefaultPosition, wx.Size(300, -1),wx.TE_PASSWORD)
        password2_register.Add(self.password_registertext2, 0, wx.ALL, 5)

        bSizer2.Add(password2_register, 0, wx.ALIGN_CENTER, 5)

        bSizer2.AddSpacer(20)

        email_register = wx.BoxSizer(wx.HORIZONTAL)

        email_register.SetMinSize(wx.Size(400, 30))
        self.email = wx.StaticText(self, wx.ID_ANY, u"邮箱：", wx.DefaultPosition, wx.Size(80, -1), 0)
        self.email.Wrap(-1)
        email_register.Add(self.email, 0, wx.ALL, 5)

        self.email_registertext = wx.TextCtrl(self, wx.ID_ANY, u"", wx.DefaultPosition, wx.Size(300, -1), 0)
        email_register.Add(self.email_registertext, 0, wx.ALL, 5)

        bSizer2.Add(email_register, 0, wx.ALIGN_CENTER, 5)

        bSizer2.AddSpacer(20)

        phone_register = wx.BoxSizer(wx.HORIZONTAL)

        phone_register.SetMinSize(wx.Size(400, 30))
        self.phone = wx.StaticText(self, wx.ID_ANY, u"电话号码：", wx.DefaultPosition, wx.Size(80, -1), 0)
        self.phone.Wrap(-1)
        phone_register.Add(self.phone, 0, wx.ALL, 5)

        self.pnumber_registertext = wx.TextCtrl(self, wx.ID_ANY, u"", wx.DefaultPosition, wx.Size(300, -1),
                                                  0)
        phone_register.Add(self.pnumber_registertext, 0, wx.ALL, 5)

        bSizer2.Add(phone_register, 0, wx.ALIGN_CENTER, 5)

        bSizer2.AddSpacer(10)

        self.register_registerbutton = wx.Button(self, wx.ID_ANY, u"确认注册", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.register_registerbutton, 0, wx.ALIGN_CENTER, 5)

        self.SetSizer(bSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

        user_info +=  self.username_registertext.GetValue()
        # Connect Events
        self.username_registertext.Bind(wx.EVT_TEXT, self.in_username)
        self.password_registertext.Bind(wx.EVT_TEXT, self.in_password)
        self.password_registertext2.Bind(wx.EVT_TEXT, self.in_password2)
        self.email_registertext.Bind(wx.EVT_TEXT, self.in_email)
        self.pnumber_registertext.Bind(wx.EVT_TEXT, self.in_pnumber)
        self.register_registerbutton.Bind(wx.EVT_BUTTON, self.sure_register)

    def __del__(self):
        pass

    def in_username(self, event):
        event.Skip()

    def in_password(self, event):
        event.Skip()

    def in_password2(self, event):
        event.Skip()

    def in_email(self, event):
        event.Skip()

    def in_pnumber(self, event):
        event.Skip()

    def sure_register(self, event):
        user_info = str()
        user_info += self.username_registertext.GetValue()+' '
        user_info += self.password_registertext.GetValue()+' '
        user_info += self.password_registertext2.GetValue()+' '
        user_info += self.email_registertext.GetValue()+' '
        user_info += self.pnumber_registertext.GetValue()
        user_info = user_info.split(' ')
        self.show_admin(user_info)
        if len(self.admin_info) == 0:
            if user_info[1] == user_info[2]:
                if user_info [0] != '' and user_info[1] != '' and user_info[2] != '' and user_info[3] != '' and user_info[4] != '':
                    self.add_admin(user_info)
                    self.Destroy()

                else:
                    app = wx.App()

                    main_win = serverui_registerlose1.register_flose1(None)
                    main_win.Show()
                    app.MainLoop()

            else:
                app = wx.App()

                main_win = serverui_registerlose.register_flose(None)
                main_win.Show()
                app.MainLoop()
        else:
            app = wx.App()

            main_win = serverui_registerlose2.register_flose2(None)
            main_win.Show()
            app.MainLoop()
        print(user_info)

    def show_admin(self,user_info):
        db = pymysql.connect(host='localhost',
                             user='root', password='xy199491314',
                             database='readbooks', charset='utf8')

        cur = db.cursor()
        cur.execute('select * from admin_info where admin_email = %s', user_info[3])

        self.admin_info = list(cur.fetchall())

    def add_admin(self,user_info):
        db = pymysql.connect(host='localhost',
                             user='root', password='xy199491314',
                             database='readbooks', charset='utf8')

        cur = db.cursor()
        cur.execute('insert into admin_info values\
                                (0,"%s","%s","%s","%s")' % (user_info[0], user_info[1], user_info[3], user_info[4]))

        db.commit()
        cur.close()
        db.close()





