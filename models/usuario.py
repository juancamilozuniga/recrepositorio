from mongoengine import * 

class Usuario(Document):
    nombre =StringField(max_length=80,required=True)
    correo =StringField(max_length=80,required=True)
    oficina=StringField(max_length=80,required=True)
    tipo=StringField(max_length=80,required=True)
    usuario=StringField(max_length=80,required=True)
    contrasena = StringField(required=True)
    
    def _repr__(self):
        return self.nombre