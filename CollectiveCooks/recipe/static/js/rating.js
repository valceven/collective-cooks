let currentRating = 0;

  function setRating(rating) {
    currentRating = rating;
    // Update the hidden input value
    document.getElementById('rating-input').value = rating;
    
    // Update the star icons
    const stars = document.querySelectorAll('.rating-star');
    stars.forEach(star => {
      const index = parseInt(star.getAttribute('data-index'));
      if (index <= rating) {
        star.classList.add('text-yellow-400');
        star.classList.remove('text-gray-400');
      } else {
        star.classList.add('text-gray-400');
        star.classList.remove('text-yellow-400');
      }
    });
  }