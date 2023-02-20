import random

def search_seq(array, data):
	global count
	position = -1
	for i in range(len(array)):
		count += 1
		if array[i] == data:
			position = i
			break
	return position


def search_bin(array, data):
	global count
	start = 0
	end = len(array) - 1

	while (start <= end):
		count += 1
		mid = (start + end) // 2

		if data == array[mid]:
			return mid
		elif data > array[mid]:
			start = mid + 1
		else:
			end = mid - 1

	return -1


data_array, sorted_array = [], []
find_data = 7878
count = 0


data_array = [random.randint(0, 999999) for _ in range(1000000)]
data_array.insert(random.randint(0, 1000000), find_data)
sorted_array = sorted(data_array)

print(f"#비정렬 배열(100만개) --> {data_array[0:5]} ~~~~ {data_array[-5:len(data_array)]}")
print(f"#정렬 배열(100만개) --> {sorted_array[0:5]} ~~~~ {sorted_array[-5:len(sorted_array)]}")

count = 0
position = search_seq(data_array, find_data)
if position != -1:
	print(f"순차 검색(비정렬 데이터) --> {count} 회")

count = 0
position = search_bin(sorted_array, find_data)
if position != -1:
	print(f"이진 검색(정렬 데이터) --> {count} 회")