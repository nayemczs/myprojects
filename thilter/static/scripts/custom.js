(function($) {
    "use strict";
	const slideRanger = document.querySelectorAll('.sliders')
	$(function() {
		slideRanger.forEach(element => {
      $(element.querySelector('.slider-range')).slider({
        range: true,
        min: 0,
        max: 400,
        values: [0, 400],
        slide: function(event, ui) {
          $(element.querySelector('.amount_low')).val(ui.values[0]);
          $(element.querySelector('.amount_high')).val(ui.values[1]);
        }
      })
    })
	})
}(jQuery));