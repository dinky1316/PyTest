# sqlite 접근 하기 위한
import sqlite3

#  해당 데이터 베이스 연결 하기 위한 인스턴스
con = sqlite3.connect("C:/CookAnalysis/naverDB")
# 해당 데이터베이스에서 cursor (특정 테이블에 접근하기 위한 도구)
cur = con.cursor()
# 터미널에서 입력 받은 데이터를, 테이블에 저장하는 예제
while (True):
    data1 = input("사용자ID ==> ")
    if data1 == "":
        break
    data2 = input("사용자이름 ==> ")
    data3 = input("이메일 ==> ")
    data4 = input("출생연도 ==> ")
    sql = "INSERT INTO userTable VALUES('" + data1 + \
        "','" + data2 + "','" + data3 + "', " + data4 + ")"
    # sql 문장을 cur(커서로) C(insert)
    cur.execute(sql)
# 저장
con.commit()
con.close()
