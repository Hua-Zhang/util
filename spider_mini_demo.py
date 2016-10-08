#-*-coding:utf8-*-
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import requests
import json
import sys
import socket
import urllib2

reload(sys)
sys.setdefaultencoding('gbk')

def getHtml(url):
#    data = None
    try:
        page = urllib2.urlopen(url,timeout=10)
        data = page.read()
    except socket.timeout, e:
        data = None
        print "time out!"
        with open("timeout",'a') as log:
            log.write(url+'\n')
    except urllib2.URLError,ee:
        data = None
        print "%s error" %(url)
    finally:
        return data

def spider(url):
    html = getHtml(url)
    if(html != None):
        selector = etree.HTML(html)
#        title = selector.xpath('//*[@id="name"]/h1/text()')
        content_field = selector.xpath('//*[@id="newsContent"]/p/text()')
#        f.writelines(title+'\n')
        print url
        for each in content_field:
           each = each.decode('gbk').encode('utf-8')
           print each
#            f.writelines(each+'\t')
#        f.writelines("###########################################################\n")
#        f1.writelines(html+'\n')
if __name__ == '__main__':
    pool = ThreadPool(20)
    f = open('content.txt','w')
    f1 = open('all.txt','w')
    page = []
    for i in range(11990700,11990800):
			newpage = 'http://www.ehuzhu.com/ehuzhu2/choujianghongbao/common.do?vm=plan/plan-web-view-information-center-newDetail&infoId='+str(i)
#        spider(newpage)
        page.append(newpage)
	
    results = pool.map(spider,page)
    pool.close()
    pool.join()
    f.close()
