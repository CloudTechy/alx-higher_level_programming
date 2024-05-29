// script that fetches the character name from this
// URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
/* global $ */

$.get(
  'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  function (data, textStatus) {
    $('DIV#character').text(data.name);
  }
);
