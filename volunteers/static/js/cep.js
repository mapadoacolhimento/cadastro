$(document).ready(function () {
  $("[data-validate-zipcode]").on("focusout", function (evt) {
    const $formField = $(evt.target).parent();

    let cep = $(evt.target).val();

    if (cep.length === 9) {
      cep = cep.replace("-", "")
      var endpoint = window.location.toString()
      endpoint = endpoint.substring(0, endpoint.indexOf('/',8)) + '/address/'
    
      console.log("Buscando dados em: ", endpoint);

      $.ajax( endpoint + "?zipcode=" + cep, {
        statusCode: {
          404: function () {
            const htmlError = '<span class="field-error is-zipcode-error">CEP Não encontrado</span>';

            $(evt.target).after(htmlError)
          }
        }
      }).done(function (data) {
        console.log("Dados encontrados: ", data);
      })
    }
  })
});