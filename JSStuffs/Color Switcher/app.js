const body = document.body
const color = document.querySelector('.color')
const switchBtn = document.querySelector('.switch') 

switchBtn.addEventListener('click', function () {
    let color1 = getRandNum();
    let color2 = getRandNum();
    let color3 = getRandNum();

    const colorString = `rgb(${color1}, ${color2}, ${color3})`;
    color.innerText = colorString;
    body.style.backgroundColor = colorString;
});

function getRandNum() {
    return Math.floor(Math.random()*256);
}