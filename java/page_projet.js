
function projets(Id){
    var text="";

    if (Id=="ecole"){
        text="Je compte poursuivre mes études à l'ENSIBS en 2ème année de prépa intégrée, avant d'intégrer le cycle ingénieur en spécialité Génie Énergétique et Électrique. Ce choix s'inscrit dans un projet professionnel réfléchi, orienté vers les enjeux de la transition énergétique et de l'électrification des systèmes, des secteurs en forte croissance qui correspondent à mes ambitions et compétences."
    }

    if (Id=="Bricolage"){
        text="Je compte continuer le plus possible à réaliser des projets en bois, autant par plaisir que pour apprendre de nouvelles techniques. Pour l'instant, je souhaite me lancer dans la fabrication de mobilier pour travailler sur de plus grandes pièces. Mais si j'ai le temps, j'aimerais également me pencher sur la métallurgie pour perfectionner mes projets."
    }

    if (Id=="travail"){
        text="Je cherche un stage pour l'été 2026 afin d'effectuer une première expérience dans le monde du travail, plus précisément dans le domaine de l'énergie et de l'électrique. Cela me permettra de découvrir ce secteur, de valider mon choix de filière et d'avoir un aperçu des entreprises susceptibles de m'accueillir en alternance lors de mon cycle ingénieur."
    }
    document.getElementById("prochain-projet").textContent=text;
}
