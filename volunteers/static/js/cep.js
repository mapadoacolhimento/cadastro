$(document).ready(function () {

  function loadCities(city) {
    var selectedState = $('#id_state').val();
    $.ajax({
      url: '/get_cities_for_state/',
      data: {'state': selectedState},
      success: function(data) {
        var citySelect = $('#id_city');
        citySelect.empty();
        citySelect.append('<option> Selecione uma cidade </option>')
        $.each(data.cities, function(index, city) {
          citySelect.append($('<option>', {
            value: city.value,
            text: city.label
          }));
        });
      }
    }).done(function () {
        if(city){ 
          $("[name=city]").val(city.toUpperCase())
          document.getElementById('label_city').classList.remove('hidden');
        }
    }
    );
  }
 
  function updateFormField($field, value) {
    $field.val(value).show();
  }


  function loadAddress (zipcodeField) {
    
    const $formField = $(zipcodeField).parent();
    const cep = $(zipcodeField).val().replace("-", "");

    if (cep.length === 8) {
      var endpoint = window.location.toString()
      endpoint = endpoint.substring(0, endpoint.indexOf('/',8)) + '/address/'

      console.log("Buscando dados em: ", $("[name=state]"));
      $.ajax(`${endpoint}?zipcode=${cep}`, {
        statusCode: {
          404: function () {
            const htmlError = '<span class="field-error is-zipcode-error">CEP Não encontrado</span>';

            $(zipcodeField).after(htmlError)
          }
        }
      }).done(async function (data) {
        console.log("Dados encontrados: ", data);

        $formField.find(".is-zipcode-error").remove();
        updateFormField($("[name=state]"), data.state.toUpperCase());
        document.getElementById('label_state').classList.remove('hidden');
        loadCities( data.city.toUpperCase())
       
        updateFormField($("[name=neighborhood]"), data.neighborhood.toUpperCase());
        $("[name=street]").val(data.street?.toUpperCase());
        $("[name=lat]").val(data.coordinates.lat);
        $("[name=lng]").val(data.coordinates.lng);

      });
    } 
  }


  //search when load the page and zipcode is filled
  if  ($("[data-validate-zipcode]").val()) {
    loadAddress($("[data-validate-zipcode]"))
  } 
  else {
    loadCities()
  }


  
  //search when input
  $("[data-validate-zipcode]").on("input",function(evt){
    loadAddress(evt.target)
  } );

  

 
});
