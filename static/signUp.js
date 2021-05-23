const signUp = async () => {
  const firstName = document.getElementById("first-name").value;
  const lastName = document.getElementById("last-name").value;
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  // Request to server endpoint to create user
  const response = await fetch("/users", {
    method: "POST",
    body: JSON.stringify({
      first_name: firstName,
      last_name: lastName,
      email,
      password,
    }),
  });
  const parsedResponse = await response.json();
  if (parsedResponse.error) {
    const emailErrorEl = document.getElementById("email-error-msg");
    emailErrorEl.innerText = parsedResponse.error;
  }
};

const form = document.querySelector("form");
form.addEventListener("submit", (event) => {
  event.preventDefault();
  signUp();
});
