"""
This module contains the game rules.
"""
import json

troops = {'Augment Gorilla': {'Move':8, 'Fight':3, 'Shoot':0, 'Shield':10, 'Morale':2, 'Health':8, 'Cost':20, 'Notes':'Animal, Cannot carry treasure or items'},
'Lackey': {'Move':6, 'Fight':2, 'Shoot':0, 'Shield':10, 'Morale':-1, 'Health':10, 'Cost':20, 'Notes':'Melee Weapon'}, 
'Security': {'Move':6, 'Fight':2, 'Shoot':1, 'Shield':12, 'Morale':2, 'Health':12, 'Cost':80, 'Notes':'Blaster, Blade'}, 
'Engineer': {'Move':4, 'Fight':0, 'Shoot':3, 'Shield':12, 'Morale':2, 'Health':10, 'Cost':60, 'Notes':'Blaster, Repair Kit'}, 
'Medic': {'Move':5, 'Fight':0, 'Shoot':0, 'Shield':12, 'Morale':3, 'Health':10, 'Cost':50, 'Notes':'Blade, Medkit'}, 
'Commando': {'Move':8, 'Fight':4, 'Shoot':0, 'Shield':10, 'Morale':4, 'Health':12, 'Cost':100, 'Notes':'Stealth Suit, Blade, Needle Gun'}, 
'Combat Droid': {'Move':3, 'Fight':2, 'Shoot':4, 'Shield':14, 'Morale':0, 'Health':14, 'Cost':150, 'Notes':'Mechanoid, Dual Blaster, Claws'},               
}
wizard = {'Captain': {'Move':5, 'Fight':2, 'Shoot':2, 'Shield':12, 'Morale':4, 'Health':12, 'Cost':0,  'Skillset': [], 'Specialism':None, 'Items':[], 'Experience':0}}
apprentice = {'Ensign': {'Move':7, 'Fight':0, 'Shoot':-1, 'Shield':10, 'Morale':2, 'Health':8,'Skillset': [], 'Specialism':None, 'Cost':250, 'Items':[], 'Experience':0}}
specialisms = [ 'Engineering', 'Psychology', 'Marksman', 'Tactics', 'Melee', 'Defence' ]
skillsets = { 'Engineering' : ['Repair', 'Sabotage', 'Augment'], 'Psychology': [ 'Bolster', 'Terror', 'Counter'], 'Marksman': ['Aim', 'Pierce', 'Reload'], 'Tactics': ['Squad', 'Ambush', 'Surround'], 'Melee': ['Block', 'Risposte', 'Dual'], 'Defence': ['Shield', 'Sacrifice', 'Resolute'] }
weapon = [ 'Blaster', 'Needle Gun', 'Blade', 'Cannon', 'Whip']
cost = { 'Blaster':5, 'Needle Gun':12, 'Blade':3, 'Cannon':15, 'Whip':5 }


def form_to_band(requestform):
       """
       This function takes in a HTTP request and returns a band object.
       """
       bandname = requestform['bandname']
       capspec = requestform['capspec']
       capskill = requestform['capskill']
       capweap = requestform['capweap']
       troops = json.loads(requestform['troops']) 
       createdband = dict()
       createdband['Name'] = bandname
       createdband['Captain'] = dict(wizard['Captain'])
       createdband['Captain']['Specialism'] = capspec
       createdband['Captain']['Skillset'].append(capskill)
       createdband['Captain']['Items'].append(capweap)
       if 'hasensign' in requestform.keys():
           
           ensspec = requestform['ensspec']
           ensskill = requestform['ensskill']
           ensweap = requestform['ensweap']
           createdband['Ensign'] = dict(apprentice['Ensign'])
           createdband['Ensign']['Specialism'] = ensspec
           createdband['Ensign']['Skillset'].append(ensskill)
           createdband['Ensign']['Items'].append(ensweap)
       createdband['Troops'] = []
       for item in troops:
           if item != "Empty":
               createdband['Troops'].append(item)
       createdband['Treasury'] = 500 - sumband(createdband)
       return createdband
 
def sumband(createdband):
    total = 0;
    for item in   createdband['Captain']['Items']:
        total = total + cost[item]
    if 'Ensign' in createdband.keys():
        total = total + 250
        for item in   createdband['Captain']['Items']:
            total = total + cost[item]
    for troop in createdband['Troops']:
        total = total + troops[troop]['Cost']
    return total

def validate_band(createdband):
    ''' Checks that band has neither too many troops, nor has overspent. '''
    if len(createdband['Troops']) > 9  or createdband['Treasury'] < 0:
        return False
    else:
        return True

