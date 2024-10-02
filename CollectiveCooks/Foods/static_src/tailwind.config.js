module.exports = {
    content: [
        // Django template paths where Tailwind CSS will be applied
        '../templates/**/*.html',
        '../../templates/**/*.html',
        '../../**/templates/**/*.html',
    ],
    theme: {
        extend: {  // Use 'extend' to add custom colors
            colors: {
                'light-mode': '#FFFFFF',
                'dark-mode': '#121212',
                'accent1': '#f53803',  // Custom accent1 color for text and background
                'accent2': '#f5D020',  // Custom accent2 color for text and background
            },
        },
    },
    darkMode: "class",  // Automatically applies dark mode based on user's system preferences
    plugins: [
        require('@tailwindcss/forms'),        // Tailwind Forms plugin
        require('@tailwindcss/typography'),   // Tailwind Typography plugin
        require('@tailwindcss/aspect-ratio'), // Tailwind Aspect Ratio plugin
    ],
};
