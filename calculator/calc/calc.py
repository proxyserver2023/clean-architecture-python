# -*- coding: utf-8 -*-

from functools import reduce

class Calc:
	
	
	def add(self, *args):
		return (sum(args))


	def sub(self, a, b):
		return a - b

	
	def mul(self, *args):
		if not all(args):
			raise ValueError
		return reduce(lambda x, y: x * y, args)

	
	def div(self, a, b):
		return a/b


	def avg(self, *args, ut=None, lt=None):
		if not args:
			return 0

		if not ut:
			ut = max(args)
		if not lt:
			lt = min(args)

		args = [arg for arg in args if arg >= lt and arg <= ut]
		return ((sum(args)/len(args)) if args else 0)