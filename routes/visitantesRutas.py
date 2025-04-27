from flask import request, jsonify, render_template, session, flash,  redirect
from app import app
from models.oficina import Oficina
from models.visitante import Visitante
from datetime import date


@app.route("/visitasVew")
def registrosVisitasVew():
    if 'nombre' not in session:
        flash("Debes iniciar sesión para acceder a esta página", "danger")
        return render_template('login.html')
    try:
        # visitantes =registra visitas
        oficinas = Oficina.objects()
        return render_template('registrarVisitas.html', oficinas=oficinas), 200
    except Exception as e:
        print("Error al obtener los visitantes:", e)
        return jsonify({"error": "Error al obtener los visitantes"}), 500

@app.route("/listarVisitas")
def ListarVisitantesVista():
    if 'nombre' not in session:
        flash("Debes iniciar sesión para acceder a esta página", "danger")
        return render_template('login.html')
    try:
        visitantes = Visitante.objects()
        return render_template('listarVisitantes.html', visitantes=visitantes), 200
    except Exception as e:
        print("Error al obtener los visitantes:", e)
        return jsonify({"error": "Error al obtener los visitantes"}), 500
    
@app.route("/registrarEntrada" , methods=["POST"])
def registrarEntrada():
    try:
        data = request.form.to_dict() if request.form else request.get_json(force=True) # obtener los datos del formulario
        data["estado"] = "Ingreso" # establecer el estado como ingreso
        data["oficina"] = Oficina.objects(id=data["oficina"]).first()#consultar la oficina por id a la bd
        data["fecha_visita"] = date.today()#obtener la fecha actual
        data["correo"] = data["correo"].lower()#convertir el correo a minuscula
        data["nombre"] = data["nombre"].lower()#convertir el nombre a minuscula
        
        visitante = Visitante(**data) # crear el objeto Visitante y guardar los datos
        visitante.save() # guardar el visitante en la base de datos
        oficinas = Oficina.objects() # obtener todas las oficinas
        flash('Registro de entrada exitoso', 'success')
        return render_template('registrarVisitas.html', oficinas=oficinas), 200
    except Exception as e:
        print("Error al obtener los visitantes:", e)
        return jsonify({"error": "Error al obtener los visitantes"}), 500
    
@app.route("/registrarSalida" , methods=["POST"])
def registrarSalida():
    try:
        data = request.form.to_dict() if request.form else request.get_json(force=True)
        data["estado"] = "Salida"
        data["oficina"] = Oficina.objects(id=data["oficina"]).first()#consultar la oficina por id a la bd
        data["fecha_visita"] = date.today()#obtener la fecha actual
        data["correo"] = data["correo"].lower()#convertir el correo a minuscula
        data["nombre"] = data["nombre"].lower()
        
        visitante = Visitante(**data)
        visitante.save()
        oficinas = Oficina.objects()
        flash('Registro de salida exitoso', 'success')
        return render_template('registrarVisitas.html', oficinas=oficinas), 200
    except Exception as e:
        print("Error al obtener los visitantes:", e)
        return jsonify({"error": "Error al obtener los visitantes"}), 500