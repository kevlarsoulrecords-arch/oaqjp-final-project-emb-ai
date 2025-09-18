// Always show the server's reply (200 or 400) in the result box.
function runSentimentAnalysis() {
  const text = document.getElementById("textToAnalyze").value;
  const out = document.getElementById("result");

  const xhr = new XMLHttpRequest();
  xhr.open("GET", "/emotionDetector?textToAnalyze=" + encodeURIComponent(text), true);

  xhr.onload = function () {
    // Show whatever the server sent (JSON on success, plain text on error)
    out.textContent = xhr.responseText || "Invalid text! Please try again!";
  };

  xhr.onerror = function () {
    out.textContent = "Network error. Please try again.";
  };

  xhr.send();
}
