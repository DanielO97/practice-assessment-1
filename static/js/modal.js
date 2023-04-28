function openModal () {
    document.querySelector('.modal').style.display = 'flex'
  }
  function closeModal() {
    document.querySelector('.modal').style.display = 'none'
  }
  document.getElementById('modal-trigger').addEventListener('click', function() {
    console.log('clicked')
    openModal()
  })
  document.getElementById('close-modal').addEventListener('click', function() {
    closeModal()
  })
  window.addEventListener('click', function(event) {
  if (event.target == document.querySelector('.modal')) {
    closeModal();
  }})
