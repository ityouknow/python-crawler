import urllib.request,socket,re,sys,os

baseUrl='http://cl.oiee.biz/'

def getContant(Weburl):
    Webheader= {'Upgrade-Insecure-Requests':'1',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36',}
    req = urllib.request.Request(url = Weburl,headers=Webheader)
    respose = urllib.request.urlopen(req)
    _contant = respose.read()
    respose.close()
    return str(_contant)

def getUrl(URL):
    pageIndex = 1
    for i in range(1,int(pageIndex)+1):
        Weburl = URL + str(i)
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
        
URL = baseUrl+'thread0806.php?fid=16&search=&page='
UrlList = getUrl(URL) 
print(UrlList)