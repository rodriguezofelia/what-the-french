fetch("https://accounts.spotify.com/api/token?grant_type=client_credentials", {
  method: "POST",
  headers: {
    "Content-Type": "application/x-www-form-urlencoded",
    Authorization: `Basic ${btoa(
      secrets.spotify_client_id + ":" + secrets.spotify_client_secret
    )}`,
  },
});
