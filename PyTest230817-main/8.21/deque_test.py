
# deque 테스트

from collections import deque

deque_list = deque()
for i in range(5):
    deque_list.append(i)
print(f"deque_list의 출력 : {deque_list}")

deque_list_left = deque()
for i in range(5):
    deque_list_left.appendleft(i)
print(f"deque_list_left 출력 : {deque_list_left}")

# rotate

print(f"해당 deque의 요소의 메모리 위치 주소값 : {id(deque_list[0])}")  # 0 나옴

deque_list.rotate(2)
print(f"test_deque_rotate 출력 : {deque_list}")

print(f"해당 deque의 요소의 메모리 위치 주소값 : {id(deque_list[0])}")  # 3 나옴

# reverse

test_deque_reverse = deque(reversed(deque_list))
print(f"test_deque_reverse 츨력 : {test_deque_reverse}")

deque_list.extend([5, 6, 7])
print(f"deque_list.extend([5,6,7]) 출력 : {deque_list}")

deque_list.extendleft([8, 9, 10])
print(f"deque_list.extendleft([8, 9, 10]) 출력 : {deque_list}")
