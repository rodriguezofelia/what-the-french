const logInOut = document.getElementById("log-in-out-link");

// Formatting cookie from a string to an object
// "logged-in=true" --> {logged-in: "true"}
const parsedCookies = Object.fromEntries(
  document.cookie.split("; ").map((x) => x.split("="))
);

if (parsedCookies["logged-in"] === "true") {
  logInOut.innerText = "Sign Out";
  logInOut.setAttribute("href", "/sign-out");
}
