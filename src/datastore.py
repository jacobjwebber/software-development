import os
import pickle

"""
This contains functions that enable the persistent storage for the war gaming app.
The implementation may very well change as development continues but the api can 
remain the same.
"""

def persist_band(band):
	"""
	This method allows a band to be persisted using the pickle dump routine.
	"""
	if os.path.isdir(os.path.join(os.path.dirname(os.path.realpath(__file__)), "bands")):
		bands = os.listdir(os.path.join(os.path.dirname(os.path.realpath(__file__)), "bands"))

	bandname = band['Name']
	pickle.dump(band, open(os.path.join(os.path.join(os.path.dirname(os.path.realpath(__file__)), "bands"),bandname), "wb"))

def get_band(bandname):
	"""
	Request a band from persistent storage.
	"""
	if os.path.isdir(os.path.join(os.path.dirname(os.path.realpath(__file__)), "bands")):
		bands = os.listdir(os.path.join(os.path.dirname(os.path.realpath(__file__)), "bands"))
	loadedband = pickle.load(open(os.path.join(os.path.join(os.path.dirname(os.path.realpath(__file__)), "bands"),band), "rb"))
	return loadedband
