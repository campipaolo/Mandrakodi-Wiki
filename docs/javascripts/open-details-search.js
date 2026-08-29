document.addEventListener("DOMContentLoaded", function () {
  // Funzione per aprire il blocco details se contiene il target o un'evidenziazione
  function openParentDetails() {
    // Se c'è un elemento target nell'URL (es. #sezione)
    if (window.location.hash) {
      var target = document.querySelector(window.location.hash);
      if (target) {
        var details = target.closest("details");
        if (details) {
          details.setAttribute("open", "");
        }
      }
    }

    // Se la ricerca ha evidenziato dei termini con il tag <mark>
    var marks = document.querySelectorAll("mark");
    marks.forEach(function (mark) {
      var details = mark.closest("details");
      if (details) {
        details.setAttribute("open", "");
      }
    });
  }

  // Esegui al caricamento della pagina
  openParentDetails();

  // Esegui ogni volta che cambia l'hash nell'URL (es. quando si clicca su un risultato di ricerca)
  window.addEventListener("hashchange", openParentDetails);
});
