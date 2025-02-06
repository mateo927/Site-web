""" Ce fichier contient au départ toutes les routes de l'application
# Concernant le CRUD des élèves
"""
from flask import Blueprint, request, render_template, redirect, url_for


import services.classe as svc_classe


classe_bp = Blueprint('classe_bp', __name__)

@classe_bp.route('/', methods=['GET'])
def liste_classe():
    return render_template('liste_classe.jinja', classe=svc_classe.get_all_Classes())

@classe_bp.route('/create', methods=['GET', 'POST'])
def create_classe():
    if request.method == 'POST':
        id_classe = svc_classe.create_classe(request.form['nom'], request.form['eleves'])
        return redirect(url_for('classe_bp.read_classe', id=id_classe))
    else:
        return render_template('form_classe.jinja', classe=None)

@classe_bp.route('/<int:id>', methods=['GET'])
def read_classe(id: int):
    e = svc_classe.get_classe(id)
    return render_template('detail_classe.jinja', classe=e, action='afficher')

@classe_bp.route('/update/<int:eid>', methods=['GET', 'POST'])
def update_classe(eid: int):
    if request.method == 'POST':
        svc_classe.update_classe(eid, request.form['nom'], request.form['eleves'])
        return redirect(url_for('classe_bp.read_classe', id=eid))
    else:
        e = svc_classe.get_classe(eid)
        return render_template('form_classe.jinja', classe=e)

@classe_bp.route('/delete/<int:eid>', methods=['GET'])
def delete_classe(eid: int):
    svc_classe.delete_classe(eid)
    return redirect(url_for('classe_bp.liste_classe'))

