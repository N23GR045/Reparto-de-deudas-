// Service worker: permite abrir la app sin conexión y recibir actualizaciones.
// GitHub Actions cambia __APP_BUILD__ por el número de versión al publicar,
// así cada versión nueva usa una caché nueva y el navegador detecta el cambio.
const CACHE = "reparto-de-deudas-__APP_BUILD__";
const SHELL = ["./", "index.html", "manifest.webmanifest", "icons/icon-192.png", "icons/icon-512.png", "icons/apple-touch-icon.png", "icons/favicon.png"];

self.addEventListener("install", (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(SHELL.map((u) => new Request(u, { cache: "reload" })))).then(() => self.skipWaiting()));
});

self.addEventListener("activate", (e) => {
  e.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener("message", (e) => {
  if (e.data && e.data.type === "SKIP_WAITING") self.skipWaiting();
});

self.addEventListener("fetch", (e) => {
  const req = e.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  // Tipografías de Google: se guardan la primera vez que se descargan.
  if (url.hostname.endsWith("fonts.googleapis.com") || url.hostname.endsWith("fonts.gstatic.com")) {
    e.respondWith(
      caches.open(CACHE).then((c) => c.match(req).then((hit) => hit || fetch(req).then((res) => { c.put(req, res.clone()); return res; })))
    );
    return;
  }
  if (url.origin !== location.origin) return;
  // Archivos de la app: primero la red (así llegan las actualizaciones); sin conexión, la copia guardada.
  e.respondWith(
    fetch(req, { cache: "no-cache" })
      .then((res) => { if (res.ok) { const copy = res.clone(); caches.open(CACHE).then((c) => c.put(req, copy)); } return res; })
      .catch(() => caches.match(req).then((hit) => hit || caches.match("index.html")))
  );
});
