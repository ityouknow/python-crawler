'''
批量下载图片

采用伪装浏览器的方式爬取豆瓣网站首页的图片，保存到指定路径文件夹下
'''

#导入所需的库
import urllib.request,socket,re,sys,os

#定义文件保存路径
targetPath = "D:\\temp\\1024\\1"

def openUrl(url):
	headers = {
	              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '                            'Chrome/51.0.2704.63 Safari/537.36'
	           }

	req = urllib.request.Request(url=url, headers=headers)
	res = urllib.request.urlopen(req)
	data = res.read()
	downImg(data)

def downImg(data):
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
	        urllib.request.urlretrieve(link,saveFile(link))
	    except:
	        print('失败')

def saveFile(path):
    #检测当前路径的有效性
    if not os.path.isdir(targetPath):
        os.mkdir(targetPath)

    #设置每个图片的路径
    pos = path.rindex('/')
    t = os.path.join(targetPath,path[pos+1:])
    return t


url = "http://cl.oiee.biz/htm_data/16/1611/2115193.html"
openUrl(url)