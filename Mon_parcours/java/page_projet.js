
function projets(Id){
    var text;

    if (Id=="ecole"){
        text="Je compte continuer mes études à l'ENSIBS en 2ème année de prépa intégrée, pour ensuite commencer mon cycle ingénieur en spécialité Génie Énergétique et Électrique."
    }

    if (Id=="bois"){
        text="Je compte continuer le plus possible à faire des projets en bois, pour le plaisir et pour apprendre de nouvelles techniques. Pour l'instant, je vais commencer à faire du mobilier pour travailler sur de plus grandes pièces. Mais si j'ai le temps, je voudrais aussi me pencher sur la métallurgie pour perfectionner mes projets."
    }

    if (Id=="travail"){
        text="Je cherche un stage pour l'été 2026 pour pouvoir rentrer dans le monde du travail, plus précisément dans le domaine de l'énergie et de l'électrique. Cela me permettra de découvrir ce domaine, de valider mon choix de filière et de me faire une idée sur les entreprises possibles pour ma future alternance en cycle ingénieur."
    }
    document.getElementById("prochain-projet").textContent=text;
}
