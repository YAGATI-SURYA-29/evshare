// Minimal Leaflet init for Avadi area
function initEvshareMap(containerId){
  if(typeof L === 'undefined'){
    console.warn('Leaflet not loaded from CDN — include leaflet CSS/JS');
    return;
  }
  const map=L.map(containerId).setView([13.1005,80.0996],13);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{maxZoom:19}).addTo(map);
  // example marker
  L.marker([13.1005,80.0996]).addTo(map).bindPopup('Avadi Station');
}
