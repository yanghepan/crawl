# Scrapy settings for jiaohang project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'jiaohang'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['jiaohang.spiders']
NEWSPIDER_MODULE = 'jiaohang.spiders'
#USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
USER_AGENT='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0'
