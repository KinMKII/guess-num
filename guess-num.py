import random

r = random.randint(1, 100)
while True:
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('恭喜你猜對了')
		break
	else:
		if num > r:
			print('不對, 再猜一次, 你的數字太大了')
		elif num < r:
			print('不對, 再猜一次, 你的數字太小了')