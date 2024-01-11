const $ = window.$;
window.onload = function () {
  $('#btn_translate').click(function () {
    showHello();
  });
  $('#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      showHello();
    }
  });
};

function showHello () {
  const lan = $('#language_code').val();
  $.get('https://fourtonfish.com/hellosalut/?lang=' + lan, function (data) {
    $('#hello').text(data.hello);
  });
}
