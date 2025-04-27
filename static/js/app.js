function salir() {
    const url = "/usuarios/logout"
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then(respuesta => respuesta.json())
        .then(resultado => {
            console.log("esta es la data; ", resultado)
            if (resultado.message == "Sesión cerrada") {
                location.href = "/"
                alert("Sesion cerrada")
            } else {
                swal.fire("Error", resultado.message, "error")
                alert("Error al cerrar la sesion")
            }
        })
        .catch(error => {
            console.log(error)
            alert("Error al cerrar la sesion")
        })
}