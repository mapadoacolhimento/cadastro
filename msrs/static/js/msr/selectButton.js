$(document).ready(function() {
  // Adiciona um ouvinte de eventos para todos os botões com a classe "choice-button"
  $('.choice-button').on('click', function() {
    // Encontre a caixa de seleção associada a este botão
    var checkbox = $(this).prev('input[type="checkbox"]');

    // Inverta o estado da caixa de seleção (selecionado / não selecionado)
    checkbox.prop('checked', !checkbox.prop('checked'));

    // Verifique se a caixa de seleção está marcada e aplique ou remova a classe "selected"
    if (checkbox.prop('checked')) {
      $(this).addClass('selected');
      $(this).css('background-color', '#C68CB9'); // Cor de fundo quando selecionado
    } else {
      $(this).removeClass('selected');
      $(this).css('background-color', ''); // Remove a cor de fundo quando desmarcado
    }
  });
});
