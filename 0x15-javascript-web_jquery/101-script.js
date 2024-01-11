const $ = window.$;
window.onload = function () {
  $('#add_item').click(function () {
    $('ul.my_list').append($('<li>').text('Item'));
  });

  $('#remove_item').click(function () {
    $('ul.my_list li:last-child').remove();
  });

  $('#clear_list').click(function () {
    $('ul.my_list li').remove();
  });
};
