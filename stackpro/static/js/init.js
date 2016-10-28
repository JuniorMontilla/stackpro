(function($){
  $(function(){
	$('.button-collapse').sideNav();
	$('.parallax').parallax();
	$('#home-navbar').pushpin({ top: 1 });
	$('.slider').slider({full_width: true});
	$('.scrollspy').scrollSpy();

	// - Animated anchor - //

	$(function(){
		$('a.anchor[href*=#]').click(function() {
		if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'')
			&& location.hostname == this.hostname) {
				var $target = $(this.hash);
				$target = $target.length && $target || $('[name=' + this.hash.slice(1) +']');
				if ($target.length) {
					var targetOffset = $target.offset().top;
					$('html,body').animate({scrollTop: (targetOffset -66)}, 800);
					$("#nav").children("li").removeClass("active");
					var id = $(this).attr("href").substr(1);
					$("#nav").children("li."+id).addClass("active");
					return false;
				}
			}
		});
	});

	// - Bavk to top - //

	if ($('#back-to-top').length) {
		var scrollTrigger = 100,
			backToTop = function () {
				var scrollTop = $(window).scrollTop();
				if (scrollTop > scrollTrigger) {
					$('#back-to-top').addClass('show');
				} else {
					$('#back-to-top').removeClass('show');
				}
			};
		backToTop();
		$(window).on('scroll', function () {
			backToTop();
		});
		$('#back-to-top').on('click', function (e) {
			e.preventDefault();
			$('html,body').animate({
				scrollTop: 0
			}, 700);
		});
	}

  });
})(jQuery);