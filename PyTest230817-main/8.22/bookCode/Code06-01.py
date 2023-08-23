# r : read
# csv -> c: 콤마, s : 구분자, v : 값
# 메모장에서 작업 가능
# csv -> MySql -> 값을 가져오기, 테이블 입력
# csv 파일을 읽어서 메모리상 inFP 라는
inFp = open("C:/CookAnalysis/CSV/singer1.csv", "r")

# 읽은 내용을 한줄씩 출력
inStr = inFp.readline()
print(inStr, end="")

inStr = inFp.readline()
print(inStr, end="")

inFp.close()
