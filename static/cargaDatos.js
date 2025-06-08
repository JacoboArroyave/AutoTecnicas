import {cargarMatriz} from "./script.js"
import { loadPage } from "./Utils.js"

async function enviarArchivo() {
    const archivoInput = document.getElementById("archivo");
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
                    cargarMatriz(data,datos);

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
const button = document.getElementById("button")
console.log(button);

button.addEventListener("click", enviarArchivo)
let datos = ""