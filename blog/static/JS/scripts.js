
  function toggleMenu() {
    const menu = document.getElementById("navLinks");
    menu.classList.toggle("show");
  }


document.addEventListener('DOMContentLoaded', function () {
const slides = document.querySelectorAll('.carousel-slide');
let currentSlide = 0;

    function showSlide(index) {
        slides.forEach((slide, i) => {
            slide.classList.remove('active');
            slide.style.opacity = '0';
        });
        if (slides[index]) {
            slides[index].classList.add('active');
            slides[index].style.opacity = '1';
        }
    }

    setInterval(() => {
        currentSlide = (currentSlide + 1) % slides.length;
        showSlide(currentSlide);
    }, 6000); 
});
