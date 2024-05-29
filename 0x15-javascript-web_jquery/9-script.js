// script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr
// and displays the value of hello from that fetch in the HTML tag DIV#hello.
// new king url: https://hellosalut.stefanbohacek.dev/?lang=fr
/* global $ */

$(() => {
  $.get(
    "https://hellosalut.stefanbohacek.dev/?lang=fr",
    function (data, textStatus) {
      $("DIV#hello").text(data.hello);
    }
  );
});
