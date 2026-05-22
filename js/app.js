document.querySelectorAll('[data-carousel]').forEach(function (carousel) {
  const track = carousel.querySelector('.carousel-track');
  const slides = Array.from(carousel.querySelectorAll('.carousel-slide'));
  const prevBtn = carousel.querySelector('.carousel-prev');
  const nextBtn = carousel.querySelector('.carousel-next');
  let current = 0;

  function maxIndex() {
    const slideWidth = slides[0].offsetWidth;
    const visible = Math.round(carousel.offsetWidth / slideWidth);
    return Math.max(0, slides.length - visible);
  }

  function update() {
    const slideWidth = slides[0].offsetWidth;
    track.style.transform = 'translateX(-' + current * slideWidth + 'px)';
    prevBtn.disabled = current === 0;
    nextBtn.disabled = current >= maxIndex();
  }

  prevBtn.addEventListener('click', function () {
    if (current > 0) { current--; update(); }
  });

  nextBtn.addEventListener('click', function () {
    if (current < maxIndex()) { current++; update(); }
  });

  window.addEventListener('resize', function () {
    current = Math.min(current, maxIndex());
    update();
  });

  update();
});
