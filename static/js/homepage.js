const quizLink = document.getElementById("quiz-link");

if (!isUserLoggedIn()) {
  quizLink.innerHTML =
    "<p>Looking to take a quiz? You'll need to <a href='/sign-in'>sign in!</a></p>";
}
