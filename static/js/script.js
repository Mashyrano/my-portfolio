const bg1 = STATIC_URL + 'images/bg.png';
const bg2 = STATIC_URL + 'images/bg2.png';

$(document).ready(function () {
    $('#myImage').mouseenter(function () {
        $('#myImage').attr("src", bg2);
        $('.nav').css('background', 'linear-gradient(180deg, red, white)');
        $('.nav-item').css('color','black');
        $('.home-section').css('background', 'linear-gradient(white, red)');
    });
    $('#myImage').mouseleave(function () {
        $('#myImage').attr("src", bg1);
        $('.nav').css('background-color','black');
        $('.nav-item').css('color','white');
        $('.home-section').css('background', 'linear-gradient(to right bottom, black, white)');
        $('.nav').css('background', 'black');
    });

});