$(document).ready(function () {
  $("[data-validate-zipcode]").on("input", function (evt) {
    const $formField = $(evt.target).parent();
    const cep = $(evt.target).val().replace("-", "");

    if (cep.length === 8) {
      var endpoint = window.location.toString()
      endpoint = endpoint.substring(0, endpoint.indexOf('/',8)) + '/address/'

      console.log("Buscando dados em: ", endpoint);
      $.ajax(`${endpoint}?zipcode=${cep}`, {
        statusCode: {
          404: function () {
            handleInvalidCep($formField);
          }
        }
      }).done(async function (data) {
        console.log("Dados encontrados: ", data);

        $formField.find(".is-zipcode-error").remove();
        updateFormField($("[name=state]"), data.state.toUpperCase());
        document.getElementById('label_state').classList.remove('hidden');
        loadCities( data.city.toUpperCase())
        //updateFormField($("[name=city]"), data.city.toUpperCase());
       
        updateFormField($("[name=neighborhood]"), data.neighborhood.toUpperCase());
        $("[name=street]").val(data.street?.toUpperCase());
        $("[name=lat]").val(data.coordinates.lat);
        $("[name=lng]").val(data.coordinates.lng);

        allowFormSubmission($formField);
      });
    } else {
      handleInvalidCep($formField);
    }
  });

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
        $("[name=city]").val(city.toUpperCase())
        document.getElementById('label_city').classList.remove('hidden');
    }
    );
  }
  function handleInvalidCep($formField) {
    const htmlError = '<span class="field-error is-zipcode-error">CEP Inválido</span>';
    $formField.find(".is-zipcode-error").remove();
    $formField.find("[name=zipcode]").after(htmlError);

    blockFormSubmission($formField);
  }

  function updateFormField($field, value) {
    $field.val(value).show();
  }

  function blockFormSubmission($formField) {
    $formField.closest("form").submit(function (event) {
      event.preventDefault();
    });
  }

  function allowFormSubmission($formField) {
    $formField.closest("form").unbind("submit");
  }
});
