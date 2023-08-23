import xlrd  # 읽기
import xlwt  # 쓰기

# 특정 조건 부분을 만족하는 행 부분을 추출해서, 쓰기

# 읽기 인스턴스
workbook = xlrd.open_workbook('c:/CookAnalysis/Excel/singer.xls')
# 쓰기 인스턴스
outWorkbook = xlwt.Workbook()
# 특정 컬럼의 인덱스 번호
idx = 4  # 평균 키의 인덱스

# 워크시트 목록들
wsheetList = workbook.sheets()
# 새 액셀 파일의 워크시트의 이름을 수동으로 지정 : singer
outSheet = outWorkbook.add_sheet("singer")
# 읽은 액셀 파일의 첫번째 워크시트 이름
worksheet = wsheetList[0]
# 첫 워크시트의 열의 갯수를 이용해서 반복
for col in range(worksheet.ncols):
    # 새로운 액셀 파일의 새 워크시트에 값을 추가하는 부분
    # 한 행이 고정이 되어서, 컬럼 부분만 변경이 업데이트 된다
    outSheet.write(0, col, worksheet.cell_value(0, col))

# 전역 변수인데 상태 변수로 사용중이고,
# 첫 행이 컬럼 제목이다 보니까, 2번째 행부터 데이터라서 구분짓기 위한
# 용도로 사용중
totalRow = 0
# 각 워크시트 이름에 대해서
for worksheet in wsheetList:
    # 예) junior 워크시트라면
    for row in range(1, worksheet.nrows):
        # 평균키를 의미하는 인덱스 번호 : 4 이 부분 값을 가져와서
        height = worksheet.cell_value(row, idx)
        # 조건문으로 분기
        if int(height) >= 165:
            # 165 이상이면, totalRow 증가
            totalRow += 1
            # junior의 워크시트의 열의 갯수만큼 반복
            for col in range(worksheet.ncols):
                # 예) 1행(행이 고정), 각 열에 대해서 반복을 함
                outSheet.write(totalRow, col, worksheet.cell_value(row, col))

outWorkbook.save('c:/CookAnalysis/Excel/outSinger2_230822.xls')
print("Save. OK~")
