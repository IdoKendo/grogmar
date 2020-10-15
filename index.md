<p dir="rtl" id="koteret_sgg">מתי משחקים??</p>
<p dir="rtl" id="sfira_leahor"></p>

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
  document.getElementById("sfira_leahor").innerHTML = "עוד " + days + " ימים, " + hours + " שעות, "
  + minutes + " דקות ו" + seconds + " שניות, אבל מי סופר? ";

  // If the count down is finished, write some text
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("sfira_leahor").innerHTML = "אללה משחקים";
  }
}, 1000);
</script>