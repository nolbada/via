var C='eobeop-sent-v4';
var F=['./','./index.html','./manifest.webmanifest','./icon-192.png','./icon-512.png','./d/ch01.js','./d/ch02.js','./d/ch03.js','./d/ch04.js','./d/ch05.js','./d/ch06.js','./d/ch07.js','./d/ch08.js','./d/ch09.js','./d/ch10.js','./d/ch11.js','./d/ch12.js','./d/ch13.js','./d/ch14.js'];
self.addEventListener('install',function(e){e.waitUntil(caches.open(C).then(function(c){return c.addAll(F)}));self.skipWaiting()});
self.addEventListener('activate',function(e){e.waitUntil(caches.keys().then(function(k){return Promise.all(k.filter(function(x){return x!==C}).map(function(x){return caches.delete(x)}))}));self.clients.claim()});
self.addEventListener('fetch',function(e){e.respondWith(fetch(e.request).then(function(r){var cp=r.clone();caches.open(C).then(function(c){c.put(e.request,cp)});return r}).catch(function(){return caches.match(e.request)}))});
