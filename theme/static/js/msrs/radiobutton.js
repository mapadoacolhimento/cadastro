document.addEventListener('DOMContentLoaded', function() {
    var radioButtons = document.querySelectorAll('.custom-radio input[type="radio"]');

    radioButtons.forEach(function(radioButton) {
        radioButton.addEventListener('change', function() {
            var labelSelected = document.querySelectorAll('.selected')
            labelSelected.forEach(function(label) {
                label.classList.remove('selected');
            })

            var label = this.parentElement;
            label.classList.remove('selected');

            if (this.checked) {
                label.classList.add('selected');
            }
        });
    });
  });

