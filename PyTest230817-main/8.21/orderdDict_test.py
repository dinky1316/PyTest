
from collections import OrderedDict

# d = {}

# 정렬된 딕션너리, collections 모듈에서 OrderdDict 클래스 이용해서,

# 정렬 옵션 함수 추가 및 sorted 함수 이용하기


def sorted_by_key(t):
    return t[0]


def sorted_by_value(t):
    return t[1]


d = dict()
d['a'] = 10
d['b'] = 2
d['c'] = 7
d['d'] = 6

test_OrderedDict = OrderedDict(sorted(d.items(), key=sorted_by_key)).items()
for k, v in test_OrderedDict:
    print(f"key : {k}, value: {v}")

# for k, v in d.items():
#     print(f"key : {k}, value: {v}")
