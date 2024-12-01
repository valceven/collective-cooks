let currentRating = 0;

// Function to set the rating when a star is clicked
function setRating(rating) {
    currentRating = rating;
    document.getElementById('rating-input').value = rating;

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

    toggleSubmitRatingButton();
}

// Function to toggle the submit rating button state
function toggleSubmitRatingButton() {
    const ratingValue = document.getElementById('rating-input').value;
    const submitRatingBtn = document.getElementById('submit-rating-btn');

    // Enable the button if the rating is greater than 0
    if (ratingValue > 0) {
      submitRatingBtn.disabled = false;
      submitRatingBtn.classList.remove('bg-gray-400', 'cursor-not-allowed');
      submitRatingBtn.classList.add('bg-accent1', 'cursor-pointer');
    } else {
      submitRatingBtn.disabled = true;
      submitRatingBtn.classList.remove('bg-accent1', 'cursor-pointer');
      submitRatingBtn.classList.add('bg-gray-400', 'cursor-not-allowed');
    }
  }

// Show the modal when the submit button is clicked
document.getElementById('submit-rating-btn').addEventListener('click', function() {
    if (currentRating > 0) {
        // Set the rating in the modal
        document.getElementById('selected-rating').textContent = currentRating;
        
        // Show the modal with animation
        const modal = document.getElementById('ratingModal');
        modal.classList.remove('hidden');
        modal.querySelector('div').classList.remove('scale-0', 'opacity-0');
        modal.querySelector('div').classList.add('scale-100', 'opacity-100');
    } else {
        alert('Please select a rating before submitting.');
    }
});

// Handle the "Cancel" button in the modal
document.getElementById('cancel-modal-btn').addEventListener('click', function() {
    hideModal();
});

// Handle the "Confirm" button in the modal
document.getElementById('confirm-modal-btn').addEventListener('click', function() {
    // Submit the form
    document.getElementById('rating-form').submit();
});

// Function to hide the modal
function hideModal() {
    const modal = document.getElementById('ratingModal');
    modal.querySelector('div').classList.add('scale-0', 'opacity-0');
    
    // Wait for the transition to finish before hiding the modal
    setTimeout(() => {
        modal.classList.add('hidden');
    }, 300);  // Matches the transition duration
}