#Python�еļ̳�
from UserDict import UserDict

class FileInfo(UserDict):
    "store files metadata"
    def __init__(self,filename = None):
        UserDict.__init__(self)    #ע1
        self["name"]= filename
'''
����� FileInfo �̳���UserDict����.
�� Python �У���ļ̳�ֻ�Ǽ򵥵��������������С����������� Java ����һ��������� extends �Ĺؼ��֡�
Python ֧�ֶ��ؼ̳С������������С�����У�������г��������Ҫ���������Զ��ŷָ���

__init__ �����ʵ���������������á� ����java�еĹ��캯��

ϰ���ϣ��κ� Python �෽���ĵ�һ���������Ե�ǰʵ�������ã������� self��
������������� C++ �� Java �еı����� this �Ľ�ɫ���� self �� Python �в�����һ�������֣���ֻ��һ������ϰ�ߡ�
��Ȼ��ˣ�Ҳ����� self ֮�ⲻҪʹ�����������֣�����һ���ǳ���̵�ϰ�ߡ�


ע1��������java�кܴ�ͬ��
��java�У��������ͻ��Զ�ִ�и��������Ĺ��췽��
��python�У�������ʾ�ص����ڸ����е��ʺϷ������������еĹ���__init__�������ᱻִ��
'''