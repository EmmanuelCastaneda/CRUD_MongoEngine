from app import app, db
import os
from flask import request,render_template,url_for,session,redirect,flash
from bson.objectid import ObjectId
from mongoengine.errors import ValidationError
from models.models import productos,categorias,Usuarios


@app.route("/home")
def home():
    if "correo" in session:
        listaProducto = productos.objects()
        return render_template("listarProductos.html", productos=listaProducto)
    else:
        mensaje ="Ingrese nuevamente sus Datos"
        return render_template("login2.html", mensaje=mensaje)
    
@app.route("/vistaAgregarProducto")
def vistaAgregarProducto():
    mensaje = None
    if "correo" in session:
        listaCategoria = categorias.objects()
        return render_template("formulario.html", categorias=listaCategoria)
    else:
        mensaje = "Ingrese nuevamente sus Datos"
        return render_template("login2.html", mensaje=mensaje)


@app.route('/vistaAgregarProducto', methods=['POST'])
def agregarProducto():
    if request.method == 'POST':
        codigo = int(request.form['codigo'])
        nombre = request.form['nombre']
        precio = int(request.form['precio'])
        categoria = request.form['categoria']
        foto = request.files['imagen']
        producto = productos(codigo=codigo,nombre=nombre,precio=precio, categoria=categoria)
        print(producto.nombre)
        producto.save() 
        FotoNombre = os.path.join(app.config["UPLOAD_FOLDER"], str(producto.id)) + ".jpg"
        FotoNombre = os.path.join(app.config["UPLOAD_FOLDER"], f"{producto.id}.jpg")

        foto.save(FotoNombre)
        
        flash('Se ha agregado correctamente', 'success') 
        return redirect(url_for('home'))

    else:
        listaProductos = productos.objects().all()
        return render_template('home', productos=listaProductos)
    
@app.route("/eliminar_producto/<producto_id>", methods=["POST"])
def eliminar_producto(producto_id):
    if "correo" in session:
        try:
            resultado = productos.objects(id=producto_id).delete()
            if resultado == 1:
                flash("Producto eliminado correctamente", "success")
                return redirect(url_for("home"))
            else:
                return "Producto no encontrado."
        except ValidationError as error:
            print("Error al eliminar el producto", error)
            return "Error al eliminar el producto"
    else:
        mensaje = "Ingrese nuevamente sus Datos"
        return render_template("login2.html", mensaje=mensaje)


@app.route("/editar_producto/<producto_id>", methods=["GET"])
def editar_producto(producto_id):
    if "correo" in session:
        try:
            producto = productos.objects(id=ObjectId(producto_id)).first()
            if producto:
                listaCategorias = categorias.objects()
                return render_template("Editar.html", producto=producto, categorias=listaCategorias)
            else:
                return "No se encontro el producto"
        except ValidationError as error:
            print("No se pudo editar e producto ", error)
            mensaje = "Error al intentar editar el producto"
    else:
        mensaje = "Ingrese nuevamente sus Datos"
        return render_template("login2.html", mensaje=mensaje)

@app.route("/actualizar_Producto/<producto_id>", methods=["POST"])
def actualizar_producto(producto_id):
    if "correo" in session:
        try:
            codigo = int(request.form["codigo"])
            nombre = request.form["nombre"]
            precio = int(request.form["precio"])
            idCategoria = request.form["categoria"]
            foto = request.files["imagen"]

            productoActualizado = {
                "codigo": codigo,
                "nombre": nombre,
                "precio": precio,
                "categoria": categorias.objects.get(id=idCategoria)
            }
            productos.objects(id=producto_id).update(**productoActualizado)
            if foto:
                FotoNombre = f"{producto_id}.jpg"
                foto.save(os.path.join(app.config["UPLOAD_FOLDER"], FotoNombre))
            return redirect(url_for("home"))
        except ValidationError as error:
            print("Error al actualizar", error)
            mensaje = "Error al intentar actualizar el producto"
    else:
        mensaje = "Ingrese nuevamente sus Datos"
        return render_template("login2.html", mensaje=mensaje)
    
    
    



