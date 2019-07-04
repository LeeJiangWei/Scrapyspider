from scrapy import cmdline


name = 'ark'
cmd = f'scrapy crawl {name}'
cmdline.execute(cmd.split())