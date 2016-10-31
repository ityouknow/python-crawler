
#!/usr/bin/env python2
# -*- coding: UTF-8 -*-


import url_manager, html_downloader, html_outputer, html_parser


class SpiderMain(object):

    # 初始各个对象， 其中UrlManager、HtmlDownloader、HtmlParser、HtmlOutputer四个对象需要之后创建
    def __init__(self):
        self.urls = url_manager.UrlManager()  #URL管理器
        self.downloader = html_downloader.HtmlDownloader()  # 下载器
        self.parser = html_parser.HtmlParser()   # 解析器 
        self.outputer = html_outputer.HtmlOutputer()  #输出器



    def craw(self, root_url):
        count = 1
        # 将root_url添加到url管理器
        self.urls.add_new_url(root_url)  

        # 只要添加的url里有新的url
        while self.urls.has_new_url():
            try :
                new_url = self.urls.get_new_url()
                print ('craw %d : %s' % (count, new_url))

                # 启动下载器，将获取到的url下载下来
                html_cont = self.downloader.download(new_url)

                # 调用解析器解析下载的这个页面
                new_urls, new_data = self.parser.parse(new_url, html_cont)

                # 将解析出的url添加到url管理器， 将数据添加到输出器里
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)


                if count == 1000:
                    break
                count = count + 1
            except:
                print ('craw failed')

        self.outputer.output_html()

if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"  #这个URL根据实际情况的url进行修改
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)  # 启动爬虫