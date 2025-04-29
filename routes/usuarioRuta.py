from flask import  render_template, request, redirect, url_for, flash, jsonify, session
from models.usuario import Usuario 
from models.oficina import Oficina 
from app import app
import random
import string
from werkzeug.security import generate_password_hash
import yagmail
import threading
import requests
email = yagmail.SMTP('kmilo2083@gmail.com','jzdqbzdqoqkspnnw',encoding='utf-8')

@app.route('/usuariosRegistroVista', methods=['GET'])
def usuariosRegistroVista():
    oficinas = Oficina.objects()
    return render_template('agregarusuario.html', oficinas=oficinas)

@app.route('/dash')
def dash():
    return render_template('login.html')

@app.route('/usuarios/logout', methods=['POST'])
def logout():
    try:
        session.clear()
        return jsonify({"message": "Sesión cerrada"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
def enviarCorreo(destinatario, asunto, mensaje):
    email.send(to=destinatario, subject=asunto, contents=mensaje)
    
@app.route('/agregarUsuario', methods=['POST'])
def agregarUsuario():
    try:
        data = request.form.to_dict() if request.form else request.get_json(force=True) # obtener los datos del formulario
        nombre = data.get("nombre") # obtener el nombre
        correo = data.get("correo") # obtener el correo
        oficina = data.get("oficina") # obtener la oficina
        tipo = data.get("tipo")
        
        if not all([nombre, correo, oficina, tipo]):
            return jsonify({"error": "Faltan campos obligatorios"}), 400
        
        
        
        #generar contraseña aleatoria
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        data["usuario"] = correo # guardar el correo como usuario
        data["contrasena"] = password # guardar la contraseña
        
        usu = Usuario(**data) # crear el objeto Usuario y guardar los datos
        usu.save() # guardar el usuario en la base de datos
        mensaje = f'Hola, has hecho el registro en la aplicación. Este es el reporte de tus datos: correo: {correo}, password: {password}'
        destinatarios = [correo, 'kmilo2083@gmail.com']  
        hilo = threading.Thread(target=enviarCorreo, args=(destinatarios, 'Registro exitoso', mensaje))
        hilo.start()
        flash('Usuario registrado exitosamente.', 'success')
        return redirect(url_for('inicio'))
    except Exception as e:
        print("Error al crear el usuario:", e)
        return jsonify({"error": "Error al crear el usuario"}), 500
    

@app.route('/usuariosLogin', methods=['POST'])
def login_usuario():
    try:
        data = request.form # obtener los datos del formulario
        correo = data.get("usuario") # obtener el correo
        passw = data.get("contrasena") # obtener la contraseña
        print("Correo:", correo)
        print("Contraseña:", passw)
        
        usuario = Usuario.objects(usuario=correo).first()#buscar el usuario por el correo
        print("Usuario encontrado:", usuario)
        
        if usuario is None:#verificar si el usuario existe
            print("Usuario no encontrado entro")
            flash("Usuario no registrado. Verifica tu correo.", "danger")
            return redirect(url_for('inicio'))  # Redirige antes de hacer cualquier acceso
        
        if not usuario.contrasena == passw: #verificar si la contraseña es correcta
            print("Contraseña incorrecta entro")
            flash("Contraseña incorrecta. Inténtalo de nuevo.", "danger")
            return redirect(url_for('inicio'))
        
        #sesion y correo
        session["id"] = str(usuario.id)     # guardar el id del usuario en la sesion
        session["correo"] = usuario.correo
        session["nombre"] = usuario.nombre
        session["tipo"] = usuario.tipo
        session["autenticado"] = True
        
        if usuario.tipo == "Administrador":
            return redirect(url_for('ListarVisitantesVista'))
        elif usuario.tipo == "Asistente":
            return redirect(url_for('registrosVisitasVew'))
        
        # si no es ninguno de esos tipos
        return redirect(url_for('inicio'))
        
        return jsonify({"message": "Login exitoso"}), 200
    except Exception as e:
        print("Error al iniciar sesion:", e)
        return jsonify({"error": "Error al inicio de sesion"}), 500