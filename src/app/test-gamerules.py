"""
This file tests game rules
"""
from werkzeug.datastructures import ImmutableMultiDict
import gamerules

testrequest = ImmutableMultiDict([('bandname', u'test-request'), (
    'capweap', u'Needle Gun'
), ('troops',
    u'["Lackey","Combat Droid","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty"]'
    ), ('capspec', u'Psychology'), ('capskill', u'Bolster')])

testband = {
    'Troops': [u'Lackey', u'Combat Droid'],
    'Captain': {
        'Shoot': 2,
        'Shield': 12,
        'Items': [u'Needle Gun'],
        'Move': 5,
        'Experience': 0,
        'Fight': 2,
        'Morale': 4,
        'Skillset': [u'Bolster'],
        'Cost': 0,
        'Health': 12,
        'Specialism': u'Psychology'
    },
    'Name': u'test-request',
    'Treasury': 318
}


def test_convert_to_band():
    band = gamerules.form_to_band(testrequest)
    assert (band == testband)


def test_validate_band():
    assert (gamerules.validate_band(testband))
