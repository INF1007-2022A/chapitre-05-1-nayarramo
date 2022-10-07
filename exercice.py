#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List

from numpy import number


def convert_to_absolute(number: float) -> float:
    if number < 0: number = -number
    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    noms = []
    for letter in prefixes:
        noms += [letter+suffixe]
    return noms


def prime_integer_summation() -> int:
    premier = [1, 2]
    nb = 3
    while len(premier) < 100:
        is_premier = True
        for div in range(2, nb//2):
            if nb%div==0:
                is_premier = False
        if is_premier:
            premier+=[nb]
        nb +=1

    return sum(premier)


def factorial(number: int) -> int:
    fact = 1
    for i in range(number):
        fact = fact * (number - i)
    return fact


def use_continue() -> None:
    for nb in range(1,11):
        if nb != 5:
            print(nb)
    pass


def verify_ages(groups: List[List[int]]) -> List[bool]:
    list = []
    for group in groups:
        value = True
        if len(group)>10 or len(group)<=3:
            value = False
        if value:
            for age in group:
                if 50 in group and age > 70:
                    value = False
                if age < 18:
                    value = False
            if 25 in group:
                value = True

        list.append(value)
        
    return list


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
