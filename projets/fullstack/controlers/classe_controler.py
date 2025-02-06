""" Ce fichier contient au départ toutes les routes de l'application
# Concernant le CRUD des élèves
"""
from flask import Blueprint, request, render_template, redirect, url_for


import services.classe as svc


classe_bp = Blueprint('classe_bp', __name__)

@classe_bp.route('/', methods=['GET'])
def liste_classe():
    # Traitement du template et transmission du HTML généré au client
    return render_template('liste_classe.jinja', classe=svc.get_all_Classes())


@classe_bp.route('/create', methods=['GET', 'POST'])
def create_classe():
    if request.method == 'POST':
        # On utilise un POST pour créer un nouvel élève
        print("CREATION")
        id_classe = svc.create_classe(request.form['nom'], request.form['eleves'])
        return redirect(url_for('classe_bp.read_classe', id=id_classe))
    else:
        # On utilise un GET pour afficher le formulaire
        return render_template('form_classe.jinja', classe=None)


@classe_bp.route('/<int:id>', methods=['GET'])
def read_classe(id: int):
    e = svc.get_classe(id)
    return render_template('detail_classe.jinja', classe=e, action='afficher')


@classe_bp.route('/update/<int:eid>', methods=['GET', 'POST'])
def update_classe(eid: int):
    if request.method == 'POST':
        # On utilise un POST pour créer un nouvel élève
        svc.update_classe(eid, request.form['nom'], request.form['eleves'])
        return redirect(url_for('classe_bp.read_classe', id=eid))
    else:
        # On utilise un GET pour afficher le formulaire
        e = svc.get_classe(eid)
        print("Demande de modification",e)
        return render_template('form_classe.jinja', classe=e)


@classe_bp.route('/delete/<int:eid>', methods=['GET'])
def delete_classe(eid: int):
    svc.delete_classe(eid)
    return redirect(url_for('classe_bp.liste_classe'))

