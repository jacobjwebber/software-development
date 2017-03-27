#!/bin/bash

# This script installs a virtual env if it does not already exist, and builds and tests the server

virtualenv env

env/bin/pip install -r requirements.txt
env/bin/python framework.py
