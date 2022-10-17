# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    machine.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lbenatta <lbenatta@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/24 12:17:45 by lbenatta          #+#    #+#              #
#    Updated: 2022/10/17 18:03:54 by lbenatta         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#https://www.digitalocean.com/community/tutorials/how-to-install-django-and-set-up-a-development-environment-on-ubuntu-20-04

class CoffeeMachine


	class EmptyCup
		self_name =

# Réalisez la classe CoffeeMachine contenant :
# • Un constructeur.
# • Une classe EmptyCup héritant de HotBeverage, avec pour nom "empty cup",
# comme prix 0.90 et comme description "An empty cup?! Gimme my money back!".
# Copiez le fichier beverages.py de l’exercice précédent dans le dossier de cet exercice pour pouvoir utiliser les classes qu’il contient.
# • Une classe BrokenMachineException héritant de Exception avec pour texte "This
# coffee machine has to be repaired.". Ce texte doit être défini dans le constructeur de l’exception.
# • Une méthode repair() qui répare la machine pour lui permettre de servir à nouveau des boissons chaudes.
# • Une méthode serve() qui aura les caractéristiques suivantes :
# Paramètres : Un unique paramètre (autre que self) qui sera une classe dérivée
# de HotBeverage.
# Retour : Une fois sur deux (aléatoirement), la méthode retourne une instance de
# la classe passée en paramètre, et une fois sur deux une instance de EmptyCup.
# 10
# Formation Python-Django - 0 OOB
# Obsolescence : La machine n’est pas de la meilleure qualité et tombe donc en
# panne après 10 boissons servies.
# En cas de panne : l’appel de la méthode serve() doit provoquer la levée d’une
# exception de type CoffeeMachine.BrokenMachineException jusqu’à-ce que
# la méthode repair() soit appelée.
# Réparation : Après un appel de la méthode repair(), la méthode serve() peut
# de nouveau fonctionner sans levée d’exception pendant un cycle de 10 boissons,
# avant de retomber en panne.
# Dans vos tests, instanciez la classe CoffeeMachine. Demandez diverses boissons venant du fichier beverages.py et affichez la boisson que vous sert la machine jusqu’à-ce
# qu’elle tombe en panne (vous devez gérer l’exception alors levée). Réparez la machine et
# recommencez jusqu’à-ce que la machine tombe de nouveau en panne (gérez à nouveau
# l’exception)
