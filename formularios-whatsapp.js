(function () {
  var forms = document.querySelectorAll('form[action^="https://formsubmit.co/"]');

  forms.forEach(function (form) {
    var button = form.querySelector('button[type="submit"]');
    if (button) button.textContent = 'Continuar no WhatsApp';

    form.addEventListener('submit', function (event) {
      event.preventDefault();
      if (!form.reportValidity()) return;

      var title = form.id === 'orcamentoForm'
        ? 'Solicitação de orçamento de curso pelo site da Quege'
        : 'Contato pelo site da Quege';
      var lines = [title];

      new FormData(form).forEach(function (value, name) {
        var text = String(value).trim();
        if (!name || name.charAt(0) === '_' || !text) return;
        lines.push((name === 'email' ? 'E-mail' : name) + ': ' + text);
      });

      if (typeof window.trackSiteEvent === 'function') {
        window.trackSiteEvent('whatsapp_form_open', {form_id: form.id || 'formulario'});
      }

      window.location.assign('https://wa.me/5547984033110?text=' + encodeURIComponent(lines.join('\n')));
    });
  });
})();
