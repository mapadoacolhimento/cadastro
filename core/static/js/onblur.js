function required($element, message = "Required field", error_class = "field-error") {
    const $formField = $element.parent();

    const htmlError = '<span class="' + error_class + ' required-error">' + message + '</span>';

    if (!$element.val()) {
      // Remove old errors
      $formField.find('.required-error').hide();
      $formField.find('.django-error').hide();

      // Add new error
      $formField.find('.error-list').append(htmlError);
    } else {
      $formField.find('.required-error').hide();
      $formField.find('.django-error').hide();
    }
}


function isEmail($element, message = "Invalid field", error_class = "field-error") {
  const re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

  const $formField = $element.parent();

  const htmlError = '<span class="' + error_class + ' is-email-error">' + message + '</span>';

  if (!re.test($element.val())) {
    // Remove old errors
    $formField.find('.is-email-error').hide();
    $formField.find('.django-error').hide();

    // Add new error
    $formField.find('.error-list').append(htmlError);
  } else {
    $formField.find('.is-email-error').hide();
    $formField.find('.django-error').hide();
  }
}


function isZipCode($element, message = "Invalid zipcode", error_class = "field-error") {
  const re = /^[0-9]{5}-[0-9]{3}$/;

  const $formField = $element.parent();

  const htmlError = '<span class="' + error_class + ' is-zipcode-error">' + message + '</span>';

  if (!re.test($element.val())) {
    // Remove old errors
    $formField.find('.is-zipcode-error').hide();
    $formField.find('.django-error').hide();

    // Add new error
    $formField.find('.error-list').append(htmlError);
  } else {
    $formField.find('.is-zipcode-error').hide();
    $formField.find('.django-error').hide();
  }
}

$(document).ready(function () {

  $('[required]').on('blur', (evt) => {
    required($(evt.target));
  })

  $('[type="email"]').on('blur', (evt) => {
    isEmail($(evt.target));
  })

  $('[data-validate-zipcode]').on('blur', (evt) => {
    isZipCode($(evt.target));
  })
});