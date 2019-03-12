# Roman numerals are represented by seven different symbols: 
# I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, two is written as II in Roman numeral, just two one's 
# added together. Twelve is written as, XII, which is simply X + II. 
# The number twenty seven is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left 
# to right. However, the numeral for four is not IIII. Instead, the 
# number four is written as IV. Because the one is before the five we
# subtract it making four. The same principle applies to the number nine,
# which is written as IX. There are six instances where subtraction 
# is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer. Input is guaranteed 
# to be within the range from 1 to 3999.

class RomanToInteger:
	
	def __init__(self, input_int):
		
		self.input_int = input_int
		
	def build_symbol(self):
		num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
		           (90, 'XC'), (50, "L"), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'),
		           (4, 'IV'), (1, 'I')]									
		
		roman = ''
		
		while self.input_int > 0:
			for num, symb in num_map:
				while self.input_int >= num:
					roman += symb
					self.input_int -= num
		
		print (roman)	
			
			 		
		
case = RomanToInteger(28)
case.build_symbol()