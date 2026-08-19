// Tema claro/escuro persistido no navegador
(function(){
  const root = document.documentElement;
  const saved = localStorage.getItem('quege-theme');
  if(saved === 'dark'){ root.setAttribute('data-theme','dark'); }

  document.addEventListener('DOMContentLoaded', function(){
    const btn = document.querySelector('.theme-toggle');
    if(btn){
      updateIcon();
      btn.addEventListener('click', function(){
        const isDark = root.getAttribute('data-theme') === 'dark';
        if(isDark){ root.removeAttribute('data-theme'); localStorage.setItem('quege-theme','light'); }
        else { root.setAttribute('data-theme','dark'); localStorage.setItem('quege-theme','dark'); }
        updateIcon();
      });
    }
    function updateIcon(){
      if(!btn) return;
      btn.textContent = root.getAttribute('data-theme') === 'dark' ? '☀' : '☾';
    }

    // menu mobile
    const menuBtn = document.querySelector('.menu-toggle');
    const links = document.querySelector('nav.links');
    if(menuBtn && links){
      menuBtn.addEventListener('click', function(){
        const open = links.style.display === 'flex';
        links.style.display = open ? 'none' : 'flex';
        links.style.flexDirection = 'column';
        links.style.position = 'absolute';
        links.style.top = '68px';
        links.style.left = '0';
        links.style.right = '0';
        links.style.background = 'var(--bg)';
        links.style.padding = '20px 24px';
        links.style.borderBottom = '1px solid rgba(0,0,0,.08)';
      });
    }
  });
})();

// Calculadora de redução de impostos na revenda de veículos (página Utilitários)
function calcularRevenda(){
  const compra = parseFloat(document.getElementById('valorCompra').value) || 0;
  const venda = parseFloat(document.getElementById('valorVenda').value) || 0;
  const aliquota = parseFloat(document.getElementById('aliquota').value) || 0;

  const margem = Math.max(venda - compra, 0);
  const impostoTotal = venda * (aliquota / 100);
  const impostoMargem = margem * (aliquota / 100);
  const economia = Math.max(impostoTotal - impostoMargem, 0);

  const fmt = v => v.toLocaleString('pt-BR', { style:'currency', currency:'BRL' });

  document.getElementById('resMargem').textContent = fmt(margem);
  document.getElementById('resImpostoTotal').textContent = fmt(impostoTotal);
  document.getElementById('resImpostoMargem').textContent = fmt(impostoMargem);
  document.getElementById('resEconomia').textContent = fmt(economia);
}

document.addEventListener('DOMContentLoaded', function(){
  const form = document.getElementById('calcForm');
  if(form){
    form.addEventListener('input', calcularRevenda);
    calcularRevenda();
  }
});
