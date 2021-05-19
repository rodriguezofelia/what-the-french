const requestSpotifyPlaylists = async () => {
  return await fetch(
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
        "https://api.spotify.com/v1/search?q=french%10podcasts&type=playlist",
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
      return response;
    });
};

const showResponse = (response) => {
  const podcastListContainer = document.querySelector("#podcastPlaylistList");
  console.log("are you wroking today ", response.playlists.items);

  const podcastHtmlItems = response.playlists.items.map((item) => {
    return `<div>
    <div>Name: ${item.name}</div>
    <div>Description: ${item.description}</div>
    <div>URL: ${item.external_urls.spotify}</div>
    <div>Image: ${item.images[0].url}</div>
    <div>Tracks: ${item.tracks.href}</div>
    </div>`;
  });
  podcastListContainer.innerHTML = podcastHtmlItems.join("");
};

const getPodcasts = async () => {
  const response = await requestSpotifyPlaylists();
  showResponse(response);
};

getPodcasts();
