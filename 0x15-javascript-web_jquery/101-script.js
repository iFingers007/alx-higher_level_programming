$(document).ready(function () {
  const list = $('.my_list');
  $('#add_item').click(function () {
    list.append('<li>Item</li>');
  });
  $('#remove_item').click(function () {
    list.children().last().remove();
  });
  $('#clear_list').click(function () {
    list.empty();
  });
});
