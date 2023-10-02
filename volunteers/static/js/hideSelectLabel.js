function hideSelectLabel(value, name) {

  if (!value) {
     document.getElementById(`label_${name}`).classList.add('hidden');
   } else {
     document.getElementById(`label_${name}`).classList.remove('hidden');
     ;
   }
}
