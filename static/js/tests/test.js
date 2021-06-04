(function () {
  "use strict";

  /**
   * test function
   * @param {string} desc
   * @param {function} fn
   */
  function it(desc, fn) {
    try {
      fn();
      console.log("\x1b[32m%s\x1b[0m", "\u2714 " + desc);
    } catch (error) {
      console.log("\n");
      console.log("\x1b[31m%s\x1b[0m", "\u2718 " + desc);
      console.error(error);
    }
  }
  function assert(isTrue) {
    if (!isTrue) {
      throw new Error();
    }
  }
  it("should return playlist items", async function () {
    const response = await requestSpotifyPlaylists();
    assert(response.playlists.items.length > 0);
  });

  it("should return html as expected", function () {
    const response = {
      playlists: {
        items: [
          {
            images: [{ url: "meow.jpg" }],
            name: "kitty",
            description: "its a kitty kat",
            external_urls: { spotify: "www.google.com" },
          },
        ],
      },
    };
    const returnedHtml = showResponse(response);
    const expectedHtml = `<div class="d-flex px-5 py-3">
    <div>
      <div><img class='spotify-img' src=meow.jpg></div>
    </div>
    <div class="d-flex flex-column justify-content-center px-4">
      <div>Name: kitty</div>
      <div>Description: its a kitty kat</div>
      <div>Interested in listening? <a href='www.google.com'>Go to podcast playlist.</a></div>
    </div>
    </div>`;
    assert(returnedHtml === expectedHtml);
  });

  it("should login user with correct login info", async function () {
    // given the value in the input element when the form is submitted
    // it should hit the /login endpoint with that value
  });
})();
