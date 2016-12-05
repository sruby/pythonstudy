# import urllib2  
# response = urllib2.urlopen("http://www.baidu.com")
# print response.read()

# Requset
# import urllib2
# request = urllib2.Request("http://www.baidu.com")
# response = urllib2.urlopen(request)
# print response.read()  


# with parameter
# import urllib
# import urllib2
# values = {"username":"1016903103@qq.com","password":"XXXX"}
# data = urllib.urlencode(values) 
# url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
# request = urllib2.Request(url,data)
# response = urllib2.urlopen(request)
# print response.read()  

 # with headers
import urllib  
import urllib2  
url = 'https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  
values = {'username' : 'cqc',  'password' : 'XXXX' }  
headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  ,
                        'Referer':'http://www.zhihu.com/articles' }  
data = urllib.urlencode(values)  
request = urllib2.Request(url, data, headers)  
response = urllib2.urlopen(request)  
page = response.read()   

# proxy
# import urllib2
# enable_proxy = True
# proxy_handler = urllib2.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
# null_proxy_handler = urllib2.ProxyHandler({})
# if enable_proxy:
#     opener = urllib2.build_opener(proxy_handler)
# else:
#     opener = urllib2.build_opener(null_proxy_handler)
# urllib2.install_opener(opener)  