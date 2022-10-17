# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    numbers.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lbenatta <lbenatta@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/24 12:17:45 by lbenatta          #+#    #+#              #
#    Updated: 2022/10/16 15:19:46 by lbenatta         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#np.set_printoptions(formatter={'float_kind':'{:f}'.format})

#-------------------------------------------------------Data reading----------------------------------------------------------
#data = pd.read_txt('numbers.txt', sep=',')
with open("numbers.txt", "r") as fichier:
	lines = fichier.read().split(',')
	print (fichier.read())
for line in lines:
	print(line)
fichier.close()

