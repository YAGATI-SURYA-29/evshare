// Enhancements: spinner, clock, PDF export hook, small helpers
function showSpinner(el){el.classList.add('spinner-border');}
function hideSpinner(el){el.classList.remove('spinner-border');}
function startClock(id){setInterval(()=>{document.getElementById(id).textContent=new Date().toLocaleTimeString()},1000)}
function generatePdf(){alert('PDF export placeholder — integrate jsPDF on server or client');}
function calculateCO2(){const miles=Number(document.getElementById('miles').value||0);const result=(miles*0.404).toFixed(2);document.getElementById('co2-result').textContent=`Estimated CO2 saved: ${result} kg/week`;}
