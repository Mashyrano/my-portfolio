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

document.addEventListener('wheel', (event) => {
    event.preventDefault(); // Prevent the default scroll behavior

    // Get all sections
    const sections = document.querySelectorAll('.section');

    // Get the current scroll position
    const currentScroll = window.pageYOffset;

    // Determine the index of the current section
    let currentSectionIndex = Array.from(sections).findIndex((section) => {
        const sectionTop = section.offsetTop;
        const sectionBottom = sectionTop + section.offsetHeight;

        return currentScroll >= sectionTop && currentScroll < sectionBottom;
    });

    if (event.deltaY > 0) {
        // Scroll down
        currentSectionIndex = Math.min(currentSectionIndex + 1, sections.length - 1);
    } else {
        // Scroll up
        currentSectionIndex = Math.max(currentSectionIndex - 1, 0);
    }

    // Scroll to the target section
    const targetSection = sections[currentSectionIndex];
    window.scrollTo({
        top: targetSection.offsetTop,
        behavior: 'smooth'
    });
}, { passive: false });
