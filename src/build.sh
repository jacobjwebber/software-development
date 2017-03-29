#!/bin/bash

# This script installs a virtual env if it does not already exist, and builds and tests the server

virtualenv env

env/bin/pip install -r requirements.txt
cd app
../env/bin/yapf -i *.py
../env/bin/nosetests
../env/bin/python framework.py
