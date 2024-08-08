$(document).ready(function () {
  // Define the URL to fetch translation data
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  // Use jQuery ajax to fetch data
  $.ajax({
    url,
    dataType: 'json',
    success: function (data) {
      const hello = data.hello; // Get the "hello" translation

      // Select the DIV element using jQuery
      const helloDiv = $('#hello');

      // Set the DIV content to the translated "hello"
      helloDiv.text(hello);
    },
    error: function (jqXHR, textStatus, errorThrown) {
      console.error('Error fetching translation:', textStatus, errorThrown);
      $('#hello').text('Error fetching translation'); // Display error message
    }
  });
});
