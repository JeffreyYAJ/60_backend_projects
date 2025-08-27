from flask import Flask, jsonify, request, send_from_directory
from app import app, allowed_file
import os
from werkzeug.utils import secure_filename

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        return jsonify({"message": "File uploaded successfully", "filename": filename}), 201

    return jsonify({"error": "File type not allowed"}), 400

@app.route("/files", methods=["GET"])
def list_files():
    files = os.listdir(app.config["UPLOAD_FOLDER"])
    return jsonify({"files": files})

@app.route("/download/<filename>", methods=["GET"])
def download_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename, as_attachment=True)

@app.route("/delete/<filename>", methods=["DELETE"])
def delete_file(filename):
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return jsonify({"message": f"{filename} deleted successfully"})
    return jsonify({"error": "File not found"}), 404

