function partenaires(Id){
    var image;

    if(Id =="Naval"){
        image = "Naval.png";
    }
    else if (Id =="Thales"){
        image = "thales.png";
    }
    else if (Id == "Orange"){
        image = "orange.png";
    }

    document.getElementById("monImage").src = image;
}