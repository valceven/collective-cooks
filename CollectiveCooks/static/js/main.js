    // Dark Mode Toggle Logic
    const toggle = document.getElementById('theme-toggle');
    const html = document.querySelector('html');
    const sunIcon = document.getElementById('sun-icon');
    const moonIcon = document.getElementById('moon-icon');

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
