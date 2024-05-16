print("\nПоиск слов в тексте\n")
text1 = input("Введите текст: ")
text1 = text1.lower()
text2 = input("Введите искомый фрагмент: ")
text2 = text2.lower()
index=text1.find(text2)
if index==-1:
	print("Фрагмент не найден")
else:
	print("Фрагмент найден -",index,"символ")
	while index!=-1:
		index=text1.find(text2,index+1)
		if index!=-1:
			print("Фрагмент найден -",index,"символ")