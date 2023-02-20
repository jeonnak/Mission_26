import random

def search_bin(array, data):
	start = 0
	end = len(array) - 1

	while (start <= end):
		mid = (start + end) // 2
		if data == array[mid]:
			return mid
		elif data > array[mid]:
			start = mid + 1
		else:
			end = mid - 1

	return -1

data_array = ['바나나맛우유', '레쓰비캔커피', '츄파춥스', '도시락', '삼다수', '코카콜라', '삼각김밥']
sell_array = [random.choice(data_array) for _ in range(20)]

print(f"#오늘 판매된 전체 물건(중복O, 정렬X) --> {sell_array}")
sell_array.sort()
print(f"#오늘 판매된 전체 물건(중복O, 정렬O) --> {sell_array}")
sell_product = list(set(sell_array))
print(f"#오늘 판매된 물품 종류(중복x) --> {sell_product}")

count_list = []
for product in sell_product:
	count = 0
	position = 0
	while (position != -1):
		position = search_bin(sell_array, product)
		if position != -1:
			count += 1
			del(sell_array[position])
	count_list.append((product, count))

print()
print(f"결산 결과 ==> {count_list}")