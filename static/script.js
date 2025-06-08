async function moverNave(caminos, delay = 300) {
    let anteriorPos = null;
    let anterior = null;
 
    for (const camino of caminos) {
       

        await cargarMatriz(window.ultimaMatriz, window.ultimosDatos);
        console.log(camino);

        for (const paso of camino) {
            console.log(paso);

            const [x, y] = paso;
            const pos = `${x},${y}`;

            const celda = document.querySelector(`[data-pos="${pos}"]`);
            console.log(celda, paso);


            // Quitar la nave de la posición anterior
            if (anterior) {
                const celdaAnt = document.querySelector(`[data-pos="${anteriorPos}"]`);
                if (celdaAnt) celdaAnt.innerHTML = ""; // Limpia la imagen
            } y

            anteriorPos = pos;
            // Poner la nave en la nueva celda
            anterior = celda
            console.log(anterior);
            celda.innerHTML = `<img src="/static/img/nave.webp" width="100%">`;


            await new Promise((res) => setTimeout(res, delay));
        }
    }
}
export async function cargarMatriz(matriz, datos) {
    window.ultimaMatriz = matriz;
    window.ultimosDatos = datos;
    const camino = matriz[1]
    matriz = matriz[0]
    const contenedor = document.getElementById("contenedor-matriz");
    contenedor.innerHTML = "";

    const filas = matriz.length;
    const columnas = matriz[0].length;
    localStorage.setItem("filas", filas)
    localStorage.setItem("columnas", columnas)

    let tamañoCelda = 40;
    if (columnas > 20) tamañoCelda = 30;
    if (columnas > 30) tamañoCelda = 25;
    if (columnas > 40) tamañoCelda = 20;

    contenedor.style.gridTemplateColumns = `repeat(${columnas}, ${tamañoCelda}px)`;

    // Convertir listas a sets/mapas para acceso rápido
    const estrellas = new Set(datos.estrellasGigantes.map(([x, y]) => `${x},${y}`));
    const agujeros = new Set(datos.agujerosNegros.map(([x, y]) => `${x},${y}`));
    const gusanos = new Set(datos.agujerosGusano.map(([entrada, _]) => `${entrada[0]},${entrada[1]}`));
    const recargas = new Map(datos.zonasRecarga.map(([x, y, c]) => [`${x},${y}`, c]));
    const origen = `${datos.origen[0]},${datos.origen[1]}`;
    const destino = `${datos.destino[0]},${datos.destino[1]}`;
    for (let i = 0; i < filas; i++) {
        for (let j = 0; j < columnas; j++) {
            const celda = document.createElement("div");
            celda.classList.add("celda");
            celda.setAttribute("data-pos", `${i},${j}`);

            celda.style.width = `${tamañoCelda}px`;
            celda.style.height = `${tamañoCelda}px`;
            celda.title = `(${i}, ${j})`;
            const key = `${i},${j}`;

            if (key === origen) {
                celda.style.backgroundColor = "transparent";
                celda.innerHTML = `<img src="/static/img/nave.webp" width="${tamañoCelda - 8}px">`;
            } else if (key === destino) {
                celda.style.backgroundColor = "#ff4d4d"; // color rojo destino
                celda.innerText = "🏁";
            } else if (estrellas.has(key)) {
                celda.style.backgroundColor = "transparent";
                celda.innerHTML = `<img src="/static/img/estrella.jpg" width="${tamañoCelda - 8}px">`;
            } else if (agujeros.has(key)) {
                celda.style.backgroundColor = "transparent";
                celda.innerHTML = `<img src="/static/img/agujero_negro.png" width="${tamañoCelda - 8}px">`;
            } else if (gusanos.has(key)) {
                celda.style.backgroundColor = "#6a1b9a";
                celda.innerText = "🌀";
            } else if (recargas.has(key)) {
                celda.style.backgroundColor = "#ffcc00";
                celda.innerText = recargas.get(key);
            } else {
                celda.innerText = matriz[i][j];
            }


            contenedor.appendChild(celda);
        }
    }
    const button = document.getElementById("button")
    button.addEventListener("click", () => moverNave(camino))

}





