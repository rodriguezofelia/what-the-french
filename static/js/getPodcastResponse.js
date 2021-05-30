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
  const podcastHtmlItems = response.playlists.items.map((item) => {
    if (item.images[0] == undefined) {
      return "";
    }
    return `<div class="d-flex px-5 py-3">
    <div>
      <div><img class='spotify-img' src=${item.images[0].url}></div>
    </div>
    <div class="d-flex flex-column justify-content-center px-4">
      <div>Name: ${item.name}</div>
      ${item.description ? `<div>Description: ${item.description}</div>` : ""}
      <div>Interested in listening? <a href='${
        item.external_urls.spotify
      }'>Go to podcast playlist.</a></div>
    </div>
    </div>`;
  });
  podcastListContainer.innerHTML = podcastHtmlItems.join("");
};

const getPodcasts = async () => {
  const response = await requestSpotifyPlaylists();
  showResponse(response);
};

getPodcasts();
