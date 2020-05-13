/**
 * Created by Sergey on 14-Oct-16.
 */

(function () {
   $(window).ready(init);
})();

function init() {
/*
	$('#puzzle-board').puzzle({
        image: 'puzle/images/landscape_02.jpg',
        size: 250,
        scale: 1
    });*/


$('.complexity_btn').on('click', function(e){
  app.open_mobile_menu()
  e.preventDefault()

  $('.puzzle-group').remove() // for bug sometimes game not ended
  $('.img_end').remove() // remove concide image
  $('#concide_image').remove() // remove concide image div

  $('.lose').fadeOut();
  $('.complexity_btn').removeClass('active_complexity_btn');
	$('#puzzle-board svg').remove()
	$('.complexity_btn').removeClass('active');
  $('.complexity_btn').prop('disabled', true);
  $(this).addClass('active_complexity_btn')

  var lengthPuzle = $(this).data('puzle');
  let data = sessionStorage.getItem('key');

  $.ajax({
    method: "POST",
    url: "/game/start/",
    dataType: "json",
    data: {'puzzle_length': lengthPuzle},
    headers: { 'X-CSRFToken':document.getElementsByName('csrfmiddlewaretoken')[0].value },
    success: function(response) {
      if (response.code == 200)
      {
        var level = response.level;
        var parAmt = level * 10;
        if (typeof timeloop !== 'undefined')
          if (timeloop)
            clearTimeout(timeloop)

        sessionStorage.setItem('level', level);
        image_url = response.image

        var scale = (screen.height / 1080).toFixed(1)
          console.log('scale',scale)
        sessionStorage.setItem('puzzle_size', scale*100);

        $('#puzzle-board').puzzle({
        	image: image_url,
        	size: lengthPuzle,
        	scale: scale
        });

        totalAmount = parAmt * 60;
        timeSet();
      }
      else if (response.code == 400)
        alert(response.error)
      else
        alert('Unexpected error.')
    }
  })
})


}
