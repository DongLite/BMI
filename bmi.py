#這是一個計算BMI數值以來告訴使用者是否過胖的程式

height = input('請輸入你的身高(公尺)(至小數點後兩位):')
weight = input('請輸入你的體重(公斤):')

height = float(height)
weight = float(weight)

bmi = weight / (height * height)

print('你的BMI值為：', bmi)
if bmi < 18.5:
	print('體重過輕')
elif bmi >= 18.5 and bmi < 24:
	print('正常人')
elif bmi >= 24 and bmi < 27:
	print('過重')
elif bmi >= 27 and bmi < 30:
	print('輕度肥胖')
elif bmi >= 30 and bmi < 35:
	print('中度肥胖')
elif bmi >=35:
	print('重度肥胖')
