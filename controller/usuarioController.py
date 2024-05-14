# from app import app, db
# from flask import render_template, request, redirect, url_for, session,json
# from werkzeug.security import generate_password_hash, check_password_hash
# from mongoengine import Document, StringField, ReferenceField
# import urllib.request
# from models.model import Usuarios


# @app.route("/")
# def Login():
#     return render_template("login.html")


# @app.route("/", methods=["GET", "POST"])
# def login():
#     mensaje = None
#     if request.method == "POST":
#         correo = request.form.get("correo")
#         contraseña = request.form.get("contraseña")
#         recaptcha_response = request.form.get("g-recaptcha-response")

#         url = "https://www.google.com/recaptcha/api/siteverify"
#         values = {
#             "secret": "6Lfk2MYpAAAAACamgvV3nWjGQvB46OTnEAvwiQjj",
#             "response": recaptcha_response,
#         }
#         data = urllib.parse.urlencode(values).encode()
#         req = urllib.request.Request(url, data=data)
#         with urllib.request.urlopen(req) as response:
#             result = json.loads(response.read().decode())

#         if result["success"]:
#             usuario = Usuarios.objects(correo=correo).first()
#             if usuario:
#                 if usuario.verificar_contraseña(contraseña):
#                     session["correo"] = correo
#                     return redirect(url_for("home"))
#                 else:
#                     mensaje = "Contraseña incorrecta"
#             else:
#                 mensaje = "Correo electrónico no registrado"
#         else:
#             mensaje = "Captcha no válido"

#     return render_template("login.html", mensaje=mensaje)


# @app.route("/salir")
# def salir():
#     session.clear()
#     mensaje = "Se ha cerrado la sesión"
#     return render_template("login.html", mensaje=mensaje)



from app import app, db
from flask import render_template, request, redirect, url_for, session
import json
import urllib.request
from models.models import Usuarios

 
    
@app.route("/")
def Login(): 
    return render_template ("login2.html")
@app.route("/", methods=["GET", "POST"])
def login():
    mensaje = None
    if request.method == "POST":
        correo = request.form.get("correo")
        contraseña = request.form.get("contraseña")
        recaptcha_response = request.form.get("g-recaptcha-response") 
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values ={
            'secret': '6Lfk2MYpAAAAACamgvV3nWjGQvB46OTnEAvwiQjj',
            'response': recaptcha_response 
        }
        data = urllib.parse.urlencode(values).encode()
        req = urllib.request.Request(url, data=data)
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode())
        if result['success']:
            usuario = Usuarios.objects(correo=correo, contraseña=contraseña).first()
            if usuario:
                session["correo"] = correo
                return redirect(url_for("home"))
            else:
                mensaje = "Los datos no coinciden"
        else:
            mensaje = "Captcha invalido"
    return render_template("login2.html", mensaje=mensaje)


@app.route("/salir")
def salir():
    session.clear()
    mensaje="Se ha cerrado sesion"
    return render_template("login2.html",mensaje=mensaje)