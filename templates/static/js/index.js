$(document).ready(() => {
  setTimeout(() => {
    $("#alert-message").hide();
  }, 7000);
  $("#alert-message-close-btn").click(() => {
    $("#alert-message").hide();
  });
});
const datePickerId = document.getElementById("datePickerId");
datePickerId.max = new Date().toISOString().split("T")[0];
