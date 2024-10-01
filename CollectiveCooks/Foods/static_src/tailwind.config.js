module.exports = {
    content: [
        // Django template paths where Tailwind CSS will be applied
        '../templates/**/*.html',
        '../../templates/**/*.html',
        '../../**/templates/**/*.html',
    ],
    theme: {
        backgroundColor: theme => ({
         ...theme('colors'),
         'light-mode': '#FFFFFF',
         'dark-mode' : '#121212',
         'accent1': '#f53803',
         'accent2': '#f5D020',
        })
    },
    darkMode: "class",  // Automatically applies dark mode based on user's system preferences
    plugins: [
        require('@tailwindcss/forms'),        // Tailwind Forms plugin
        require('@tailwindcss/typography'),   // Tailwind Typography plugin
        require('@tailwindcss/aspect-ratio'), // Tailwind Aspect Ratio plugin
    ],
};
