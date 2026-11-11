document.addEventListener("DOMContentLoaded", function() {
  // Legge i parametri dell'URL (MkDocs usa 'h' o 'highlight' per la ricerca)
  var urlParams = new URLSearchParams(window.location.search);
  var query = urlParams.get('h') || urlParams.get('highlight');

  if (query) {
    // Attende che la pagina e le evidenziazioni <mark> siano pronte
    setTimeout(function() {
      var highlightedElement = document.querySelector("mark");
      
      if (highlightedElement) {
        // Fa uno scroll fluido portando la parola trovata al centro dello schermo
        highlightedElement.scrollIntoView({
          behavior: "smooth",
          block: "center"
        });
      }
    }, 400);
  }
});
