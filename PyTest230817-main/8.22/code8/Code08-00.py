# SQLite 데이터베이스에 스키마 생성, 테이블 생성해서
# 파이썬 버전으로 접근해서, 데이터 게터/세터
# 크롤링 한 데이터를 임시 메모리 저장 -> 해당 디비 쓰기작업
# 특정 시간마다 입력이 되게끔 설정
# 1) cmd -> 스키마 생성 및 테이블 생성, crud
# sqlite 설치한 폴더 : c 드라이브 밑으로 이동
# 해당 폴더에 가서 샘플로 만들기
# 2) DB Browser for SQLite(워크벤치) : GUI로 간단히
# 스키마 생성 및 crud

import sqlite3
con = sqlite3.connect("C:/CookAnalysis/naverDB")
cur = con.cursor()
cur.execute(
    "CREATE TABLE userTable (id char(4), userName char(15), email char(20), birthYear int)")

cur.execute(
    "CREATE TABLE userTable (id char(4), userName char(15), email char(20), birthYear int)")

cur.execute(
    "INSERT INTO userTable VALUES('john', 'John Bann', 'john@naver.com', 1990)")
cur.execute(
    "INSERT INTO userTable VALUES('kim', 'Kim Chi', 'kim@daum.net', 1992)")
cur.execute(
    "INSERT INTO userTable VALUES('lee', 'Lee Pal', 'lee@paran.com', 1988)")
cur.execute(
    "INSERT INTO userTable VALUES('park', 'Park Su', 'park@gmail.com', 1980)")

con.commit()
con.close()
