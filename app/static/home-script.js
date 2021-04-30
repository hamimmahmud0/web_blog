
let pjtAnimeSeed = 1
let pjtAnimeSpeed = 0.1;
let pjtAnimetxt = "PROJECTS_SO_FAR";
let seed = "0123456789";//"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
var D = new Date();

var pjtAnimeD = 0;
function pjtAnimeTxtAnimate(timestamp) {	

	let len = pjtAnimetxt.length;
	let randomLen = Math.floor(len*pjtAnimeSeed);
	let finalLen = len - randomLen;
	let randomtxt = '';
	let finaltxt = '';

	for (var i = 0; i < randomLen; i++) {
		randomtxt += randomchar();
	}

	finaltxt = pjtAnimetxt.substring(pjtAnimetxt.length-finalLen,pjtAnimetxt.length)

	$("#pjt-slide-text").text(randomtxt+finaltxt);


	if(pjtAnimeSeed == 0)
	{
		return;
	}

	
		pjtAnimeD = D.getMilliseconds();
		pjtAnimeSeed = pjtAnimeSeed - pjtAnimeSpeed;

	
	if(pjtAnimeSeed < .01) {
		pjtAnimeSeed = 0;
	}

}
				

function randomchar() {
	let x = Math.floor( (Math.random() * seed.length));
	return seed.charAt(x);
}

setInterval(pjtAnimeTxtAnimate,150);


var abtMe = $(".abt-me");
var abtMeTxt = abtMe.text();
var abtAnimeSeed =  1;
var abtComp = false;

abtMe.text("000");

function abtMeAnimate(timestamp) {	

	if(abtComp) {return;}

	let len = abtMeTxt.length;
	let randomLen = Math.floor(len*abtAnimeSeed);
	let finalLen = len - randomLen;
	let randomtxt = '';
	let finaltxt = '';

	for (var i = 0; i < randomLen; i++) {
		randomtxt += randomchar();
	}
	finaltxt = abtMeTxt.substring(abtMeTxt.length-finalLen,abtMeTxt.length)

	abtMe.text(randomtxt+finaltxt);


	if(abtAnimeSeed == 0)
	{
		abtComp = true;
	}

	
		pjtAnimeD = D.getMilliseconds();
		abtAnimeSeed = abtAnimeSeed - pjtAnimeSpeed;

	
	if(abtAnimeSeed < .01) {
		abtAnimeSeed = 0;
	}

}

var cntMe = $(".cnt-me");
var cntMeTxt = cntMe.text();
var cntAnimeSeed =  1;
var cntComp = false;

cntMe.text("000");

function cntMeAnimate(timestamp) {	

	if(cntComp) {return;}

	let len = cntMeTxt.length;
	let randomLen = Math.floor(len*cntAnimeSeed);
	let finalLen = len - randomLen;
	let randomtxt = '';
	let finaltxt = '';

	for (var i = 0; i < randomLen; i++) {
		randomtxt += randomchar();
	}
	finaltxt = cntMeTxt.substring(cntMeTxt.length-finalLen,cntMeTxt.length)

	cntMe.text(randomtxt+finaltxt);


	if(cntAnimeSeed == 0)
	{
		cntComp = true;
	}

	
		pjtAnimeD = D.getMilliseconds();
		cntAnimeSeed = cntAnimeSeed - pjtAnimeSpeed;

	
	if(cntAnimeSeed < .01) {
		cntAnimeSeed = 0;
	}

}

//project-slide

var slidermousedown = false;
var sliderlastx = 0;
var slider = $(".slider");
var cardW = $(".card").width() + 10;
var tar = 0;
var pjtslider = $(".slider")
pjtslider.bind('mousedown', function(event) {
	slidermousedown = true;
	sliderlastx = event.clientX;
});

$(document).bind('mouseup', function(event) {
	slidermousedown = false;
	sliderlastx = 0;
	count = 0;
	setInterval(slideAnimate,30);
});

$(document).bind('mousemove', function(event) {
	if(slidermousedown) {
		var diff = sliderlastx - event.clientX;
		sliderlastx = event.clientX;
		var left = slider.position().left - diff/$(window).width()*700;


		var factor = -left/cardW + 60/cardW;
		if($(window).width() > 768) {
			factor = -left/cardW + (60 + $(".menubar").width())/cardW;
		}
		factor = Math.round(factor);
		tar = 50 - factor*cardW;

		if(slider.position().left > 50 + $(window).width()/5) {
			left =slider.position().left + left/(slider.position().left - 50 + $(window).width()/5)/10;
		}
		var right = (slider.width() + slider.position().left);

		if(right < 200 + $(window).width()/5) {
			left =slider.position().left;
		}

		slider.css({
			'left' : left + 'px'
		});

		//console.log(-left/cardW + 60/cardW);

	}
});

var count = 0;

function slideAnimate(timestamp) {
	if(count * 30 > 1500) {
		return;
	}
	count += 1;
	var left = tar - slider.position().left;
	left = (Math.abs(left) < 1) ? 1*left/left : left;
	//console.log(left);
	left = left  * .1;

	left = slider.position().left + left;
		slider.css({
			'left' : left + 'px'
		});

}