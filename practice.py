# 터미널에서 실행 명령어 python3 practice.py
"""
다중 주석 처리 방법
"""
# 한줄 주석 처리 방법

# 메뉴얼 및 검색 하는곳 
"""

인터넷에 파이썬 검색 후 
https://www.python.org/doc/
-> Documentation -> Python 3.x Resources 내용에 
-> Browse Python 3.12.0 Documentation - (Module Index) 클릭 
https://docs.python.org/3/ 이동되는 페이지 (왼쪽 상단에 언어 변경 가능)

Tutorial 클릭 -> https://docs.python.org/3/tutorial/index.html 튜토리얼
Library Reference 클릭 -> https://docs.python.org/3/library/index.html 라이브러리 부터 확인

Language Reference 클릭 -> https://docs.python.org/3/reference/index.html 파이썬 문법에 대한 설명
(나중에 심화로 참고)

모든건 검색해서 찾거나 챗GPT 활용하는것도 좋음
"""

# https://wikidocs.net/book/2 추가 참고 주소 

"""
# https://wikidocs.net/77 
import 모듈 
-> 모듈에 전체을 가져오는 방법
from 모듈 import 이름
-> from importlib import reload 형식으로 모듈내에 필요한것만 가져오는 방법

* 주의점 : 불러온 모듈에 이름과 겹치게 되면 다른게 출력이되거나 이상해 질수 있음 *
"""

from math import * # 수학 모듈
from random import * # 랜덤 모듈

## 숫자형 데이터 타입
# str()는 문자형으로 변경
print("abs : " + str( abs(-5) )) # 절대값
print("abs :", abs(-5)) # 절대값
print("pow : " , pow(4,2)) # 제곱 
print("max : " , max(5,12)) # 가장 큰 값을 골라주는 함수
print("min : " , min(5,12)) # 가장 큰 값을 골라주는 함수

print("round : " , round(3.14)) # 반올림 함수
print("round : " , round(4.99)) # 반올림 함수


print(floor(4.99)) # 내림
print(ceil(3.14)) # 올림
print(sqrt(16)) # 제곱근

print("random", random() * 10)
print("random.randrange", randrange(1,10))

## 문자열 데이터 타입 
print('Hello world')
print("Hello world")

# 줄바꿈을 처리
print(""" 
Hello world1
Hello world2
Hello world3
Hello world4
""")

## 리스트 데이터 타입
import statistics
students = ["egoing","sori","maru"]
grades = [2,1,4]
print("students[1]", students[1]) # sori
print("len(students)", len(students)) # 3
print("max(grades)" , max(grades)) # 4
print("min(grades)" , min(grades)) # 1
print("sum(grades)" , sum(grades)) # 7
print("statistics.mean(grades)" , statistics.mean(grades)) # 2.3333333333333335

## 변수
name = "이름"
print("hello "+name+" ...." + name)

## 디버깅 (개발 단계 중에 발생하는 시스템의 논리적인 오류나 비정상적 연산(버그)을 찾아내고 수정하는 작업 과정)
"""
1. print()를 사용해서 중간에 출력을 해서 확인 해보는 방법
2. 디버거(debug)
   -> VSCODE사용법 왼쪽 탭들중에 [Run and  Debug] 클릭해서 사용
"""

## 입력과 출력
name = input('name: ') # 실행 후 해당 부분에 입력을 하면 출력이 되는 코드
message = "hi,"+name+".... bye, "+name+","
print(message)

## pypi - https://pypi.org/
# 확인 시 상단에 설치 명령어 pip install pandas
# 설치 시 명령어 'python3 -m pip install pandas'

import pandas
house = pandas.read_csv('house.csv')
print(house) # 액셀에 정보를 csv로 만들어서 출력
print(house.head(2)) # 맨상단에 2개만 노출
print(house.describe()) # 해당 정보에 요약점을 출력 (카운트, min, max 등등)