package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
)

func uploadHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method == "GET" {
		html := `
			<html>
				<body>
					<form enctype="multipart/form-data" action="/upload" method="post">
						<input type="file" name="myFile" />
						<input type="submit" value="Upload" />
					</form>
				</body>
			</html>`
		fmt.Fprint(w, html)
		return
	}

	// Parse file
	file, header, err := r.FormFile("myFile")
	if err != nil {
		http.Error(w, "Error uploading file", http.StatusBadRequest)
		return
	}
	defer file.Close()

	// Create destination file
	dst, err := os.Create("./uploads/" + header.Filename)
	if err != nil {
		http.Error(w, "Cannot save file", http.StatusInternalServerError)
		return
	}
	defer dst.Close()

	// Copy file content
	_, err = io.Copy(dst, file)
	if err != nil {
		http.Error(w, "Error saving file", http.StatusInternalServerError)
		return
	}

	fmt.Fprintf(w, "File uploaded successfully: %s\n", header.Filename)
}

func main() {
	// Create upload dir if not exists
	os.MkdirAll("./uploads", os.ModePerm)

	http.HandleFunc("/upload", uploadHandler)
	fmt.Println("Server started at http://localhost:8080")
	http.ListenAndServe(":8080", nil)
}
