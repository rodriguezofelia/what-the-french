const getPodcasts = async () => {
  fetch(
    "https://accounts.spotify.com/api/token?grant_type=client_credentials",
    {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
        Authorization: `Basic ${btoa(
          secrets.spotify_client_id + ":" + secrets.spotify_client_secret
        )}`,
      },
    }
  )
    .then((response) => response.json())
    .then((response) => {
      console.log(response);
      return fetch(
        "https://api.spotify.com/v1/search?q=french%20podcasts&type=playlist",
        {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${response.access_token}`,
          },
        }
      );
    })
    .then((response) => response.json())
    .then((response) => {
      console.log(response);
    });
};

getPodcasts();
