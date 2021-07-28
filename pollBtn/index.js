const pollBtn = document.querySelector('.btn')
const intervalBtn = document.querySelector('.interval-btn');

let tog = false;
let intervalOn = true;

pollBtn.addEventListener('mousedown', function() {
    tog = true;
});

pollBtn.addEventListener('mouseup', function() {
    tog = false;
});

intervalBtn.addEventListener('click', function() {
    intervalOn = !intervalOn;
    intervalBtn.classList.toggle('active');
    
    pollBtn.classList.toggle('disabled');
    polling();

});


function polling () {
    if(intervalOn) {
        if (tog) {
            pollBtn.classList.add('active');
        } else {
            pollBtn.classList.remove('active');
        }
        setInterval(polling, 1000);
    } else {
        pollBtn.classList.toggle('disabled');
    }
}
     
   

polling();