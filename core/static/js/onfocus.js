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

      var fields = document.querySelectorAll('input,select');
      fields.forEach((x) =>{
        if(x.value){
          var target = $(x).data('target');
          this.placeholder = "";
          $('[tag="' + target + '"]').removeClass('hidden');
           
        }
      }
        
      );

 });
