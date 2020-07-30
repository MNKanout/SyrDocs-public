function getscroll () {
    let scrollPosition = window.pageYOffset;
    document.getElementById('scrollPosition').value = scrollPosition
  }

function scroll (y) {
    window.scrollTo(0,y);
}