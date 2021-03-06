import httpcodes
import datastore
import gamerules
import config

import logging
import json
import os
from flask import Flask, request, render_template, redirect, g, send_from_directory

# Create exportable app
app = Flask(__name__)

banddir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "bands")


def render_illegal_band():
    return render_template(
        'blankband.html',
        people=config.troops,
        wizard=config.wizard,
        apprentice=config.apprentice,
        specs=config.specialisms,
        skills=config.skillsets,
        weaps=config.weapon), httpcodes.BAD_REQUEST


def render_new_band():
    return render_template(
        'blankband.html',
        people=config.troops,
        wizard=config.wizard,
        apprentice=config.apprentice,
        specs=config.specialisms,
        skills=config.skillsets,
        weaps=config.weapon), httpcodes.OK


def render_created_band():
    return render_template(
        'blankband.html',
        people=config.troops,
        wizard=config.wizard,
        apprentice=config.apprentice,
        specs=config.specialisms,
        skills=config.skillsets,
        weaps=config.weapon), httpcodes.CREATED


def render_edit_band(loadedband):
    return render_template(
        'editband.html',
        band=loadedband,
        people=config.troops,
        wizard=config.wizard,
        apprentice=config.apprentice,
        specs=config.specialisms,
        skills=config.skillsets,
        weaps=config.weapon), httpcodes.OK


def render_edit_list(bandlist):
    return render_template('bandlist.html', bands=bandlist), httpcodes.OK


def render_illegal_edit_band(loadedband):
    return render_template(
        'editband.html',
        band=loadedband,
        people=config.troops,
        wizard=config.wizard,
        apprentice=config.apprentice,
        specs=config.specialisms,
        skills=config.skillsets,
        weaps=config.weapon), httpcodes.OK


@app.route('/', methods=['GET'])
def welcome_page():
    return app.send_static_file('index.html'), httpcodes.OK


@app.route('/new', methods=['GET', 'POST'])
def new_warband():
    if request.method == 'GET':
        return render_new_band()
    if request.method == 'POST':
        createdband = gamerules.form_to_band(request.form)
        if gamerules.validate_band(createdband) == False:
            return render_illegal_band()
        else:
            datastore.persist_band(createdband)
            return render_created_band()


@app.route('/edit', methods=['GET'])
def edit_warband():
    bands = datastore.get_list_of_bands()
    return render_edit_list(bands)


@app.route('/edit/<band>', methods=['GET', 'POST'])
def edit_given_warband(band):

    loadedband = datastore.get_band(band)
    if request.method == 'GET':
        return render_edit_band(loadedband)
    if request.method == 'POST':
        createdband = gamerules.form_to_band(request.form)

    if gamerules.validate_band(createdband):
        datastore.persist_band(createdband)
        return render_edit_list(datastore.get_band_list())
    else:
        return render_illegal_band()


@app.route('/delete/<band>', methods=['GET'])
def delete_given_warband(band):
    datastore.delete_band(band)
    bands = datastore.get_list_of_bands()
    return render_edit_list(bands)


if __name__ == "__main__":
    app.run(host=config.host, port=config.port)
