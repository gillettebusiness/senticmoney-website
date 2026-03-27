(function() {
  'use strict';

  // Self-exclude: visit any page with ?notrack=1 to permanently stop tracking this browser.
  // To re-enable: open DevTools > Application > Local Storage > delete _snt_notrack
  if (new URLSearchParams(location.search).get('notrack') === '1') {
    localStorage.setItem('_snt_notrack', '1');
  }
  if (localStorage.getItem('_snt_notrack') === '1') return;

  var ENDPOINT = 'https://sentic-proxy-server.onrender.com/track';

  // Visitor ID (persistent via localStorage)
  var vid = localStorage.getItem('_snt_vid');
  if (!vid) {
    vid = crypto.randomUUID ? crypto.randomUUID() : 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
      var r = Math.random() * 16 | 0;
      return (c === 'x' ? r : (r & 0x3 | 0x8)).toString(16);
    });
    localStorage.setItem('_snt_vid', vid);
  }

  // UTM params — read from URL, persist in sessionStorage for cross-page nav
  var params = new URLSearchParams(location.search);
  var utmKeys = ['utm_source', 'utm_medium', 'utm_campaign'];
  utmKeys.forEach(function(k) {
    var v = params.get(k);
    if (v) sessionStorage.setItem(k, v);
  });

  var payload = {
    path: location.pathname,
    referrer: document.referrer || '',
    visitor_id: vid,
    utm_source: sessionStorage.getItem('utm_source') || '',
    utm_medium: sessionStorage.getItem('utm_medium') || '',
    utm_campaign: sessionStorage.getItem('utm_campaign') || '',
    screen_width: screen.width,
    ua: navigator.userAgent
  };

  var data = JSON.stringify(payload);
  if (navigator.sendBeacon) {
    navigator.sendBeacon(ENDPOINT, data);
  } else {
    fetch(ENDPOINT, { method: 'POST', body: data, keepalive: true }).catch(function() {});
  }
})();
