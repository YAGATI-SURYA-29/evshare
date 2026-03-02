// Enhancements: spinner, clock, PDF export hook, small helpers
function showSpinner(el){el.classList.add('spinner-border');}
function hideSpinner(el){el.classList.remove('spinner-border');}
function startClock(id){setInterval(()=>{document.getElementById(id).textContent=new Date().toLocaleTimeString()},1000)}
function generatePdf(){
    // simple client-side PDF generation using jsPDF
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();
    doc.text('EVShare Booking', 10, 10);
    const form = document.getElementById('scheduler-form');
    const entries = new FormData(form);
    let y = 20;
    for (let [k,v] of entries) {
        doc.text(`${k}: ${v}`, 10, y);
        y += 10;
    }
    doc.save('booking.pdf');
}

function runFrontPageAnimations(){
    const hero = document.querySelector('.hero');
    if(hero) hero.classList.add('hero');
    const features = document.querySelectorAll('.feature');
    features.forEach(f=>{f.style.opacity='1';});
    const btn = document.querySelector('.btn-animate');
    if(btn) btn.classList.add('btn-animate');
}

document.addEventListener('DOMContentLoaded', runFrontPageAnimations);
function calculateCO2(){const miles=Number(document.getElementById('miles').value||0);const result=(miles*0.404).toFixed(2);document.getElementById('co2-result').textContent=`Estimated CO2 saved: ${result} kg/week`;}
