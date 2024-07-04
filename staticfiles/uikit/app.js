// Invoke Functions Call on Document Loaded
document.addEventListener('DOMContentLoaded', function () {
  // Ensure hljs is defined before using it
  if (typeof hljs !== 'undefined') {
    hljs.highlightAll();
  } else {
    console.error('highlight.js is not loaded.');
  }
});

let alertWrapper = document.querySelector('.alert');
let alertClose = document.querySelector('.alert__close');

if (alertWrapper) {
  alertClose.addEventListener('click', () => {
    alertWrapper.style.display = 'none';
  });
}