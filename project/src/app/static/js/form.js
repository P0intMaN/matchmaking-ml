$(document).ready(function() {
    $('#match-form').click(function(event) {
      event.preventDefault();
      $.ajax({
        type: 'POST',
        url: '/match',
        data: {
            profile1: $('#profile1').val(),
            profile2: $('#profile2').val()
          },
        success: function(response) {
          var resultDiv = $('#result');
          if (response.result == 0) {
            resultDiv.text('Dissimilar');
            resultDiv.removeClass('text-success').addClass('text-danger');
          } else {
            resultDiv.text('Similar');
            resultDiv.removeClass('text-danger').addClass('text-success');
          }
        }
      });
    });
  });
  