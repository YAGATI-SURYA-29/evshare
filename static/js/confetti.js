// Simple confetti wrapper using canvas-confetti
function fireConfetti(){
    if(typeof confetti === 'function'){
        confetti({particleCount:100, spread:70, origin:{y:0.6}});
    } else {
        console.log('confetti! (library not loaded)');
    }
}
