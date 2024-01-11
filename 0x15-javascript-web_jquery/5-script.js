const $ = window.$;
$('#add_item').click(function () {
  $('ul.my_list').append($('<li>').text('Item'));
});
