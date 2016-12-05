#-*-coding:utf-8 -*-

import urllib
import urllib2
import cookielib

filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
            'funcNo':'1106104',
            'mobile':'18675341112',
            'password':'d71d2cb97280a17a0ee06768f570347cdddbcbacc7ff38fa72d77cc6b531809e61f2a79a0a733f794e342edb75e06ce3977b2864df24f33dfdc61cf938e468c83fcb1cf1a30337d26faeeceba92e34f9dbe34e996e5c1011f9ec219734ebc5e6ac2ca6b9b0c60646560d2451b341e50875ceb2f1d907467caca9c5431712f042'
        })
#登录
loginUrl = 'http://218.17.161.51:32995/servlet/json'
#模拟登录，并把cookie保存到变量
result = opener.open(loginUrl,postdata)
print result.read() 

#保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)
#利用cookie请求访问另一个网址，此网址是成绩查询网址
gradeUrl = 'http://218.17.161.51:32995/servlet/json?funcNo=1106700'
#请求访问成绩查询网址
result = opener.open(gradeUrl)
print result.read()  