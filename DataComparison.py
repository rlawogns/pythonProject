from urllib.request import urlopen
from bs4 import BeautifulSoup
def datacompare():
    f = open("D:\PyCharm Community Edition 2020.3.3\pythonProject\저장파일.txt", 'r')
    pre=f.read()
    html = urlopen("https://computer.cnu.ac.kr/computer/notice/bachelor.do")
    bs = BeautifulSoup(html, "html.parser")
    tags = bs.select("tbody > tr > td > div > a")
    print("학사공지\n")
    for tag in tags:
        if(tag.get('title') not in pre):
            print(tag.get('title')+"\n")
    print("--------------------------------------------------------------------\n")
    html = urlopen("https://computer.cnu.ac.kr/computer/notice/notice.do")
    bs = BeautifulSoup(html, "html.parser")
    tags = bs.select("tbody > tr > td > div > a")
    print("일반소식\n")
    for tag in tags:
        if (tag.get('title') not in pre):
            print(tag.get('title') + "\n")
    print("--------------------------------------------------------------------\n")
    html = urlopen("https://computer.cnu.ac.kr/computer/notice/project.do")
    bs = BeautifulSoup(html, "html.parser")
    tags = bs.select("tbody > tr > td > div > a")
    print("사업단소식\n")
    for tag in tags:
        if (tag.get('title') not in pre):
            print(tag.get('title') + "\n")
    print("--------------------------------------------------------------------\n")
    html = urlopen("https://computer.cnu.ac.kr/computer/notice/job.do")
    bs = BeautifulSoup(html, "html.parser")
    tags = bs.select("tbody > tr > td > div > a")
    print("취업정보\n")
    for tag in tags:
        if (tag.get('title') not in pre):
            print(tag.get('title') + "\n")
    f.close()