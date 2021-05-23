const accountLink = document.getElementById("account-link");
const logInOut = document.getElementById("log-in-out-link");
const quizNavLink = document.getElementById("quiz-nav-link");
console.log(isUserLoggedIn(), "heee");
if (isUserLoggedIn()) {
  accountLink.style.display = "list-item";
  quizNavLink.style.display = "list-item";
  logInOut.innerText = "Sign Out";
  logInOut.setAttribute("href", "/sign-out");
} else {
  accountLink.style.display = "none";
  quizNavLink.style.display = "none";
}
