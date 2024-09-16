const newsletterUrl = "/newsletter/";
$(document).ready(() => {
  setTimeout(() => {
    $("#alert-message").hide();
  }, 7000);
  $("#alert-message-close-btn").click(() => {
    $("#alert-message").hide();
  });
  $("#newsletter-form").submit((event) => {
    event.preventDefault();
    console.log(event);
    csrfToken = event.target.querySelector(
      '[name="csrfmiddlewaretoken"]'
    ).value;
    email = event.target.querySelector('[name="subscribe"]').value;
    postRequest(newsletterUrl, {
      email: email,
      csrfmiddlewaretoken: csrfToken,
    });
  });
});
const datePickerId = document.getElementById("datePickerId");
if (datePickerId) {
  datePickerId.max = new Date().toISOString().split("T")[0];
}

/*Ajax Requests */
function postRequest(url, data) {
  ajaxCall("POST", url, data);
}

function ajaxCall(method, url, data) {
  $.ajax({
    url: url,
    type: method,
    data: data,
    headers: {
      "X-CSRFToken": data.csrfmiddlewaretoken,
    },
    success: function (content, status, xhr) {
      if (xhr.status == 200) {
        alert(content.message);
      }
    },
    error: function (xhr, error, status) {
      console.error(`An Error Occured with Status ${status} ${xhr.status}`);
    },
  });
}
