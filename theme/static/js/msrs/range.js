function updateRangeValue(value) {
  const rangeValue = document.getElementById('range-value');
  const formattedValue = formatCurrency(value);
  rangeValue.textContent = formattedValue;
}

function formatCurrency(amount) {
  const formatter = new Intl.NumberFormat('pt-BR', {
    style: 'currency',
    currency: 'BRL',
    minimumFractionDigits: 2,
  });
  return formatter.format(amount / 100);
}

updateRangeValue(document.getElementById('range-slider').value);
