# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    capital_city.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lbenatta <lbenatta@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/24 12:17:45 by lbenatta          #+#    #+#              #
#    Updated: 2022/10/16 15:20:46 by lbenatta         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import itertools
import collections
import sys

def change_dico(arg):
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    values_states = states.get(arg, 'no key')
    values_capitals = capital_cities.get(values_states)
    print(values_capitals)

def main():
    if(len(sys.argv) !=2):
        return
    change_dico(sys.argv[1])

if __name__ =='__main__':
    main()

#  python3 capital_city.py Oregon
