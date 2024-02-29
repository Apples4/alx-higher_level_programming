$(document).ready(function addColor () {
  $('DIV#toggle_header').click(function colorChange () {
    if ($('HEADER').attr('class') !== 'red') {
      $('HEADER').attr('class', 'red');
    } else {
      $('HEADER').attr('class', 'green');
    }
  });
});
