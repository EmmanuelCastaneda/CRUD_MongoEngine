from mongoengine import Document, ReferenceField,StringField,IntField,EmailField

class Usuarios(Document):
    usuario=StringField(max_length=50, required=True,unique=True)
    nombre=StringField(max_length=50)
    correo=EmailField(required=True)
    contraseña=StringField(max_length=50)
    verificar_contraseña=StringField(max_length=50)
    
class categorias(Document):
    nombre=StringField(max_length=50 , unique=True)
    
class productos(Document):
    codigo=IntField(unique=True)
    nombre=StringField(max_length=50)
    precio=IntField()
    categoria=ReferenceField(categorias)
    
    