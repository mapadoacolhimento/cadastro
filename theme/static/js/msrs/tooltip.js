function showTooltip(step) {
  const tooltip = document.getElementById(`tooltip-content-${step}`);
  const arrow = tooltip.previousElementSibling.querySelector('svg');
  tooltip.style.display = 'block';
  arrow.classList.add('rotate-180');
}

function hideTooltip(step) {
  const tooltip = document.getElementById(`tooltip-content-${step}`);
  const arrow = tooltip.previousElementSibling.querySelector('svg');
  tooltip.style.display = 'none';
  arrow.classList.remove('rotate-180');
}
