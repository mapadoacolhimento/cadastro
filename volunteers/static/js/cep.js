$(document).ready(function () {
  $("[data-validate-zipcode]").on("input", function (evt) {
    const $formField = $(evt.target).parent();
    const cep = $(evt.target).val().replace("-", "");

    if (cep.length === 8) {
      const endpoint = "https://brasilapi.com.br/api/cep/v1";

      console.log("Buscando dados em: ", endpoint);
      $.ajax(`${endpoint}/${cep}`, {
        statusCode: {
          404: function () {
            handleInvalidCep($formField);
          }
        }
      }).done(function (data) {
        console.log("Dados encontrados: ", data);

        $formField.find(".is-zipcode-error").remove();
        updateFormField($("[name=state]"), data.state.toUpperCase());
        updateFormField($("[name=city]"), data.city.toUpperCase());
        updateFormField($("[name=neighborhood]"), data.neighborhood.toUpperCase());

        allowFormSubmission($formField);
      });
    } else {
      handleInvalidCep($formField);
    }
  });

  function handleInvalidCep($formField) {
    const htmlError = '<span class="field-error is-zipcode-error">CEP Inválido</span>';
    $formField.find(".is-zipcode-error").remove();
    $("[name=state], [name=city], [name=neighborhood]").val("").hide();
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
