#urllister.py
from sgmllib import SGMLParser

class URLLister(SGMLParser):
    def reset(self):
        '''
        reset由SGMLParser 的__init__方法来调用，也可以在创建一个分析器实例时手工来调用。
        如果您需要做初始化。
        '''        
        SGMLParser.reset(self)
        self.urls = []

    def start_a(self.attrs):
        href = [v for k,v in attrs if k == 'href']
        if href:
            self.urls.extend(href)