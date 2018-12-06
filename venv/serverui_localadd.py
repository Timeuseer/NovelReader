# -*- coding: utf-8 -*-



import wx
import wx.xrc
import serverui_laddlose
import shutil
import re
import time
import pymysql

global err,tr
err = str()
tr = str()

class local_addbook(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"本地添加图书", pos=wx.DefaultPosition, size=wx.Size(508, 420),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer23 = wx.BoxSizer(wx.VERTICAL)

        bSizer23.SetMinSize(wx.Size(323, 455))
        self.m_bitmap5 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"../venv/jiange1.jpg", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.Size(-1, 150), 0)
        bSizer23.Add(self.m_bitmap5, 0, 0, 5)

        bSizer23.AddSpacer(10)

        bSizer24 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText18 = wx.StaticText(self, wx.ID_ANY, u"选择图书：", wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.m_staticText18.Wrap(-1)
        self.m_staticText18.SetFont(wx.Font(11, 74, 90, 92, False, wx.EmptyString))

        bSizer24.Add(self.m_staticText18, 0, wx.ALL, 5)

        self.addbook_file = wx.FilePickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*",
                                              wx.DefaultPosition, wx.Size(500, -1), wx.FLP_DEFAULT_STYLE)
        self.addbook_file.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_APPWORKSPACE))
        self.addbook_file.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_APPWORKSPACE))

        bSizer24.Add(self.addbook_file, 0, 0, 5)

        bSizer23.Add(bSizer24, 0, 0, 5)

        bSizer23.AddSpacer(10)

        bSizer241 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText182 = wx.StaticText(self, wx.ID_ANY, u"选择图片：", wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.m_staticText182.Wrap(-1)
        self.m_staticText182.SetFont(wx.Font(11, 74, 90, 92, False, wx.EmptyString))

        bSizer241.Add(self.m_staticText182, 0, wx.ALL, 5)

        self.addbook_image = wx.FilePickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*",
                                               wx.DefaultPosition, wx.Size(500, -1), wx.FLP_DEFAULT_STYLE)
        self.addbook_image.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_APPWORKSPACE))
        self.addbook_image.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_APPWORKSPACE))

        bSizer241.Add(self.addbook_image, 0, 0, 5)

        bSizer23.Add(bSizer241, 0, 0, 5)

        bSizer23.AddSpacer(10)

        bSizer26 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText181 = wx.StaticText(self, wx.ID_ANY, u"图书作者：", wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.m_staticText181.Wrap(-1)
        self.m_staticText181.SetFont(wx.Font(11, 74, 90, 92, False, wx.EmptyString))

        bSizer26.Add(self.m_staticText181, 0, wx.ALL, 5)

        self.addbook_auther = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(500, -1), 0)
        bSizer26.Add(self.addbook_auther, 0, 0, 5)

        bSizer23.Add(bSizer26, 0, 0, 5)

        bSizer23.AddSpacer(10)

        bSizer261 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1811 = wx.StaticText(self, wx.ID_ANY, u"图书类型：", wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.m_staticText1811.Wrap(-1)
        self.m_staticText1811.SetFont(wx.Font(11, 74, 90, 92, False, wx.EmptyString))

        bSizer261.Add(self.m_staticText1811, 0, wx.ALL, 5)

        self.addbook_type = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(500, -1), 0)
        bSizer261.Add(self.addbook_type, 0, 0, 5)

        bSizer23.Add(bSizer261, 0, 0, 5)

        bSizer23.AddSpacer(10)

        self.m_button16 = wx.Button(self, wx.ID_ANY, u"上传图书", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer23.Add(self.m_button16, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(bSizer23)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.addbook_file.Bind(wx.EVT_FILEPICKER_CHANGED, self.book_file)
        self.addbook_image.Bind(wx.EVT_FILEPICKER_CHANGED, self.book_image)
        self.addbook_auther.Bind(wx.EVT_TEXT, self.book_auther)
        self.addbook_type.Bind(wx.EVT_TEXT, self.book_type)
        self.m_button16.Bind(wx.EVT_BUTTON, self.book_upload)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def book_file(self, event):
        event.Skip()

    def book_image(self, event):
        event.Skip()

    def book_auther(self, event):
        event.Skip()

    def book_type(self, event):
        event.Skip()

    def book_upload(self, event):
        global err,tr
        book_info = str()
        book_info += self.addbook_file.GetPath() + ' '
        book_info += self.addbook_image.GetPath() + ' '
        book_info += self.addbook_auther.GetValue() + ' '
        book_info += self.addbook_type.GetValue()
        book_info = book_info.split(' ')

        if book_info[0] !='' and book_info[1] !=''and book_info[2] !=''and book_info[3] !='':
            bookn = re.findall(r'\w+',book_info[0])
            booki = re.findall(r'\w+',book_info[1])
            if bookn[-1] =='txt' and booki[-1] =='jpg':
                self.book_copy(book_info)
                tr = '上传图书成功'
                err = ''
                self.ladd_sql(book_info)
                app = wx.App()

                main_win = serverui_laddlose.ladd_lose(None)
                main_win.Show()
                app.MainLoop()
            else:
                tr = '上传图书失败'
                err = '请选择正确的图书信息！\n图书文件必须为.txt\n图书图片必须为.jpg'
                app = wx.App()

                main_win = serverui_laddlose.ladd_lose(None)
                main_win.Show()
                app.MainLoop()

        else:
            err = '请输入完整的图书信息！'
            app = wx.App()

            main_win = serverui_laddlose.ladd_lose(None)
            main_win.Show()
            app.MainLoop()

    def book_copy(self,book_info):
        global err
        try:
            url_name = re.findall(r'\w+',book_info[0])
            self.book_name = url_name[-2]
            url_name = url_name[-2]+'.'+url_name[-1]
            local_url='../books/book/'

            self.bookn_url = local_url+url_name
            shutil.copy2(book_info[0],local_url+url_name)

            url_image = re.findall(r'\w+', book_info[1])
            url_image = url_image[-2] + '.' + url_image[-1]
            local_url2 = '../books/image/'

            self.booki_url = local_url2 + url_image
            shutil.copy2(book_info[1], local_url2 + url_image)
        except Exception as e:
            err = e

    def ladd_sql(self,book_info):
        global err,tr
        try:
            db = pymysql.connect(host='localhost',
                                 user='root', password='xy199491314',
                                 database='readbooks', charset='utf8')

            cur = db.cursor()
            judg = cur.execute('select * from book_info where book_name = "%s" and book_auther = "%s"'%(self.book_name,book_info[2]))
            if judg == 0:
                cur.execute('insert into book_info values\
                                                (0,"%s","%s","%s","%s","%s","%s")' % (
                self.book_name, book_info[2], self.bookn_url, self.booki_url,book_info[3],time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
            else:
                cur.execute('update book_info set book_url = "%s",book_image = "%s"\
                    ,book_type = "%s",book_dwtm = "%s"where book_name = "%s" and book_auther ="%s"' %(self.bookn_url, self.booki_url,book_info[3],time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),self.book_name, book_info[2]))

            db.commit()
            cur.close()
            db.close()
        except Exception as e:
            tr = '上传图书失败'
            err = e






