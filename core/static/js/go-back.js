document.addEventListener("DOMContentLoaded", function() {
  var backButton = document.getElementById("backButton");

  if (backButton) {
    backButton.addEventListener("click", function() {
      window.history.go(-1);
    });
  }
});
