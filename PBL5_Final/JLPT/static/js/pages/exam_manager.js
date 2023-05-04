$(document).ready(function() {
    var dropdownButton = $("#dropdownMenuButton2");
    var dropdownItems = $(".dropdown-item");
    dropdownItems.click(function() {
      var selectedText = $(this).text();
      dropdownButton.text(selectedText);
    });
  });
  