# -*- coding: utf-8 -*-



import wx
import wx.xrc
import urllib
import urllib.request
import re
import serverui_downbook
import pymysql
import time
import requests


global s,booku_info
s = list()
booku_info = list()


class url_addbook(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"从网上爬取小说", pos=wx.DefaultPosition, size=wx.Size(340, 312),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer33 = wx.BoxSizer(wx.VERTICAL)

        self.m_bitmap6 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"../venv/jiange3.jpg", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.Size(-1, 150), 0)
        bSizer33.Add(self.m_bitmap6, 0, 0, 5)

        bSizer33.AddSpacer(10)

        self.m_staticText26 = wx.StaticText(self, wx.ID_ANY, u"输入小说主页的网络地址", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText26.Wrap(-1)
        bSizer33.Add(self.m_staticText26, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.book_url = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer33.Add(self.book_url, 0, wx.ALL | wx.EXPAND, 5)

        self.down_book = wx.Button(self, wx.ID_ANY, u"下载图书", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer33.Add(self.down_book, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(bSizer33)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.book_url.Bind(wx.EVT_TEXT, self.url_book)
        self.down_book.Bind(wx.EVT_BUTTON, self.book_dw)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def url_book(self, event):
        event.Skip()

    #小说下载
    def book_dw(self, event):
        global s,booku_info
        event.Skip()
        url = self.book_url.GetValue()  # 获取小说主页网址(章节目录页)
        if url:  # 从输入框获取到小说主页网址后，判断其是否为“www”开头，是的话给其添加头部"http://"
            if url[0:3] == "www":
                url = urlcat("https://", url)
            try:
                spider = BQG()
                spider.start(url)

            except Exception as e:
                s.append(e)
            finally:
                self.booku_sql()
                booku_info = []
                self.Destroy()
                app = wx.App()
                main_win = serverui_downbook.down_book(None)
                s = []
                main_win.Show()
                app.MainLoop()



        else:
            app = wx.App()
            s.append(u"请输入合理的网址")
            main_win = serverui_downbook.down_book(None)
            main_win.Show()
            app.MainLoop()

    #将小说信息写入数据库
    def booku_sql(self):
        global s
        try:
            print(booku_info)
            booku_url = '../books/book/' + booku_info[0] + ".txt"
            db = pymysql.connect(host='localhost',
                                 user='root', password='xy199491314',
                                 database='readbooks', charset='utf8')

            cur = db.cursor()
            judg = cur.execute('select * from book_info where book_name = "%s" and book_auther = "%s"' % (booku_info[0], booku_info[1]))
            if judg == 0:
                cur.execute('insert into book_info values\
                        (0,"%s","%s","%s","%s","%s","%s")' % (booku_info[0], booku_info[1], booku_url, booku_info[3], booku_info[2],
                            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
            else:
                cur.execute('update book_info set book_url = "%s",book_image = "%s"\
                         ,book_type = "%s",book_dwtm = "%s" where book_name = "%s" and book_auther ="%s"' % (
                            booku_url, booku_info[3], booku_info[2],time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                            booku_info[0], booku_info[1]))

            db.commit()
            cur.close()
            db.close()
        except Exception as e:
            print(e)
            s.append(e)





# --------------------------------------------------------------爬取-----------------------------------------------------------
#从代理网站获取一系列的代理，每次随机用一个代理，并获取这个代理IP的完整信息
def AgentIp():
    agent_url = 'http://www.xicidaili.com/'
    user_agent='Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'
    header = {'User-Agent': user_agent}
    request = urllib.request.Request(agent_url, headers = header)
    response = urllib.request.urlopen(request)
    pageCode = response.read().decode('utf-8')
    pattern = re.compile('<td class="country"><img.*?/></td>.*?<td>(.*?)</td>.*?>高匿</td>', re.S)
    host = re.search(pattern, pageCode)[1]
    pattern_1 = re.compile('<td class="country"><img.*?/></td>.*?<td>' + host + '</td>.*?<td>(.*?)</td>.*?>高匿</td>',
                           re.S)
    port = re.findall(pattern_1, pageCode)[0]
    pattern_1 = re.compile(
        '<td class="country"><img.*?/></td>.*?<td>' + host + '</td>.*?<td>' + port + '</td>.*?>高匿</td>.*?<td>(.*?)</td>',
        re.S)
    htp = re.findall(pattern_1, pageCode)[0]
    host_port = host + ':' + port
    ip = {htp: host_port}
    if host and port and htp:
        return ip
    return None

#判断输入的链接是否符合规范
def urlcat(head, tail):
    cnt = len(head) # 获取头部长度
    index = 0
    flag = True
    while flag:
        if head.rfind(tail[0:index]) != -1: #查看相同部分的大小
            index += 1
        else:
            flag = False
        if index >= cnt:
            flag = False

    #返回链接后的地址
    if index > 0:
        return (head + tail[index-1::])
    else:
        return head + tail



class BQG:
    def __init__(self):
        self.agentIP = AgentIp()  # 代理IP网址"113.118.94.140"
        self.file = None    # 用于保存下载的小说--txt格式
        self.bookName = 'test'   # 小说名
        self.mainurl = ''
        self.headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'}


    def openFile(self, filename):
        file = open(filename, 'r+')
        if file:
            return file
        return None


    #使用高匿爬取小说首页的信息
    def getPage_proxy(self, url):
        proxy = self.agentIP
        proxy_support = urllib.request.ProxyHandler(proxy)
        opener = urllib.request.build_opener(proxy_support)
        opener.addheaders = [('User-agent','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36')]
        urllib.request.install_opener(opener)
        response = urllib.request.urlopen(url)
        pageCode = response.read().decode("utf-8")
        return pageCode

    #获取所下载小说对应的信息：作者、类型、小说名、小说图片
    def getBookName(self, pageCode):
        global s,booku_info

        pattern = re.compile('<h1>(.*?)</h1>', re.S)
        bookName = re.findall(pattern, pageCode)

        pattern2 = re.compile('<h1>.*?</h1>.*?<p>(.*?)</p>', re.S)
        bookAuther = re.findall(pattern2, pageCode)
        bookAuther = re.findall(r"\w+", bookAuther[0])[-1]

        pattern3 = re.compile('&gt; (.*?)&gt', re.S)
        bookTy = re.findall(pattern3, pageCode)
        pattern33 = re.compile('<a href=".*">(.*?)</a>', re.S)
        bookType = re.findall(pattern33, bookTy[0])[-1]

        pattern4 = re.compile(
            '<div id=".*?">.*?<img alt=".*?" src="(.*?)".*?</div>', re.S)
        Image_url = re.findall(pattern4, pageCode)[-1]
        bookImage = self.WriteImage(Image_url)

        booku_info.append(bookName[-1])
        booku_info.append(bookAuther)
        booku_info.append(bookType)
        booku_info.append(bookImage)


        if bookName:
            print("\n\n准备下载小说:\t%s\n"%(bookName[0].strip()))
            s.append("\n\n准备下载小说:\t%s\n"%(bookName[0].strip()))
            self.bookName = bookName[0].strip()

    #下载小说图片
    def WriteImage(self,url):
        res = requests.get(url, headers=self.headers)
        res.encoding = "utf-8"
        html = res.content
        # filename
        filename = '../books/image/'+url[-10:]
        with open(filename, "wb") as f:
            f.write(html)
            time.sleep(0.5)
            print("%s小说图片下载成功" % filename)

        return filename

    #获取每一章的内容，并去掉里面不需要的字符
    def getOneChapterContent(self, chapterurl):
        pageCode = self.getPage_proxy(chapterurl.strip())
        if pageCode == None:
            return None
        pattern = re.compile('<div id="content".*?>.*?nbsp;(.*?)</div>', re.S)
        content = re.findall(pattern, pageCode)
        if content:
            pp = re.compile('<br />')
            text = re.sub(pp, "\n", content[0])
            pp = re.compile('&nbsp;')
            text = re.sub(pp, " ", text)
            return text
        print("none")
        return ''


    #获得该小说的所有章节名和对应链接
    def getChapters(self, pageCode):
        global s
        pattern = re.compile('<dd>.*?<a href="(.*?)">(.*?)</a></dd>', re.S)
        chapters = re.findall(pattern, pageCode)
        if chapters:
            filename ='../books/book/' + self.bookName + ".txt"
            print("创建小说文件:\t%s"%filename)
            s.append("创建小说文件:\t%s"%filename)
            file = open(filename, 'w')
            if file:
                print("\n=================== 依次下载各章节内容 ===================\n")
                s.append("\n==依次下载各章节内容==\n")
                for chapter in chapters:
                    print("获取章节：\t%s"%(chapter[1]))#chapter[0]--章节链接 chapter[1]--章节名
                    s.append("获取章节：\t%s"%(chapter[1]))
                    file.write('\n\n' + chapter[1] + '\n\n')
                    real_url = chapter[0].strip()

                    # 判断是否是最后一章的链接，并修改最后一章链接的格式
                    if real_url[-4:] != 'html':
                        pattern = re.compile('(.*?\Whtml).*?', re.S)
                        real_url = re.findall(pattern, real_url)[0].strip()
                    #补全链接
                    if real_url[0] == '/':
                        real_url = urlcat(self.mainurl, real_url)
                    text = self.getOneChapterContent(real_url)
                    file.write(text)
                file.close()
            else:
                print("文件创建or打开失败")
                s.append("文件创建or打开失败")


    #开始小说爬取
    def start(self, bqg_url):
        global s
        self.mainurl = bqg_url
        pageCode = self.getPage_proxy(bqg_url)
        self.getBookName(pageCode)
        self.getChapters(pageCode)
        print("\n已下载完成，退出！\n")
        s.append("\n已下载完成，退出！\n")









