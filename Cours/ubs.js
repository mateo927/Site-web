// On attend que le DOM soit entièrement chargé avant d'exécuter le script
document.addEventListener("DOMContentLoaded", () => {

    // Associe chaque image (via son src) à sa description textuelle
    const descriptions = {
        "../Cours/photos/Fac_D.jpg": "Installée dans des bâtiments modernes sur le campus de Tohannic.",
        "../Cours/photos/Fac_L.jpg" : "La Faculté, située sur le campus de Lorient, accueille chaque année environ 2000 étudiant·es. Nous proposons des formations de la licence au doctorat dans les domaines des lettres & langues et sciences humaines & sociales.",
        "../Cours/photos/Fac_S.jpg" : "À la rentrée universitaire de septembre 2023, nous avons augmenté nos effectifs,  essentiellement au niveau Licence (L1, L2 et L3), de plus de 15% pour atteindre près de 3000 étudiants, en Licence et Master, dont 500 hors les murs.",
        "../Cours/photos/ENSIBS.jpg" : "Implantée au sein de l'Université de Bretagne-Sud, l'École Nationale Supérieure d'Ingénieurs de Bretagne-Sud (ENSIBS) propose six spécialités",
        "../Cours/photos/IUT_vannes.jpg" : "Des formations dans les domaines de la Gestion, du Commerce, de l'Informatique, de la Science des Données.",
        "../Cours/photos/iut.jpg" : "L'IUT Lorient - Pontivy, c'est : 2 sites, 6 Bachelors Universitaires de Technologie (B.U.T.), 3 licences professionnelles et 650 étudiants.",
        "../Cours/photos/iae.jpg" : "L'IAE Bretagne Sud propose une offre de formation diversifiée."
    };

    const zone = document.getElementById("description-text");

    // Écoute les clics sur toute la page pour détecter le clic sur une image
    document.addEventListener("click", (e) => {
        const nom = e.target.getAttribute("src");
        // Affiche la description correspondante, ou un message par défaut si introuvable
        zone.textContent = descriptions[nom] || "Aucune description disponible";
    });
});
