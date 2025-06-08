export async function loadPage(url, container, borrar) {
    try {
      
      const response = await fetch("./static/html/play.html");
      console.log(container);
      
      if (!response.ok) {
        throw new Error("Failed to load page");
      }
      const html = await response.text();
      if (container) {
        if (borrar) {
          container.innerHTML = ""; 
        }
        let contenidoInterno = container.innerHTML;
        contenidoInterno += html;
        container.innerHTML = contenidoInterno;
      }
    } catch (error) {
      console.error(error,"hola");
    }
  }
  