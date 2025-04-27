document.getElementById("formusuario").addEventListener("submit", function (event) {
    event.preventDefault();
  
    const nombre = document.getElementById("nombre").value;
    const correo = document.getElementById("correo").value;
    const oficina = document.getElementById("oficina").value;
    const tipo = document.getElementById("tipo").value;
    const usuario = document.getElementById("usuario").value;
    const contrasena = document.getElementById("contrasena").value;
  
    const data = { nombre, correo, oficina, tipo, usuario, contrasena };
  
    fetch("/agregarusuario", { 
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      })
      .then((response) => response.text())
      .then((data) => {
        const parser = new DOMParser();
        const doc = parser.parseFromString(data, "text/html");
  
        const estado = doc.querySelector("#alert-container").getAttribute("data-estado");
        const mensaje = doc.querySelector("#alert-container").getAttribute("data-mensaje");
  
        if (estado === "True") {
          Swal.fire({
            icon: "success",
            title: "¡Éxito!",
            text: mensaje,
            confirmButtonText: "Aceptar",
          }).then(() => {
            window.location.href = "/agregarusuario/";
          });
        } else {
          Swal.fire({
            icon: "error",
            title: "¡Error!",
            text: mensaje,
            confirmButtonText: "Aceptar",
          });
        }
      })
      .catch((error) => {
        Swal.fire({
          icon: "error",
          title: "¡Algo salió mal!",
          text: "Hubo un problema al procesar la solicitud.",
          confirmButtonText: "Aceptar",
        });
      });
  });
  