(function () {
  function group(row) { var g = row.nextElementSibling; return g && g.classList.contains('oGuwee') ? g : null; }
  function set(row, open) {
    var g = group(row); if (!g) return;
    g.style.display = open ? 'block' : 'none';
    var a = row.querySelector('a'); if (a) a.setAttribute('aria-expanded', open);
  }
  function toggle(row) { var g = group(row); if (g) set(row, g.style.display === 'none'); }
  document.querySelectorAll('nav .PsKE7e').forEach(function (row) {
    var t = row.querySelector('.j10yRb'), a = row.querySelector('a');
    if (t) t.addEventListener('click', function (e) { e.preventDefault(); e.stopPropagation(); toggle(row); });
    if (a && !a.getAttribute('href')) a.addEventListener('click', function (e) { e.preventDefault(); toggle(row); });
  });
  // expand ancestors of the current page
  document.querySelectorAll('nav a[href]').forEach(function (a) {
    if (a.href.split('#')[0] !== location.href.split('#')[0] || !a.closest('li[data-nav-level]')) return;
    var row = a.closest('.PsKE7e'); if (row) set(row, true);
    for (var g = a.closest('.oGuwee'); g; g = g.parentElement && g.parentElement.closest('.oGuwee')) {
      g.style.display = 'block';
      var r = g.previousElementSibling; if (r) { var pa = r.querySelector('a'); if (pa) pa.setAttribute('aria-expanded', true); }
    }
  });
})();
(function () {
  var btn = document.getElementById('s9iPrd'), nav = document.getElementById('yuynLe');
  if (!btn || !nav) return;
  var st = document.createElement('style');
  st.textContent = '#s9iPrd{display:block !important;position:fixed;top:72px;right:16px;z-index:1000;width:48px !important;height:48px !important;box-sizing:border-box;background:#fff;color:#000;border:1px solid #888;border-radius:6px;cursor:pointer}' +
    '#yuynLe svg{width:24px;height:24px}#s9iPrd svg{width:24px;height:24px;stroke:#000}#yuynLe{display:block !important;position:fixed;top:0;bottom:0;left:-100%;z-index:999;overflow-y:auto;box-shadow:2px 0 8px rgba(0,0,0,.3)}#yuynLe.jsnVQ{left:0}' +
    '#yuynLe .IKA38e{left:0;opacity:1}';
  document.head.appendChild(st);
  function setOpen(o) { nav.classList.toggle('jsnVQ', o); btn.setAttribute('aria-expanded', o); }
  btn.addEventListener('click', function () { setOpen(!nav.classList.contains('jsnVQ')); });
  document.addEventListener('click', function (e) {
    if (nav.classList.contains('jsnVQ') && !nav.contains(e.target) && !btn.contains(e.target)) setOpen(false);
  });
})();
