// calculator-api/main.go
package main

import (
	"encoding/json" // Pour encoder/décoder les données JSON
	"fmt"           // Pour afficher des logs dans la console
	"net/http"      // Pour créer et gérer le serveur HTTP
)

// -------------------
// STRUCTURES DE DONNÉES
// -------------------

// Structure pour représenter la requête envoyée par le client
// Exemple JSON attendu : {"num1": 10, "num2": 5, "operator": "+"}
type CalculationRequest struct {
    Num1     float64 `json:"num1"`     // Premier nombre
    Num2     float64 `json:"num2"`     // Deuxième nombre
    Operator string  `json:"operator"` // Opérateur mathématique (+, -, *, /)
}

// Structure pour représenter la réponse envoyée au client
type CalculationResponse struct {
    Result float64 `json:"result"`           // Résultat du calcul
    Error  string  `json:"error,omitempty"`  // Message d'erreur (facultatif, omis si vide)
}

// -------------------
// HANDLER PRINCIPAL
// -------------------

// Fonction qui traite la requête HTTP POST /calculate
func calulate(w http.ResponseWriter, r *http.Request) {
    // 1️⃣ Vérifier que la méthode est POST (pas GET, PUT, etc.)
    if r.Method != http.MethodPost {
        http.Error(w, "Invalid request method", http.StatusMethodNotAllowed)
        return
    }

    // 2️⃣ Déclarer une variable pour stocker les données reçues
    var req CalculationRequest

    // 3️⃣ Décoder le JSON envoyé par le client dans la variable `req`
    err := json.NewDecoder(r.Body).Decode(&req)
    if err != nil {
        http.Error(w, "Invalid JSON data", http.StatusBadRequest)
        return
    }

    // 4️⃣ Déclarer une variable pour le résultat final
    var result float64

    // 5️⃣ Exécuter l'opération en fonction de l'opérateur fourni
    switch req.Operator {
    case "+":
        result = req.Num1 + req.Num2
    case "-":
        result = req.Num1 - req.Num2
    case "*":
        result = req.Num1 * req.Num2
    case "/":
        // Vérifier si division par zéro
        if req.Num2 == 0 {
            json.NewEncoder(w).Encode(CalculationResponse{Error: "Division by zero"})
            return
        }
        result = req.Num1 / req.Num2
    default:
        // Si l'opérateur est invalide
        json.NewEncoder(w).Encode(CalculationResponse{Error: "Invalid operator"})
        return
    }

    // 6️⃣ Préparer et envoyer la réponse au client
    w.Header().Set("Content-Type", "application/json") // Type de contenu JSON
    json.NewEncoder(w).Encode(CalculationResponse{Result: result})
}

// -------------------
// FONCTION MAIN
// -------------------

func man() {
    // Associer la route "/calculate" à la fonction `calculate`
    http.HandleFunc("/calculate", calculate)

    // Message de confirmation dans le terminal
    fmt.Println("✅ Calculator API is running on http://localhost:8080")

    // Lancer le serveur HTTP sur le port 8080
    if err := http.ListenAndServe(":8080", nil); err != nil {
        fmt.Println("❌ Failed to start server:", err)
    }
}
