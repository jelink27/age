driving = input('請問你有沒有開過車?')
age = input ('請問你的年齡?')
age = float(age)
age_2 = int (18 - age)

if driving != '有' and driving !='沒有':
	print('只能輸入 有/沒有'
		raise systemExit

if driving == '有':
	if age >= 18:
		print('你通過測驗了')
	else:  
		print('你還不可以開車')
elif driving == '沒有' :
	if age >= 18:
		print('你可以考駕照了')
	else:
		print('再過',age_2,'年就可以去考了')
else:
	print('只能輸入有或沒有')
