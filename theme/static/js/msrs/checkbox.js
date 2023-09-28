document.addEventListener('DOMContentLoaded', function() {
  var checkboxes = document.querySelectorAll('.custom-checkbox input[type="checkbox"]');

  checkboxes.forEach(function(checkbox) {
      checkbox.addEventListener('change', function() {
          var label = this.parentElement;
          if (this.checked) {
              label.classList.add('selected');
          } else {
              label.classList.remove('selected');
          }
      });
  });
});
