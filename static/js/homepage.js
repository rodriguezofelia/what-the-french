const quizLink = document.getElementById("quiz-link");

if (!isUserLoggedIn()) {
  quizLink.innerHTML =
    "<p class='m-0'>Looking to take a quiz? You'll need to <a class='text-decoration-none' href='/sign-in'>sign in!</a></p>";
}
