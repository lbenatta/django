# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    beverages.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lbenatta <lbenatta@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/24 12:17:45 by lbenatta          #+#    #+#              #
#    Updated: 2022/10/17 14:47:48 by lbenatta         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# class SomeClass:
#++	cl = Rectangle
#	cl = Triangle
#	pass

# class Something:
#     def out(self):
#         print("it works")

# s = Something()
# s.out()

#from typing_extensions import Self


class HotBeverage:
	# name= ''
	# price= ''
	# description = ''

	#def out(self):
	#	print("it works")
	def __init__(self, name, price, description):
		self.name = name
		self.price = price
		self.description = description
		#print(self.name + self.description)
		#super(HotBeverage, self).__init__(name, price, description)
	def __str__(self):
		return f'HotBeverage({self.name},{self.price},{self.description})'

	def mybeverage(self):
		print("A " + self.name)

	def myprice(self):
		print(self.price)

	def mydescription(self):
		print("A " + self.name + self.description + "please")

coffee = HotBeverage("Coffee", "0.4 Euros", " To take away ")
coffee.mybeverage()
coffee.mydescription()
coffee.myprice()

tea = HotBeverage("Tea", "0.3 Euros", " Just some hot water in a cup.")
tea.mybeverage()
tea.mydescription()
tea.myprice()

chocolate = HotBeverage("Chocolate", "0.5 Euros", " Chocolate, sweet chocolate...")
chocolate.mybeverage()
chocolate.mydescription()
chocolate.myprice()

cappucino = HotBeverage("Cappucino", "0.45 Euros", " Un po’ di Italia nella sua tazza!")
cappucino.mybeverage()
cappucino.mydescription()
cappucino.myprice()



# Here we declare that the Square class inherits from the Rectangle class
	# class Square(Rectangle):
	# 	def __init__(self, length, **kwargs):
	# 		super(Square, self).__init__(length=length, width=length, **kwargs)

	# class Cube(Square):
	# 	def surface_area(self):
	# 		face_area = super(Square, self).area()
	# 		self.surface_area =(face_area * 6)
	# 		return face_area * 6
	# print(face_area * 6)

	# def volume(self):
	# 	face_area = super(Square, self).area()
	# 	return face_area * self.length
	# print(face_area * self.length)

# class Triangle:
# 	def __init__(self, base, height, **kwargs):
# 		self.base = base
# 		self.height = height
# 		super().__init__(**kwargs)

# 	def tri_area(self):
# 		return 0.5 * self.base * self.height
# 	print(0.5 * self.base * self.height)

# 	class RightPyramid(Square, Triangle):
# 		def __init__(self, base, slant_height, **kwargs):
# 			self.base = base
# 			self.slant_height = slant_height
# 			kwargs["height"] = slant_height
# 			kwargs["length"] = base
# 			super().__init__(base=base, **kwargs)

# 		def area(self):
# 			base_area = super().area()
# 			perimeter = super().perimeter()
# 			return 0.5 * perimeter * self.slant_height + base_area
# 	print(0.5 * perimeter * self.slant_height + base_area)

# 	def area_2(self):
# 		base_area = super().area()
# 		triangle_area = super().tri_area()
# 		return triangle_area * 4 + base_area
# 	print(triangle_area * 4 + base_area)


