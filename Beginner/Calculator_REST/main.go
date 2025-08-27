package main

import (
	"encoding/json"
	"fmt"
	"net/http"
)

type CalculatorOperation struct{
	Number1 float64 `json:"number1"`
	Number2 float64 `json:"number2"`
	Operator string `json:"operator"`
}

type CalculatorAnswer struct {
	Answer float64 `json:"answer"`
	Error string `json:"error"`
}

func calculate(w http.ResponseWriter, r *http.Request)  {
	if r.Method != http.MethodPost {
		http.Error(w, "Invalid request method. POST method expected.", http.StatusMethodNotAllowed)
		return 
	}
	var request CalculatorOperation
	error := json.NewDecoder(r.Body).Decode(&request)

	if error!= nil{
		http.Error(w, "Invalid JSON data.", http.StatusBadRequest)
		return
	}

	var result float64

	switch request.Operator {
	case "+":
		result = request.Number1 + request.Number2
	
	case "-":
		result = request.Number1 + request.Number2
	
	case "*":
		result = request.Number1 * request.Number2
		
	case "/":
		if request.Number2 == 0{
			http.Error(w, "Division by zero Error.", http.StatusNotImplemented)
			return 
		}
		result = request.Number1/ request.Number2
	default:
		json.NewEncoder(w).Encode(CalculatorAnswer{Error:"Invalid operator"}) 
		return 
	}

	w.Header().Set("Content-Type","application/json")
	json.NewEncoder(w).Encode(CalculatorAnswer{Answer:result})

}

func main()  {
	http.HandleFunc("/calculate", calculate)
	fmt.Println("Server running on http://localhost:8000")

	if error:= http.ListenAndServe(":8000", nil); error !=nil{
		fmt.Println("Failed to start server", error)
	}
}