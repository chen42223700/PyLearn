#urllister.py
from sgmllib import SGMLParser

class URLLister(SGMLParser):
    def reset(self):
        '''
        reset��SGMLParser ��__init__���������ã�Ҳ�����ڴ���һ��������ʵ��ʱ�ֹ������á�
        �������Ҫ����ʼ����
        '''        
        SGMLParser.reset(self)
        self.urls = []

    def start_a(self.attrs):
        href = [v for k,v in attrs if k == 'href']
        if href:
            self.urls.extend(href)