from urllib.request import urlopen
from bs4 import BeautifulSoup
def news():
    f = open("D:\PyCharm Community Edition 2020.3.3\pythonProject\저장파일.txt", 'w')
    html = urlopen("https://computer.cnu.ac.kr/computer/notice/bachelor.do")
    bs = BeautifulSoup(html, "html.parser")
    tags=bs.select("tbody > tr > td > div > a")
    for tag in tags:
        f.write(tag.get('title') + "\n")
    f.write("--------------------------------------------------------------------\n")
    html = urlopen("https://computer.cnu.ac.kr/computer/notice/notice.do")
    bs = BeautifulSoup(html, "html.parser")
    tags=bs.select("tbody > tr > td > div > a")
    for tag in tags:
        f.write(tag.get('title') + "\n")
    f.write("--------------------------------------------------------------------\n")
    html = urlopen("https://computer.cnu.ac.kr/computer/notice/project.do")
    bs = BeautifulSoup(html, "html.parser")
    tags=bs.select("tbody > tr > td > div > a")
    for tag in tags:
        f.write(tag.get('title') + "\n")
    f.write("--------------------------------------------------------------------\n")
    html = urlopen("https://computer.cnu.ac.kr/computer/notice/job.do")
    bs = BeautifulSoup(html, "html.parser")
    tags=bs.select("tbody > tr > td > div > a")
    for tag in tags:
        f.write(tag.get('title') + "\n")
    f.close()
"""def news():
    f = open("D:\PyCharm Community Edition 2020.3.3\pythonProject\저장파일.txt", 'w')
    html = urlopen("https://computer.cnu.ac.kr/computer/notice/bachelor.do")
    bs = BeautifulSoup(html, "html.parser")
    tags=bs.select("tbody > tr > td > div > a")
    n=1
    for tag in tags:
        n+=1
        print(tag.get('title') , n)"""