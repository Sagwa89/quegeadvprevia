const siteHeader = document.querySelector('header');
const heroSection = document.querySelector('.hero');
if(siteHeader && heroSection){
  const toggleHeader = function(){
    const heroBottom = heroSection.getBoundingClientRect().bottom;
    if(heroBottom <= siteHeader.offsetHeight){
      siteHeader.classList.add('scrolled');
    } else {
      siteHeader.classList.remove('scrolled');
    }
  };
  toggleHeader();
  window.addEventListener('scroll', toggleHeader, {passive:true});
}

(function(){
  const revealEls = document.querySelectorAll('.reveal-up');
  if(!revealEls.length) return;
  if(!('IntersectionObserver' in window)){
    revealEls.forEach(function(el){ el.classList.add('is-visible'); });
    return;
  }
  const io = new IntersectionObserver(function(entries){
    entries.forEach(function(entry){
      if(entry.isIntersecting){
        entry.target.classList.add('is-visible');
        io.unobserve(entry.target);
      }
    });
  }, {threshold:0.3});
  revealEls.forEach(function(el){ io.observe(el); });
})();

(function(){
  const h1 = document.querySelector('.hero h1');
  const svg = document.getElementById('heroUnderline');
  const path = document.getElementById('heroUnderlinePath');
  if(!h1 || !svg || !path) return;
  const spans = h1.querySelectorAll(':scope > span');
  if(spans.length < 2) return;
  let loopTimer, restartTimer;

  function buildPath(){
    const h1Rect = h1.getBoundingClientRect();
    const r2 = spans[1].getBoundingClientRect();
    const pad = 8;
    const R = (r2.height / 2) + pad;
    const cy = (r2.top + r2.bottom) / 2 - h1Rect.top;
    const leftX = r2.left - h1Rect.left;
    const rightX = r2.right - h1Rect.left;
    const topY = cy - R;
    const botY = cy + R;
    const arcSteps = 24;
    let pts = [];
    pts.push(leftX.toFixed(1) + ',' + topY.toFixed(1));
    pts.push(rightX.toFixed(1) + ',' + topY.toFixed(1));
    for(let i = 1; i <= arcSteps; i++){
      const t = (180 * i / arcSteps);
      const rad = t * Math.PI / 180;
      pts.push((rightX + R * Math.sin(rad)).toFixed(1) + ',' + (cy - R * Math.cos(rad)).toFixed(1));
    }
    pts.push(leftX.toFixed(1) + ',' + botY.toFixed(1));
    for(let i = 1; i <= arcSteps; i++){
      const t = 180 + (180 * i / arcSteps);
      const rad = t * Math.PI / 180;
      pts.push((leftX + R * Math.sin(rad)).toFixed(1) + ',' + (cy - R * Math.cos(rad)).toFixed(1));
    }
    const d = `M ${pts[0]} L ${pts.join(' L ')}`;
    path.setAttribute('d', d);
    return path.getTotalLength();
  }

  function run(){
    const len = buildPath();
    path.style.transition = 'none';
    path.style.strokeDasharray = len;
    path.style.strokeDashoffset = len;
    path.style.opacity = '1';
    path.getBoundingClientRect();
    requestAnimationFrame(function(){
      path.style.transition = 'stroke-dashoffset .55s linear';
      path.style.strokeDashoffset = '0';
    });
    loopTimer = setTimeout(function(){
      path.style.transition = 'opacity 1.4s ease';
      path.style.opacity = '0';
    }, 550 + 200);
    restartTimer = setTimeout(run, 550 + 200 + 1400 + 800);
  }

  let resizeTimer;
  window.addEventListener('resize', function(){
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function(){
      clearTimeout(loopTimer);
      clearTimeout(restartTimer);
      run();
    }, 200);
  });

  if(document.fonts && document.fonts.ready){
    document.fonts.ready.then(run);
  } else {
    run();
  }
})();

const quoteText = document.querySelector('.quote-text');
if(quoteText){
  const quoteObserver = new IntersectionObserver(function(entries){
    entries.forEach(function(entry){
      if(entry.isIntersecting) entry.target.classList.add('in-view');
    });
  }, {threshold:.4});
  quoteObserver.observe(quoteText);
}

const areasSection = document.getElementById('areas');

document.querySelectorAll('.faq-q').forEach(function(btn){
  btn.addEventListener('click', function(){
    var item = btn.closest('.faq-item');
    item.classList.toggle('open');
    
    // Troca o background dinamicamente com base no atributo data-bg
    var bgImg = btn.getAttribute('data-bg');
    if(bgImg) {
      areasSection.style.backgroundImage = `linear-gradient(rgba(10,11,12,.65),rgba(10,11,12,.8)), url('${bgImg}')`;
    }
  });
});
</script>
