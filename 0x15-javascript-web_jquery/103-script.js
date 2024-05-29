// script that fetches and prints how to say “Hello”
// depending on the language that is passed as argument
// new working url: https://hellosalut.stefanbohacek.dev/
/* global $ */

$(() => {
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();

    const url = `https://hellosalut.stefanbohacek.dev/?lang=${lang}`;
    $.get(url, function (data, statusCode) {
      $('DIV#hello').text(data.hello);
    });
  });

  // The translation must be fetched when the user clicks on INPUT#btn_translate OR presses
  // ENTER when the focus is on INPUT#language_code
  $('INPUT#language_code').keypress(function (e) {
    if (e.which === 13) {
      $('INPUT#btn_translate').click();
    }
  });
});
