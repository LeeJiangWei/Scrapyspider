from scrapy import cmdline


name = 'ark'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())