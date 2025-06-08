import { cargarMatriz } from "./script.js"
import { loadPage } from "./Utils.js"

async function enviarArchivo() {
    const archivoInput = document.getElementById("archivo1");
    const archivo = archivoInput.files[0];
    console.log("hola");
    if (!archivo) {
        alert("Por favor selecciona un archivo JSON.");
        return;
    }

    const lector = new FileReader();

    lector.onload = function (e) {
        try {
            datos = JSON.parse(e.target.result);

            fetch('/resolver', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(datos)
            })
                .then(res => res.json())
                .then(async data => {
                    // document.getElementById("resultado").innerText =
                    //   "Respuesta del servidor:\n\n" + JSON.stringify(data, null, 2);
                    const container = document.getElementById("container")
                    await loadPage("templates/play.html", container, true)
                    console.log("holass");
                    cargarMatriz(data, datos);

                })
                .catch(err => {
                    console.error(err);
                    alert("Ocurrió un error al enviar los datos.");
                });

        } catch (error) {
            alert("El archivo no tiene formato JSON válido.");
        }
    };

    lector.readAsText(archivo);
}
const button = document.getElementById("boton1")
console.log(button);

button.addEventListener("click", enviarArchivo)
let datos = ""

const button1 = document.getElementById("boton2")

button1.addEventListener("click", () => {
    const resultado = document.getElementById("resultado2");
    console.log(document.getElementById("automata1").value);
    fetch('/resolverAutomata', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ automata: document.getElementById("automata1").value })
    })
        .then(res => res.json())
        .then(async data => {
            console.log(data, "holas");
            if (data.valida) {
                resultado.innerText = data.mensaje;
                resultado.style.color = "lightgreen";
            } else {
                resultado.innerText = data.error + "\n" + data.mensaje;
                resultado.style.color = "salmon";
            }
        })
        .catch(err => {
            console.error(err);
            alert("Ocurrió un error al enviar los datos.");
        });
    // Limpiar el campo de entrada
    document.getElementById("automata1").value = "";

})
const button3 = document.getElementById("boton3")

button3.addEventListener("click", async () => {
    console.log(document.getElementById("clave-producto").value);
    await fetch('/clave-producto', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ automata: document.getElementById("clave-producto").value })
    })
        .then(res => res.json())
        .then(data => {
            console.log(data, "holas");
            const resultado = document.getElementById("resultado2");
            if (data.valida) {
                resultado.innerText = data.mensaje;
                resultado.style.color = "lightgreen";
            } else {
                resultado.innerText = data.error + "\n" + data.mensaje;
                resultado.style.color = "salmon";
            }
        });
    document.getElementById("clave-producto").value = "";

})

