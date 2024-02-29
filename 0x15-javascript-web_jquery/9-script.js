$(document).ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function getData (data) {
    $('DIV#hello').text(data.hello);
  });
});
