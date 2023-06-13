$(document).ready(function() {
    $('input').focus(function() {
         var target = $(this).data('target');
         $('[tag="' + target + '"]').removeClass('hidden');
     });

     $('input').blur(function() {
         var target = $(this).data('target');
         if (!this.value){
          $('[tag="' + target + '"]').addClass('hidden');
         }
         
      });
 });
