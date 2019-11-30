Temp = int(input("Qual a temperatura da água? "))
if Temp > 100:
		aguaFerve = True
		evaporação = 'muito'
		print("ferveu!!")
else:
		aguaMorna = True
		aguaFerve = False
		print("Putz! A água ainda tá morna!")
