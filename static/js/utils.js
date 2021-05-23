const isUserLoggedIn = () => {
  // Formatting cookie from a string to an object
  // "logged-in=true" --> {logged-in: "true"}
  const parsedCookies = Object.fromEntries(
    document.cookie.split("; ").map((x) => x.split("="))
  );

  return parsedCookies["logged-in"] === "true";
};
