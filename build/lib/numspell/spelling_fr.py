"""Frech rules and tables for the numspell module"""

RULES = """
ab = {a0}-{b}
axx = {a} cent {x}
(a)xxx = {a} {*} {x}
"""

NUMBERS = {
    0: 'zero',
    1: 'un',
    2: 'deux',
    3: 'trois',
    4: 'quatre',
    5: 'cinq',
    6: 'six',
    7: 'sept',
    8: 'huit',
    9: 'neuf',
    10: 'dix',
    11: 'onze',
    12: 'douze',
    13: 'treize',
    14: 'quatorze',
    15: 'quize',
    16: 'seize',
    17: 'dix sept',
    18: 'dix huit',
    19: 'dix neuf',
    20: 'vingt',
    30: 'trente',
    40: 'quarante',
    50: 'cinquante',
    60: 'soixante',
    70: 'soixante-dix',
    80: 'quatre-vingt',
    90: 'quatre-vingt-dix'
}

ORDERS = [
    '',
    'mille', 'million', 'milliard', 'trillion', 'quadrillion',
    'quintillion', 'sextillion', 'septillion', 'octillion', 'nonillion',
    'decillion', 'undecillion', 'duodecillion', 'tredecillion',
    'quattuordecillion', 'quindecillion'
]
