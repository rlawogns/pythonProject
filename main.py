import SaveNews
import os
import DataComparison

while True:
    print("1 : 공지사항 읽음으로 변경\n2 : 전체 새 공지사항 출력")
    a=input("\n")
    if a=='1':
        SaveNews.news() #저장
        print("저장완료")
    elif a=='2':
        DataComparison.datacompare()   #출력
        print("출력완료")
    else :
        break
