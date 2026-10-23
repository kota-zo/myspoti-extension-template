// "Heard Lately": a tiny real extension, the starting point of your own.
// It remembers the last songs that started and shows them as a section at the end of Home.
// No network. Documentation: https://github.com/kota-zo/myspoti/blob/main/docs/extensions/API.md

var KEEP = 10;

function recent() {
  return myspoti.storage.get('recent') || [];
}

// Called for each new song (needs the "playback.events" action).
myspoti.on('track', function (track) {
  if (!track.uri || track.uri.indexOf('spotify:track:') !== 0) return;   // local files have no Spotify page
  var list = recent().filter(function (t) { return t.uri !== track.uri; });
  list.unshift({ uri: track.uri, title: track.title, subtitle: track.artist });
  myspoti.storage.set('recent', list.slice(0, KEEP));
  myspoti.ui.refresh('home');                                            // ask the app to draw Home again
});

// Called when Home is drawn (needs "home.sections"). Answers blocks, never HTML: the app draws them.
myspoti.provide('home', function () {
  var list = recent();
  if (list.length === 0) {
    return [{ type: 'section', title: 'Heard lately', blocks: [
      { type: 'text', text: 'Play a song and it shows up here.', style: 'caption' }
    ] }];
  }
  return [{ type: 'section', title: 'Heard lately', blocks: [
    { type: 'tracks', items: list },
    { type: 'button', label: 'Clear', icon: 'refresh', action: 'clear' }
  ] }];
});

// A tap on a block with an "action" (the button above).
myspoti.provide('tap', function (e) {
  if (e.action === 'clear') {
    myspoti.storage.set('recent', []);
    myspoti.ui.refresh('home');
  }
});
