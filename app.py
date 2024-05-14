from flask import Flask
from flask_mongoengine import MongoEngine
app = Flask(__name__)
app.secret_key="5783290"
app.config["UPLOAD_FOLDER"]="./static/img"
app.config["MONGODB_SETTINGS"]=[{
    "db":"GESTIONPRODUCTOS1",
    "host": "mongodb://localhost:27017/GESTIONPRODUCTOS1"
    
}]
db = MongoEngine(app)


    
if __name__ == "__main__":
    from controller.productoController import *
    from controller.usuarioController import *
    from models.models import *


    
    app.run(port=4000, debug=True)
    


    
