  var currentStep = {{ step }};

  if (currentStep === 10) {

      var nextStep = currentStep + 1;


      setTimeout(function() {
          window.location.href = window.location.pathname.replace(currentStep, nextStep);
      }, 4000);
  }
