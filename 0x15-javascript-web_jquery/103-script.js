$(document).ready(() => {
  function enter () {
    const lang = $('input#language_code').val();
    $.getJSON(`https://www.fourtonfish.com/hellosalut/?lang=${lang}`, (data) => {
      $('div#hello').html(data.hello);
    });
  }
  $('input#btn_translate').click(enter);
  $('input#language_code').keyup((event) => {
    if (event.keyCode === 13) enter();
  });
});