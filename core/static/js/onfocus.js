$(document).ready(function() {
    $('input, select').focus(function() {
         var target = $(this).data('target');
         this.placeholder = "";
         $('[tag="' + target + '"]').removeClass('hidden');
     });

     $('input, select').blur(function() {
         var target = $(this).data('target');
         this.placeholder = target;
         if (!this.value){
          $('[tag="' + target + '"]').addClass('hidden');
         }
         
      });
 });
