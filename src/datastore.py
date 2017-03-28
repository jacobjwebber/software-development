import os
import pickle
"""
This contains functions that enable the persistent storage for the war gaming app.
The implementation may very well change as development continues but the api can 
remain the same.
"""

banddir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "bands")


def persist_band(band):
    """
	This method allows a band to be persisted using the pickle dump routine.
	"""
    bandname = band['Name']
    bandfile = open(os.path.join(banddir, bandname), 'wb')
    pickle.dump(band, bandfile)
    bandfile.close


def get_band(bandname):
    """
	Request a band from persistent storage.
	"""
    bandfile = open(os.path.join(banddir, bandname), 'rb')
    loadedband = pickle.load(bandfile)
    print(loadedband)
    bandfile.close
    return loadedband


def get_list_of_bands():
    if os.path.isdir(banddir):
        bands = os.listdir(banddir)
    else:
        bands = None
    return bands


def delete_band(band):
    os.remove(os.path.join(banddir, band))
    return
