(function() {
  $(window).scroll(function(){
    $("#right-sidebar").stop().animate({"marginTop": ($(window).scrollTop()) + "px", "marginLeft":($(window).scrollLeft()) + "px"}, "slow" );
  });
})();