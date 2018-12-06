# -*- coding: utf-8 -*-



import wx
import wx.xrc
import pymysql
import re
import server_readbook
import serverui_main


class readBook(wx.Frame):
    bookName = str()
    ChaContent = list()
    bookTitle = list()

    def __init__(self, parent):
        self.load_book()
        book_len = len(self.bookinfo)
        if book_len % 2 == 0:
            lay_len = book_len // 2
        else:
            lay_len = book_len // 2 + 1
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"图书阅读", pos=wx.DefaultPosition, size=wx.Size(555, 766),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.Size(555, 766), wx.Size(555, 766))

        bSizer42 = wx.BoxSizer(wx.VERTICAL)

        bSizer42.SetMinSize(wx.Size(555, 766))
        self.m_scrolledWindow4 = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                   wx.HSCROLL | wx.VSCROLL)
        self.m_scrolledWindow4.SetScrollRate(5, 5)
        bSizer43 = wx.BoxSizer(wx.VERTICAL)
        btnList = []
        y = 0
        for x in range(0,lay_len):
            if y < book_len:
                bSizer44 = wx.BoxSizer(wx.HORIZONTAL)
                m_bpButton1 = wx.BitmapButton(self.m_scrolledWindow4, wx.ID_ANY,
                                                    wx.Bitmap(u""+self.bookinfo[y][4], wx.BITMAP_TYPE_ANY),
                                                    wx.DefaultPosition, wx.Size(240, 320), wx.BU_AUTODRAW)
                bSizer44.Add(m_bpButton1, 0, wx.ALL, 5)
                btnList.append(m_bpButton1)
                y +=1
                if y < book_len:
                    m_bpButton2 = wx.BitmapButton(self.m_scrolledWindow4, wx.ID_ANY,
                                                         wx.Bitmap(u""+self.bookinfo[y][4], wx.BITMAP_TYPE_ANY),
                                                         wx.DefaultPosition, wx.Size(240, 320), wx.BU_AUTODRAW)
                    bSizer44.Add(m_bpButton2, 0, wx.ALL, 5)
                    y +=1
                    btnList.append(m_bpButton2)
                bSizer43.Add(bSizer44, 1, wx.EXPAND, 5)

        self.m_scrolledWindow4.SetSizer(bSizer43)
        self.m_scrolledWindow4.Layout()
        bSizer43.Fit(self.m_scrolledWindow4)
        bSizer42.Add(self.m_scrolledWindow4, 1, wx.EXPAND | wx.ALL, 5)

        self.m_button27 = wx.Button(self, wx.ID_ANY, u"返回上一层", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer42.Add(self.m_button27, 0, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer42)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button27.Bind(wx.EVT_BUTTON, self.goback)
        num = 0
        for x in btnList:
            self.Bind(wx.EVT_BUTTON, lambda event, i=self.bookinfo[num][0]: self.goread(event, i), x)
            num += 1

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def goread(self,event,id):

        #获取所点击图书的详细内容
        bookId = str(id)
        book = self.SearchBook(bookId)
        filename = book[0][3]
        self.bookName = book[0][1]
        with open(filename, "r") as f:
            file = f.read()
        #获取图书的章节
        pattern = re.compile(
            '.*?\n(第.*?章.*?)\n',
            re.S)
        self.bookTitle = re.findall(pattern, file)
        #获取图书章节对应的内容
        self.ChaContent = []
        for x in range(0,len(self.bookTitle)-1):
            pattern = re.compile(
                self.bookTitle[x] + '.*?\n(.*?)'+self.bookTitle[x+1],
                re.S)
            self.ChaContent.append(re.findall(pattern, file))
        pattern = re.compile(
            '.*?' + self.bookTitle[-1] + '\n(.*)',
            re.S)
        self.ChaContent.append(re.findall(pattern, file))

        app = wx.App()
        main_win = server_readbook.read_book(None,bName = self.bookName,tList=self.bookTitle,cList=self.ChaContent)
        self.Destroy()
        main_win.Show()
        app.MainLoop()


    def goback(self, event):
        event.Skip()
        app = wx.App()
        main_win = serverui_main.readserverui_main(None)
        self.Destroy()
        main_win.Show()
        app.MainLoop()


    def SearchBook(self,id):
        db = pymysql.connect(host='localhost',
                             user='root', password='xy199491314',
                             database='readbooks', charset='utf8')

        cur = db.cursor()

        cur.execute('select * from book_info where book_id="%s"' %id)

        cur.close()
        db.close()

        return list(cur.fetchall())

    def load_book(self):
        db = pymysql.connect(host='localhost',
                             user='root', password='xy199491314',
                             database='readbooks', charset='utf8')

        cur = db.cursor()

        cur.execute('select * from book_info')

        self.bookinfo =list(cur.fetchall())

        cur.close()
        db.close()

