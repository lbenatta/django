# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    var_to_dict.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lbenatta <lbenatta@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/24 12:17:45 by lbenatta          #+#    #+#              #
#    Updated: 2022/10/16 15:20:10 by lbenatta         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"Allman" : 1946,
"King" : 1925,
"Clapton" : 1945,
"Johnson" : 1911,
"Berry" : 1926,
"Vaughan" : 1954,
"Cooder" : 1947,
"Page" : 1944,
"Richards" : 1943,
"Hammett" : 1962,
"Cobain" : 1967,
"Garcia" : 1942,
"Beck" : 1944,
"Santana" : 1947,
"Ramone" : 1948,
"White" : 1975,
"Frusciante": 1970,
"Thompson" : 1949,
"Burton" : 1939}

#for i in mon_dico.items():
#    print(i)

for key,valeur in mon_dico.items():
	print(valeur ,":",  key)

