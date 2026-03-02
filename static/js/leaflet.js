// Minimal Leaflet init for Avadi area
function initEvshareMap(containerId){
  if(typeof L === 'undefined'){
    console.warn('Leaflet not loaded from CDN — include leaflet CSS/JS');
    return;
  }
  const map=L.map(containerId).setView([13.1005,80.0996],13);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{maxZoom:19}).addTo(map);
  // sample station data
  const stations = [
    {name:'Avadi C1',coords:[13.1005,80.0996]},
    {name:'Avadi C2',coords:[13.102,80.095]},
    {name:'Avadi East',coords:[13.097,80.102]}
  ];
  stations.forEach(s=>{
    L.marker(s.coords).addTo(map).bindPopup(s.name);
  });
}
