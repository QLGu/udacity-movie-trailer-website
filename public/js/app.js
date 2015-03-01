var elMovies = document.getElementById('movies')

/**
 * Add modal event listener
 */
elMovies.addEventListener('click', function (event) {
  event = event || window.event
  var target = event.target || event.srcElement

  while (!target.classList.contains('movie-tile'))
  target = target.parentNode

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

  var elWrapModal = document.createElement('div')
  elWrapModal.addEventListener('click', removeModal)
  elWrapModal.id = 'modal'
  elWrapModal.className = 'wrap__modal'

  var elModal = document.createElement('div')
  elModal.className = 'modal'

  var elInnerModal = document.createElement('div')
  elInnerModal.className = 'inner__modal'

  var elWrapIframe = document.createElement('div')
  elWrapIframe.className = 'wrap__iframe'

  var elIframe = document.createElement('iframe')
  elIframe.src = sourceUrl

  var elModelClose = document.createElement('div')
  elModelClose.id = 'modal__close'
  elModelClose.className = 'modal__close'
  elModelClose.innerHTML = '&times;'

  elWrapIframe.appendChild(elIframe)
  elWrapIframe.appendChild(elModelClose)

  elInnerModal.appendChild(elWrapIframe)
  elModal.appendChild(elInnerModal)
  elWrapModal.appendChild(elModal)

  return elWrapModal
}
