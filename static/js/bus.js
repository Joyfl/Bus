function filter(tag)
{
	var seats;
	$("#filter").find("li").removeClass("active");
	$("#filter").find("[tag='%s']".$(tag)).addClass("active");
	if(tag == "all") seats = $(".seat");
	else seats = $(".seat").filter("[tag='%s']".$(tag));
	$(".seat").hide();
	$(".seat").removeClass("strip");
	var len = seats.length;
	for(var i = 0; i < len; i += 2) $(seats[i]).addClass("strip");
	seats.show();
}