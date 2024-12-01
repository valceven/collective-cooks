// JavaScript function to toggle the submit button's enabled/disabled state and style
function toggleSubmitButton() {
    const commentTextarea = document.getElementById('comment-textarea');
    const submitButton = document.getElementById('submit-comment-btn');

    // Enable the button if the textarea has content, otherwise disable it
    if (commentTextarea.value.trim() !== '') {
        submitButton.disabled = false;
        submitButton.classList.remove('bg-gray-400', 'cursor-not-allowed');
        submitButton.classList.add('bg-accent1', 'cursor-pointer');
    } else {
        submitButton.disabled = true;
        submitButton.classList.remove('bg-accent1', 'cursor-pointer');
        submitButton.classList.add('bg-gray-400', 'cursor-not-allowed');
    }
}
