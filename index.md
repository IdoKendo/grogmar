<p dir="rtl" id="koteret_sgg">מתי משחקים??</p>
<p dir="rtl" id="sfira_leahor"></p>
<button onclick="copySfiraLeahor()" style="float: right;">אני רוצה להעתיק את זה כדי להדביק בטלגרם</button>


<script>
// Set the date we're counting down to
var countDownDate = new Date("Oct 17, 2020 20:00:00").getTime();

// Update the count down every 1 second
var x = setInterval(function() {

  // Get today's date and time
  var now = new Date().getTime();

  // Find the distance between now and the count down date
  var distance = countDownDate - now;

  // Time calculations for days, hours, minutes and seconds
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);

  // Display the result in the element with id="sfira_leahor"
  var sfira = "עוד " + days + " ימים, " + hours + " שעות, " + minutes + " דקות ו" + seconds + " שניות, אבל מי סופר? ";
  document.getElementById("sfira_leahor").innerHTML = sfira.replace(" 2 ימים", " יומיים").replace(" 2 שעות", " שעתיים").replace(" 1 ימים", " יום").replace(" 1 שעות", " שעה").replace(" 1 דקות", " דקה");

  // If the count down is finished, write some text
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("sfira_leahor").innerHTML = "אללה משחקים";
  }
}, 1000);

function copyTextToClipboard(text) {
  var textArea = document.createElement("textarea");

  //
  // *** This styling is an extra step which is likely not required. ***
  //
  // Why is it here? To ensure:
  // 1. the element is able to have focus and selection.
  // 2. if element was to flash render it has minimal visual impact.
  // 3. less flakyness with selection and copying which **might** occur if
  //    the textarea element is not visible.
  //
  // The likelihood is the element won't even render, not even a
  // flash, so some of these are just precautions. However in
  // Internet Explorer the element is visible whilst the popup
  // box asking the user for permission for the web page to
  // copy to the clipboard.
  //

  // Place in top-left corner of screen regardless of scroll position.
  textArea.style.position = 'fixed';
  textArea.style.top = 0;
  textArea.style.left = 0;

  // Ensure it has a small width and height. Setting to 1px / 1em
  // doesn't work as this gives a negative w/h on some browsers.
  textArea.style.width = '2em';
  textArea.style.height = '2em';

  // We don't need padding, reducing the size if it does flash render.
  textArea.style.padding = 0;

  // Clean up any borders.
  textArea.style.border = 'none';
  textArea.style.outline = 'none';
  textArea.style.boxShadow = 'none';

  // Avoid flash of white box if rendered for any reason.
  textArea.style.background = 'transparent';


  textArea.value = text;

  document.body.appendChild(textArea);
  textArea.focus();
  textArea.select();

  try {
    var successful = document.execCommand('copy');
    var msg = successful ? 'successful' : 'unsuccessful';
    console.log('Copying text command was ' + msg);
  } catch (err) {
    console.log('Oops, unable to copy');
  }

  document.body.removeChild(textArea);
}

function copySfiraLeahor() {
  /* Get the text field */
  var copyText = document.getElementById("sfira_leahor");

  copyTextToClipboard(copyText.innerHTML);
}
</script>