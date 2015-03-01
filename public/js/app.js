var elMovies = document.getElementById('movies')

/**
 * Add modal event listener
 */
elMovies.addEventListener('click', function (event) {
  event = event || window.event
  var target = event.target || event.srcElement

  while (!target.classList.contains('movie-tile')) {
    target = target.parentNode
  }

  addModal(target.getAttribute('data-trailer-id'))
})

/******************************************************************************/

/**
 * Add modal
 */
function addModal (trailerID) {
  var model = createModal(trailerID)
  document.body.appendChild(model)
}


/**
 * Remove modal
 */
function removeModal () {
  document.body.removeChild(document.getElementById('modal'))
}

/******************************************************************************/

/**
 * Create modal wth trailer video
 */
function createModal (trailerID) {
  var sourceUrl = 'http://www.youtube.com/embed/' +
      trailerID + '?autoplay=1&html5=1'

  var elModal = document.createElement('div')
  elModal.addEventListener('click', removeModal)
  elModal.id = 'modal'
  elModal.className = 'wrap__modal'
  elModal.innerHTML = '' +
    '<div class="modal">' +
      '<div class="inner__modal">' +
        '<div class="modal__content">' +
          '<div class="modal__body">' +
            '<iframe src="' + sourceUrl + '" border="0"></iframe>' +
          '</div>' +
          '<div id="modal__close" class="modal__close">&times;</div>' +
        '</div>' +
      '</div>' +
    '</div>'

  return elModal
}
