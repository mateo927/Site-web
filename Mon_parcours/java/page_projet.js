
function projets(Id){
    var text;

    if (Id=="ecole"){
        text="Je compte continuer mes etudes a L'ENSIBS pour une 2 eme annee de prepa integree pour ensuite faire commencer mon cycle ingenieur en specialiter genie enregetique et electrique"
    }

    if (Id=="bois"){
        text="Je compte continuer le plus possible a faire des projets en bois pour le plaisir et pour apprendre de nouvelles techniques de travail pour l'instant je vais commencer a faire du mobilier pour travailler sur de plus grandes pieces.Mais aussi si  j'ai le temps me pencher sur la metelurgie pour perfectionner mes projets en bois ."
    }

    if (Id=="travail"){
        text="Je cherche un stage pour l'été 2026 pour pouvoir rentrer dans le monde du travail plus precisement dans le domaine de l'energie et de l'electrique pour decouvrir ce domaine et pour valider mon choix de filiere de plus cela pourrat me faire une idee sur les entreprise possible pour ma future alternance en cycle ingenieur."
    }
    document.getElementById("prochain-projet").textContent=text;
}
