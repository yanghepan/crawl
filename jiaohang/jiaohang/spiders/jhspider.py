import scrapy
import urllib2
import sys
import os
import requests
import urllib
from jiaohang.secret import USERNAME,PASSWORD,YEAR,MONTH

class JiaoHangSpider(scrapy.Spider):
	name="jiaohang"
	start_urls=["http://shanghai.tsyw.bankcomm.com:8080/bankstmt"]

	def parse(self,response):
		return scrapy.FormRequest.from_response(response,
		formdata={"username":USERNAME,"password":PASSWORD},
		callback=self.after_login)

	def after_login(self,response):
		return scrapy.Request("http://shanghai.tsyw.bankcomm.com:8080/bankstmt/app/bf_download_stmt.jsp",self.after_jump)

	def after_jump(self,response):
		return scrapy.FormRequest.from_response(response,
		formdata={"year":YEAR,"month":MONTH},
		method="POST",
		url="http://shanghai.tsyw.bankcomm.com:8080/bankstmt/app/download_stmt.jsp",
		callback=self.after_link)

	def after_link(self,response):
		for item in response.xpath('//a[@class="banner"]/@href').extract():
			print item
			f=urllib2.urlopen(item)
			filename=item.split('=')[1]
			try:
				with open(filename,"wb") as code:
					code.write(f.read())
				print os.path.abspath(filename)
				print 'load suc'
			except:
				info=sys.exc_info()
				print info[0],":",info[1]
			#filename=item.split('=')[1]
			#filename=wget.download(item)
			#testfile=urllib.URLopener()
			#testfile.retrieve(item,item.split('=')[1])
