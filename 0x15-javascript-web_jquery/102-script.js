const $ = window.$;
window.onload = function () {
  $('#btn_translate').click(function () {
    const lan = $('#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/?lang=' + lan, function (data) {
      $('#hello').text(data.hello);
    });
  });
};
