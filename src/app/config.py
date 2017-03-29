"""
This source file contains a list of variables that should be definable
without changing other source files.
"""

#server defaults

host = '0.0.0.0'
port = 5000

troops = {
    'Augment Gorilla': {
        'Move': 8,
        'Fight': 3,
        'Shoot': 0,
        'Shield': 10,
        'Morale': 2,
        'Health': 8,
        'Cost': 20,
        'Notes': 'Animal, Cannot carry treasure or items'
    },
    'Lackey': {
        'Move': 6,
        'Fight': 2,
        'Shoot': 0,
        'Shield': 10,
        'Morale': -1,
        'Health': 10,
        'Cost': 20,
        'Notes': 'Melee Weapon'
    },
    'Security': {
        'Move': 6,
        'Fight': 2,
        'Shoot': 1,
        'Shield': 12,
        'Morale': 2,
        'Health': 12,
        'Cost': 80,
        'Notes': 'Blaster, Blade'
    },
    'Engineer': {
        'Move': 4,
        'Fight': 0,
        'Shoot': 3,
        'Shield': 12,
        'Morale': 2,
        'Health': 10,
        'Cost': 60,
        'Notes': 'Blaster, Repair Kit'
    },
    'Medic': {
        'Move': 5,
        'Fight': 0,
        'Shoot': 0,
        'Shield': 12,
        'Morale': 3,
        'Health': 10,
        'Cost': 50,
        'Notes': 'Blade, Medkit'
    },
    'Commando': {
        'Move': 8,
        'Fight': 4,
        'Shoot': 0,
        'Shield': 10,
        'Morale': 4,
        'Health': 12,
        'Cost': 100,
        'Notes': 'Stealth Suit, Blade, Needle Gun'
    },
    'Combat Droid': {
        'Move': 3,
        'Fight': 2,
        'Shoot': 4,
        'Shield': 14,
        'Morale': 0,
        'Health': 14,
        'Cost': 150,
        'Notes': 'Mechanoid, Dual Blaster, Claws'
    },
}
wizard = {
    'Captain': {
        'Move': 5,
        'Fight': 2,
        'Shoot': 2,
        'Shield': 12,
        'Morale': 4,
        'Health': 12,
        'Cost': 0,
        'Skillset': [],
        'Specialism': None,
        'Items': [],
        'Experience': 0
    }
}
apprentice = {
    'Ensign': {
        'Move': 7,
        'Fight': 0,
        'Shoot': -1,
        'Shield': 10,
        'Morale': 2,
        'Health': 8,
        'Skillset': [],
        'Specialism': None,
        'Cost': 250,
        'Items': [],
        'Experience': 0
    }
}
specialisms = [
    'Engineering', 'Psychology', 'Marksman', 'Tactics', 'Melee', 'Defence'
]
skillsets = {
    'Engineering': ['Repair', 'Sabotage', 'Augment'],
    'Psychology': ['Bolster', 'Terror', 'Counter'],
    'Marksman': ['Aim', 'Pierce', 'Reload'],
    'Tactics': ['Squad', 'Ambush', 'Surround'],
    'Melee': ['Block', 'Risposte', 'Dual'],
    'Defence': ['Shield', 'Sacrifice', 'Resolute']
}
weapon = ['Blaster', 'Needle Gun', 'Blade', 'Cannon', 'Whip']
cost = {'Blaster': 5, 'Needle Gun': 12, 'Blade': 3, 'Cannon': 15, 'Whip': 5}
