from mongoengine import Document, StringField, IntField, DateTimeField, ListField, ReferenceField, EmbeddedDocument, EmbeddedDocumentField
from models.oficina import Oficina
from datetime import datetime

class Visitante(Document):
    nombre = StringField(required=True)
    correo = StringField(required=True)
    oficina = ReferenceField(Oficina , required=True) 
    fecha_visita = DateTimeField(default=datetime.utcnow) 
    estado = StringField(required=True, choices=['Ingreso', 'Salida'])
    
    def _repr__(self):
        return self.nombre