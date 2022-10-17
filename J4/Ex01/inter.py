# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    inter.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lbenatta <lbenatta@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/24 12:17:45 by lbenatta          #+#    #+#              #
#    Updated: 2022/10/16 16:26:19 by lbenatta         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Person:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self):
        return f'Person({self.name},{self.position})'

    def myfunc1(self):
        print("Je m'appelle " + self.name)

    def myfunc2(self):
        print("Je suis " + self.position)

    def myfunc3(self):
        print(self.name + ", this is the worst coffee you ever tasted")

    def myfunc4(self):
        print(self.name + ", this is the beeeeeest coffee I ever tasted")

    def myfunc5(self):
        print("Je suis " + self.position + ", I can’t do that...")


p1 = Person("Mark", "Intern")
p1.myfunc1()
p1.myfunc2()
p1.myfunc3()

p2 = Person('Lolo','Chef')
p2.myfunc1()
p2.myfunc2()
p2.myfunc4()

p3 = Person('No name','Intern')
p3.myfunc2()
p3.myfunc5()

