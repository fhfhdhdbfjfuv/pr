from linsys import LinSys

class App:
	
	def __init__(self) -> None:
		pass

	def run(self) -> None:
		numberOfUnknowns = self.getInputNumberOfUnknowns()

		linsys = LinSys(numberOfUnknowns)

		linsys.processUserInput()

		if linsys.solve():
			linsys.printAnswer()
	
	def getInputNumberOfUnknowns(self) -> int:
		while True:
			try:
				numberOfUnknowns = int(input("Введите количество неизвестных (менее 4): "))
			except ValueError:
				print("Введённое значение должно быть целым числом!")
				continue
			if numberOfUnknowns < 1:
				print("Введённое значение не может быть меньше единицы!")
				continue
			elif numberOfUnknowns > 3:
				print("Введённое значение не может быть больше трёх!")
				continue
			return numberOfUnknowns

