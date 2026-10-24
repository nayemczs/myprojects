const bgAeroplane = document.getElementById('id_bg_aeroplane')
const circleSilver = document.getElementById('circle_silver')
const circleBlack = document.getElementById('circle_black')
const idImg = document.getElementById('id_for_img')
const coverImgSrc = idImg.getAttribute('src')

window.onscroll = function() {myFunction()};

function myFunction() {
  if (document.body.scrollTop > 600 || document.documentElement.scrollTop > 800) {
    bgAeroplane.style.backgroundImage= `url(${coverImgSrc})`
    circleSilver.style.color= 'black'
    circleBlack.style.color = 'silver'
  } else {
    bgAeroplane.style.backgroundImage= 'none'
  }
}