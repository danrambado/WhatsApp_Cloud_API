/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx}",
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
 
    // Or if using `src` directory:
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    // colors: {
    //   'iafpink': '#BA0170'
    // },
    extend: {
      colors: {
        'iafpink': '#BA0170'
      },
      keyframes: {
        'gradient-move': {
          '0%, 100%': {
            'background-size': '200% 200%',
            'background-position': 'center',
          },
          '50%': {
            'background-size': '200% 200%',
            'background-position': 'right',
          },
        },
      },
      animation: {
        'gradient-move': 'gradient-move 10s ease-in-out infinite',
      },
    },
  },
  plugins: [],
}