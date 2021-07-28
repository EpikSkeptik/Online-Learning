const pollBtn = document.querySelector('.btn')
let tog = false;


pollBtn.addEventListener('mouseover', function() {
    tog = true;
});

pollBtn.addEventListener('mouseout', function() {
    tog = false;
});

function polling () {
    if (tog) {
        pollBtn.classList.add('active');
    } else {
        pollBtn.classList.remove('active');
    }
    setTimeout(polling, 1000);
}

polling()