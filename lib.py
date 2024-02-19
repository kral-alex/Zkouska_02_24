from abc import ABC, abstractmethod
import math


class Statistik(ABC):
	
	@abstractmethod
	def arit_prumer(self, values: list[float]) -> float:
		pass

	@abstractmethod
	def kvad_prumer(self, values: list[float]) -> float:
		pass


class StatistikCalculate(Statistik):
	
	def arit_prumer(self, values: list[float]) -> float:
		return sum(values) / len(values)


	def kvad_prumer(self, values: list[float]) -> float:
		return math.sqrt(sum(x**2 for x in values) / len(values))

class StatistikLog(Statistik):
	
	def __init__(self, delegate: Statistik):
		self._delegate = delegate

	
	def arit_prumer(self, values: list[float]) -> float:
		print(values)
		res = self._delegate.arit_prumer(values)
		print(res)
		return res

	def kvad_prumer(self, values: list[float]) -> float:
		print(values)
		res = self._delegate.kvad_prumer(values)
		print(res)
		return res
