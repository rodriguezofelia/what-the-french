const requestSpotifyPlaylists = async () => {
  const response = await fetch("/spotify-auth");
  return response.json();
};

const showResponse = (response) => {
  const podcastListContainer =
    document.querySelector("#podcastPlaylistList") || {};
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
      }' target="_blank">Go to podcast playlist.</a></div>
    </div>
    </div>`;
  });
  podcastListContainer.innerHTML = podcastHtmlItems.join("");
  return podcastHtmlItems.join("");
};

const getPodcasts = async () => {
  const response = await requestSpotifyPlaylists();
  showResponse(response);
};

getPodcasts();
