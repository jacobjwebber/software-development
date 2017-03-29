"""
This module contains the game rules.
"""
import json
import config


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
    createdband['Captain'] = dict(config.wizard['Captain'])
    createdband['Captain']['Specialism'] = capspec
    createdband['Captain']['Skillset'].append(capskill)
    createdband['Captain']['Items'].append(capweap)
    if 'hasensign' in requestform.keys():

        ensspec = requestform['ensspec']
        ensskill = requestform['ensskill']
        ensweap = requestform['ensweap']
        createdband['Ensign'] = dict(config.apprentice['Ensign'])
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
    total = 0
    for item in createdband['Captain']['Items']:
        total = total + config.cost[item]
    if 'Ensign' in createdband.keys():
        total = total + 250
        for item in createdband['Captain']['Items']:
            total = total + config.cost[item]
    for troop in createdband['Troops']:
        total = total + config.troops[troop]['Cost']
    return total


def validate_band(createdband):
    ''' Checks that band has neither too many troops, nor has overspent. '''
    if len(createdband['Troops']) > 9 or createdband['Treasury'] < 0:
        return False
    else:
        return True
