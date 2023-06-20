document.addEventListener("keydown", function(event) {
  if (event.key === "Enter") {
    event.preventDefault(); // Impede a ação padrão da tecla "Enter"
    document.getElementById("continue-btn").click(); // Ativa o botão "Continuar"
  }
});
