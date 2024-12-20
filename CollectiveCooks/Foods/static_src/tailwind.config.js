module.exports = {
    content: [
        // Django template paths where Tailwind CSS will be applied
        '../templates/**/*.html',
        '../../templates/**/*.html',
        '../../**/templates/**/*.html',
    ],
    theme: {
        extend: {  // Use 'extend' to add custom styles
            colors: {
                'light-mode': '#FFFFFF',
                'dark-mode': '#1a1a1a',
                'accent1': '#db461d',  // Custom accent1 color for text and background
                'accent2': '#f5D020',
                'confirm': '#15803d',
                'cancel': '#dc2626',
            },
            backgroundImage: theme => ({
                'gradient-accent': 'linear-gradient(to right, #faf118, #c21806)', // Custom gradient
            }),
        },
    },
    darkMode: "class",  // Automatically applies dark mode based on user's system preferences
    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),  
        require('@tailwindcss/aspect-ratio'),
        function ({addUtilities}) {
            const newUtilities = {
                ".no-scrollbar::-webkit-scrollbar" : {
                    display: "none",
                },
                ".no-scrollbar":{
                    'ms-overflow-style':'none',
                    'scrollbar-width':'none',
                }
            };

            addUtilities(newUtilities)
        }
    ],
    safelist: ['bg-cancel'], // Safelist the 'bg-cancel' class
};
