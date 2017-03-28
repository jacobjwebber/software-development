import httpcodes
import datastore
import gamerules

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
        people=gamerules.troops,
        wizard=gamerules.wizard,
        apprentice=gamerules.apprentice,
        specs=gamerules.specialisms,
        skills=gamerules.skillsets,
        weaps=gamerules.weapon), httpcodes.BAD_REQUEST


def render_new_band():
    return render_template(
        'blankband.html',
        people=gamerules.troops,
        wizard=gamerules.wizard,
        apprentice=gamerules.apprentice,
        specs=gamerules.specialisms,
        skills=gamerules.skillsets,
        weaps=gamerules.weapon), httpcodes.OK


def render_created_band():
    return render_template(
        'blankband.html',
        people=gamerules.troops,
        wizard=gamerules.wizard,
        apprentice=gamerules.apprentice,
        specs=gamerules.specialisms,
        skills=gamerules.skillsets,
        weaps=gamerules.weapon), httpcodes.CREATED


def render_edit_band(loadedband):
    return render_template(
        'editband.html',
        band=loadedband,
        people=gamerules.troops,
        wizard=gamerules.wizard,
        apprentice=gamerules.apprentice,
        specs=gamerules.specialisms,
        skills=gamerules.skillsets,
        weaps=gamerules.weapon), httpcodes.OK


def render_edit_list(bandlist):
    return render_template('bandlist.html', bands=bandlist), httpcodes.OK


def render_illegal_edit_band(loadedband):
    return render_template(
        'editband.html',
        band=loadedband,
        people=gamerules.troops,
        wizard=gamerules.wizard,
        apprentice=gamerules.apprentice,
        specs=gamerules.specialisms,
        skills=gamerules.skillsets,
        weaps=gamerules.weapon), httpcodes.OK


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
        return render_edit_band(band)
    if request.method == 'POST':

        bandname = request.form['bandname']
        capspec = request.form['capspec']
        skills = json.loads(request.form['capskill'])
        capweap = request.form['capweap']
        troops = json.loads(request.form['troops'])
        capmov = request.form['capmove']
        capfig = request.form['capfight']
        capsho = request.form['capshoot']
        capshi = request.form['capshield']
        capmor = request.form['capmorale']
        caphea = request.form['caphealth']
        capexp = request.form['capexperience']
        createdband = dict()
        createdband['Name'] = bandname
        createdband['Captain'] = dict(gamerules.wizard['Captain'])
        createdband['Captain']['Specialism'] = capspec
        createdband['Captain']['Skillset'].extend(skills)
        createdband['Captain']['Items'].append(capweap)
        createdband['Captain']['Move'] = capmov
        createdband['Captain']['Fight'] = capfig
        createdband['Captain']['Shoot'] = capsho
        createdband['Captain']['Shield'] = capshi
        createdband['Captain']['Morale'] = capmor
        createdband['Captain']['Health'] = caphea
        createdband['Captain']['Experience'] = capexp
        if 'hasensign' in request.form.keys():

            ensspec = request.form['ensspec']
            eskills = json.loads(request.form['ensskill'])
            ensmov = request.form['ensmove']
            ensfig = request.form['ensfight']
            enssho = request.form['ensshoot']
            ensshi = request.form['ensshield']
            ensmor = request.form['ensmorale']
            enshea = request.form['enshealth']
            ensexp = request.form['ensexperience']
            ensweap = request.form['ensweap']
            createdband['Ensign'] = dict(gamerules.apprentice['Ensign'])
            createdband['Ensign']['Specialism'] = ensspec
            createdband['Ensign']['Skillset'].extend(eskills)
            createdband['Ensign']['Items'].append(ensweap)
            createdband['Ensign']['Move'] = ensmov
            createdband['Ensign']['Fight'] = ensfig
            createdband['Ensign']['Shoot'] = enssho
            createdband['Ensign']['Shield'] = ensshi
            createdband['Ensign']['Morale'] = ensmor
            createdband['Ensign']['Health'] = enshea
            createdband['Ensign']['Experience'] = ensexp
        createdband['Troops'] = []
        for item in troops:
            if item != "Empty":
                createdband['Troops'].append(item)
        if gamerules.validate_band(createdband):
            datastore.persist_band(createdband)
            return render_edit_list(datastore.get_band_list())
        else:
            return render_illegal_band()


@app.route('/delete/<band>', methods=['GET'])
def delete_given_warband(band):
    datastore.delete_band(band)
    bands = datastore.get_band_list()
    return render_edit_list(bands)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
