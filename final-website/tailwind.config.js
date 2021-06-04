module.exports = {
  purge: ['./src/**/*.{js,jsx,ts,tsx}', './public/index.html'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      fontFamily: {
        'futura': ['Futura', 'sans-serif']
      },
      colors: {
        'font-gray': '#444B54',
        'normal': '#A8A878',
        'fire': '#F08030',
        'water': '#6790F0',
        'grass': '#78C84F',
        'electric': '#F9CF30',
        'ice': '#98D8D8',
        'fighting': '#C03028',
        'poison': '#9F409F',
        'ground': '#E0C068',
        'ghost': '#705898',
        'flying': '#A890F0',
        'psychic': '#F85888',
        'bug': '#A8B720',
        'rock': '#B8A039',
        'dark': '#705848',
        'dragon': '#7038F8',
        'steel': '#B8B8D0',
        'fairy': '#F0B6BC',
        'btn-blue': '#386ABB'
      }
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
