$(document).ready(function() {
    // JQuery code to be added in here.

    const required_fields = ['first_name', 'email', 'phone_number', 'document_number']

    $("form input").on("blur", function(evt) {

        if (required_fields.includes(evt.target.name) && !evt.target.value) {
            $($(evt.target).prev(), '.error').hide();
            $(evt.target).after('<p class="error">este campo é obrigatorio</p>')
        } else {
            $($(evt.target).after(), '.error').hide();
        }
    });
});