(function () {
  var H = '4029c902a2059f38af3f6f53884b76d227243d22b981caa8dcc21a9d65181e40';
  var base = document.currentScript.src.replace(/assets\/auth\.js.*$/, '');
  var ok = false;
  try { ok = sessionStorage.getItem('occi_auth') === H; } catch (e) {}
  if (ok) return;
  document.documentElement.style.display = 'none';
  var path = location.href.slice(base.length).split('#')[0];
  location.replace(base + 'login.html?next=' + encodeURIComponent(path));
})();
