const bg1 = STATIC_URL + 'images/bg.png';
const bg2 = STATIC_URL + 'images/bg2.png';

const navLinks = document.querySelectorAll('.nav-center li a');

navLinks.forEach(link => {
    link.addEventListener('click', (event) => {
        event.preventDefault(); // Prevent the default behavior of jumping to the section
        
        // Remove 'active' class from all links
        navLinks.forEach(nav => nav.classList.remove('active'));

        // Add 'active' class to the currently clicked link
        link.classList.add('active');

        // Scroll to the target section
        const targetId = link.getAttribute('href').substring(1); // Extract ID from href
        const targetSection = document.getElementById(targetId);

        if (targetSection) {
            window.scrollTo({
                top: targetSection.offsetTop - 90, // Adjust for navbar height
                behavior: 'smooth'
            });
        } else {
            console.warn(`Section with ID "${targetId}" not found.`);
        }
    });
});

// scroll scrolling
document.addEventListener('DOMContentLoaded', () => {
    const sections = document.querySelectorAll('.section');
    const navLinks = document.querySelectorAll('.nav-item');
    const sectionMapping = {
        home: ['home'],
        about: ['about', 'skills'],
        projects: ['projects'],
        contact: ['contact'],
    };

    const offset = 90; // Adjust scroll position upwards by 90 pixels

    const scrollToSection = (targetIndex) => {
        if (targetIndex >= 0 && targetIndex < sections.length) {
            const targetSection = sections[targetIndex];
            window.scrollTo({
                top: targetSection.offsetTop - offset, // Apply offset
                behavior: 'smooth',
            });
        }
    };

    let currentSectionIndex = 0;

    // Add scroll event listener
    document.addEventListener('wheel', (event) => {
        event.preventDefault();
        let targetIndex = currentSectionIndex;

        if (event.deltaY > 0 && currentSectionIndex < sections.length - 1) {
            targetIndex++;
        } else if (event.deltaY < 0 && currentSectionIndex > 0) {
            targetIndex--;
        }

        const currentSection = sections[currentSectionIndex];
        const nextSection = sections[targetIndex];
        
        const currentLink = Object.keys(sectionMapping).find(key =>
            sectionMapping[key].includes(currentSection.id)
        );
        const nextLink = Object.keys(sectionMapping).find(key =>
            sectionMapping[key].includes(nextSection.id)
        );

        if (currentLink !== nextLink) {
            navLinks.forEach(link => link.classList.remove('active'));
            document.querySelector(`.nav-item[href="#${nextLink}"]`).classList.add('active');
        }

        currentSectionIndex = targetIndex;
        scrollToSection(targetIndex);
    }, { passive: false });
});

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

