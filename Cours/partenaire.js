// Change l'image affichée selon le bouton partenaire cliqué
function partenaires(Id){
    var image;

    if (Id=="Naval"){
        image="NAVAL.png"
    }

    if (Id=="Thales"){
        image="Thales.png"
    }

    if (Id=="Orange"){
        image="Orange-cyberdefense.png"
    }

    // Met à jour le src de l'image principale avec le logo choisi
    document.getElementById("monImage").src=image
}
