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
    document.getElementById("monImage").src=image
}