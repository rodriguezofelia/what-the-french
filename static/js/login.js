const login = async () => {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  // Request to server endpoint to login user
  const response = await fetch("/login", {
    method: "POST",
    body: JSON.stringify({
      email,
      password,
    }),
  });
  const parsedResponse = await response.json();

  if (parsedResponse.error) {
    const emailErrorEl = document.getElementById("incorrect-pw-msg");
    emailErrorEl.innerText = parsedResponse.error;
  } else {
    window.location.href = "/profile";
  }
};

const form = document.querySelector("form");
form.addEventListener("submit", (event) => {
  event.preventDefault();
  login();
});
