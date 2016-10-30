'''
批量下载1204图片

1024导航网站http://1024bug.me/
'''
import urllib.request,socket,re,sys,os

baseUrl='http://cl.oiee.biz/'
targetPath = "D:\\temp\\1024\\"

def getContant(Weburl):
    Webheader= {'Upgrade-Insecure-Requests':'1',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36',}
    req = urllib.request.Request(url = Weburl,headers=Webheader)
    respose = urllib.request.urlopen(req)
    _contant = respose.read()
    respose.close()
    return str(_contant)

def getUrl(URL):
    #pageIndex = input("要下载多少页呢？\n")
    pageIndex = 1
    for i in range(1,int(pageIndex)+1):
        Weburl = URL + str(i)#获取每大页的URL
        contant = getContant(Weburl)
        comp = re.compile(r'<a href="htm_data.{0,30}html" target="_blank" id=""><font color=g')
        urlList1 = comp.findall(contant)
        comp = re.compile(r'a href="(.*?)"')
        urlList2 = comp.findall(str(urlList1))
        urlList = []
        for url1 in urlList2:
            url2 = baseUrl+url1
            urlList.append(url2)
        return urlList

def openUrl(url):
    headers = {
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '                            'Chrome/51.0.2704.63 Safari/537.36'
               }

    filePath=targetPath+url[-12:-5]
    #检测当前路径的有效性
    if not os.path.isdir(filePath):
        os.mkdir(filePath)
        req = urllib.request.Request(url=url, headers=headers)
        res = urllib.request.urlopen(req)
        data = res.read()
        downImg(data,filePath)
    else:
        print("已经下载过的地址跳过："+url)
        print("filePath  "+filePath)

def downImg(data,filePath):
    for link,t in set(re.findall(r'([http|https]:[^\s]*?(jpg|png|gif))', str(data))):

        if link.startswith('s'):
            link='http'+link
        else:
            link='htt'+link
        print(link)
        try:
            opener=urllib.request.build_opener()
            opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(link,saveFile(link,filePath))
        except:
            print('失败')

def saveFile(path,filePath):
    #设置每个图片的路径
    pos = path.rindex('/')
    t = os.path.join(filePath,path[pos+1:])
    return t


def openPage(UrlList):
    for pageUlr in UrlList:
        try:
            print('正在下载地址：'+pageUlr)
            openUrl(pageUlr)
        except:
            print('地址：'+pageUlr+'下载失败')

URL = baseUrl+'thread0806.php?fid=16&search=&page='
for num in range(0,20):
    print("#######################################")
    print("##########总目录下载地址#############################")
    print(URL+str(num))
    print("#######################################")
    print("#######################################")
    UrlList = getUrl(URL+str(num)) 
    openPage(UrlList)


