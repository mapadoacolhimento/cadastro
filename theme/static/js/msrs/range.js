function updateRangeValue(value) {
  const rangeValue = document.getElementById('range-value');
  const incomeValue = document.getElementById('id_11-income');
  const formattedValue = formatCurrency(value);
  rangeValue.textContent = formattedValue;
  incomeValue.value = (value/100).toFixed(2);
  console.log((value/100).toFixed(2))
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
