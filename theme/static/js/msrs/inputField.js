// Adicione um evento de carga do documento
document.addEventListener('DOMContentLoaded', function () {
  const inputFields = document.querySelectorAll('.input-field');

  inputFields.forEach((inputField) => {
    const label = inputField.nextElementSibling;

    // Verifique se o campo está vazio ao carregar a página
    if (!inputField.value) {
      label.style.transform = 'translate(-50%, -50%)'; // Rótulo centralizado
      label.style.color = '#999'; // Cor cinza para o texto do rótulo
    }

    // Adicione eventos de foco e desfoque
    inputField.addEventListener('focus', () => {
      label.style.transform = 'translate(-50%, -80%) scale(0.75)'; // Mova o rótulo para cima e reduza o tamanho
      label.style.color = '#5b225b'; // Cor roxa quando em foco
    });

    inputField.addEventListener('blur', () => {
      if (!inputField.value) {
        label.style.transform = 'translate(-50%, -50%)'; // Rótulo centralizado
        label.style.color = '#999'; // Cor cinza quando não em foco
      }
    });
  });
});
