    // Dark Mode Toggle Logic
    const toggle = document.getElementById('theme-toggle');
    const html = document.querySelector('html');
    const sunIcon = document.getElementById('sun-icon');
    const moonIcon = document.getElementById('moon-icon');
    const searchInput = document.getElementById('search-input');
    const searchResults = document.getElementById('search-results');
    const searchButton = document.getElementById('search-button');

    // Check for saved user preference
    const userTheme = localStorage.getItem('theme');
        if (userTheme === 'dark') {
        html.classList.add('dark');
        sunIcon.classList.add('hidden');
        moonIcon.classList.remove('hidden');
    }

    toggle.addEventListener('click', () => {
    html.classList.toggle('dark');

    // Toggle icons
    sunIcon.classList.toggle('hidden');
    moonIcon.classList.toggle('hidden');

    // Save user preference
    const theme = html.classList.contains('dark') ? 'dark' : 'light';
        localStorage.setItem('theme', theme);
    });

    searchInput.addEventListener('input', (event) => {
        const query = event.target.value.trim();
        if (query !== '') {
            // Make a request to the backend search API
            fetch(`/search/?q=${query}`)
                .then(response => response.json())
                .then(data => {
                    // Update the search results display
                    searchResults.innerHTML = data.map(item => `
                        <li>
                            <a href="/profile/${item.name}">
                                <img src="${item.profile_picture || '/static/default-profile.png'}" alt="${item.name}'s profile picture" class="profile-pic">
                                ${item.name}
                            </a>
                        </li>
                    `).join('');
                })
                .catch(error => console.error('Error fetching search results:', error));
        } else {
            searchResults.innerHTML = '';  // Clear results if query is empty
        }
    });

    searchButton.addEventListener('click', () => {
        const query = searchInput.value.trim();
        if (query !== '') {
            // Make a request to the backend search API
            fetch(`/search/?q=${query}`)
                .then(response => response.json())
                .then(data => {
                    // Update the search results display
                    searchResults.innerHTML = data.map(item => `<li>${item.username}</li>`).join('');
                })
                .catch(error => console.error('Error fetching search results:', error));
        } else {
            searchResults.innerHTML = '';
        }
    });