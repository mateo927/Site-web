
function projets(Id){
    var text="cliquez sur un bouton pour voir les futurs projets que j'ai prévus dans ces domaines";

    if (Id=="ecole"){
        text="Je compte poursuivre mes études à l'ENSIBS en 2ème année de prépa intégrée, avant d'intégrer le cycle ingénieur en spécialité Génie Énergétique et Électrique. Ce choix s'inscrit dans un projet professionnel réfléchi, orienté vers les enjeux de la transition énergétique et de l'électrification des systèmes, des secteurs en forte croissance qui correspondent à mes ambitions et compétences."
    }

    if (Id=="Bricolage"){
        text="Je compte continuer le plus possible à faire des projets en bois, pour le plaisir et pour apprendre de nouvelles techniques. Pour l'instant, je vais commencer à faire du mobilier pour travailler sur de plus grandes pièces. Mais si j'ai le temps, je voudrais aussi me pencher sur la métallurgie pour perfectionner mes projets."
    }

    if (Id=="travail"){
        text="Je cherche un stage pour l'été 2026 pour pouvoir rentrer dans le monde du travail, plus précisément dans le domaine de l'énergie et de l'électrique. Cela me permettra de découvrir ce domaine, de valider mon choix de filière et de me faire une idée sur les entreprises possibles pour ma future alternance en cycle ingénieur."
    }
    document.getElementById("prochain-projet").textContent=text;
}
