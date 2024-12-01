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
}

// Show the modal when the submit button is clicked
document.getElementById('submit-rating-btn').addEventListener('click', function() {
    if (currentRating > 0) {
        // Set the rating in the modal
        document.getElementById('selected-rating').textContent = currentRating;
        
        // Show the modal
        document.getElementById('ratingModal').classList.remove('hidden');
    } else {
        alert('Please select a rating before submitting.');
    }
});

// Handle the "Cancel" button in the modal
document.getElementById('cancel-modal-btn').addEventListener('click', function() {
    document.getElementById('ratingModal').classList.add('hidden');
});

// Handle the "Confirm" button in the modal
document.getElementById('confirm-modal-btn').addEventListener('click', function() {
    // Submit the form
    document.getElementById('rating-form').submit();
});
