$(document).ready(function(){
  function loadCities() {
    var selectedState = $('#id_state').val();
    $.ajax({
      url: '/get_cities_for_state/',
      data: {'state': selectedState},
      success: function(data) {
        var citySelect = $('#id_city');
        citySelect.empty();
        $.each(data.cities, function(index, city) {
          citySelect.append($('<option>', {
            value: city.city_value,
            text: city.city_label
          }));
        });
      }
    });
  }

  loadCities();

  $('#id_state').change(function(){
    loadCities();
  });
});
