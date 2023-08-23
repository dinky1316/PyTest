import sqlite3

## 변수 선언 부분 ##
con, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
row = None

## 메인 코드 부분 ##
con = sqlite3.connect("C:/CookAnalysis/testDB_230822.db")
cur = con.cursor()

cur.execute("SELECT * FROM user_test")

print("사용자ID    이메일      패스워드")
print("-----------------------------------------")

while (True):
    row = cur.fetchone()
    if row == None:
        break
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    print("%3d   %11s   %10s  " % (data1, data2, data3))

con.close()
