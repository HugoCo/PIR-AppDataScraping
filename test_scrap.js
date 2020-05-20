var gplay = require('google-play-scraper');

test = gplay.app({appId: 'com.google.android.apps.translate'})
  .then(console.log, console.log);
  test.replace(/&quot;/ig,'"');