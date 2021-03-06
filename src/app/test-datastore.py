import datastore

testband = {
    'Troops': ['Combat Droid'],
    'Captain': {
        'Shoot': 2,
        'Shield': 12,
        'Items': ['Needle Gun'],
        'Move': 5,
        'Experience': 0,
        'Fight': 2,
        'Morale': 4,
        'Skillset': ['Aim'],
        'Cost': 0,
        'Health': 12,
        'Specialism': 'Marksman'
    },
    'Name': 'tuesday',
    'Treasury': 338
}


def test_if_stored():
    datastore.persist_band(testband)
    gotband = datastore.get_band(testband['Name'])
    datastore.delete_band(testband['Name'])
    assert (testband == gotband)


def test_if_dict():
    datastore.persist_band(testband)
    gotband = datastore.get_band(testband['Name'])
    datastore.delete_band(testband['Name'])
    assert (isinstance(gotband, dict))


def test_get_list():
    assert (isinstance(datastore.get_list_of_bands(), list))


def test_list_contains():
    datastore.persist_band(testband)
    listofbands = datastore.get_list_of_bands()
    datastore.delete_band(testband['Name'])
    if testband['Name'] in listofbands:
        assert (True)
    else:
        assert (False)
