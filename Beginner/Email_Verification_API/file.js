// Fonction pour obtenir le commentaire selon l'âge
function obtenirCommentaire(age) {
    if (age >= 1 && age <= 6) {
        return "Vous êtes un jeune enfant.";
    } else if (age >= 7 && age <= 11) {
        return "Vous êtes un enfant qui a atteint l'âge de raison.";
    } else if (age >= 12 && age <= 17) {
        return "Vous êtes un adolescent.";
    } else if (age >= 18 && age <= 120) {
        return "Vous êtes un adulte.";
    } else {
        return "Âge invalide. Veuillez entrer un âge entre 1 et 120 ans.";
    }
}

// Exemple d'utilisation
const age = parseInt(prompt("Entrez votre âge :"));
const commentaire = obtenirCommentaire(age);
console.log(commentaire);

// Vous pouvez aussi tester avec des valeurs directement
console.log(obtenirCommentaire(5));   // Jeune enfant
console.log(obtenirCommentaire(9));   // Âge de raison
console.log(obtenirCommentaire(15));  // Adolescent
console.log(obtenirCommentaire(25));  // Adulte
console.log(obtenirCommentaire(130)); // Âge invalide
