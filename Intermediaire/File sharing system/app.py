from flask import Flask, render_template, request, send_from_directory, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key("yaj")

Up_folder = "./uploads"
os.makedirs(Up_folder, exist_ok=True)
app.config["UPLOAD_FOLDER"] = Up_folder
ALLOWED_EXTENSION = {'txt', 'png', 'yaj', 'zip', 'jpg', 'jpeg', 'pdf'}
help = 'file'


def verify_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSION

from routes import *