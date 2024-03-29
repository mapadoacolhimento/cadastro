/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
  purge: false,
  daisyui: {
    themes: [
      {
        mapa: {
          "primary": "#622565",
          "secondary": "#E8B638",
          "accent": "#1FB2A5",
          "neutral": "#424242",
          "base-100": "#fff",
          "info": "#3ABFF8",
          "success": "#36D399",
          "warning": "#FBBD23",
          "error": "#F87272",
        }
      },
    ],
  },

  content: [
    /**
     * HTML. Paths to Django template files that will contain Tailwind CSS classes.
     */

    /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
    // 'templates/**/*.html',

    /*
     * Main templates directory of the project (BASE_DIR/templates).
     * Adjust the following line to match your project structure.
     */
    // '../../templates/**/*.html',

    /*
     * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
     * Adjust the following line to match your project structure.
     */
    '/templates/*.html',
    '/templates/**/*.html',
    '../**/templates/**/*.html',

    /**
     * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
     * patterns match your project structure.
     */
    /* JS 1: Ignore any JavaScript in node_modules folder. */
    // '!../../**/node_modules',
    /* JS 2: Process all JavaScript files in the project. */
    '../**/static/**/*.js',

    /**
     * Python: If you use Tailwind CSS classes in Python, uncomment the following line
     * and make sure the pattern below matches your project structure.
     */
    // '../../**/*.py'
  ],
  theme: {
    colors: {
      lightPink: '#FFF3EF',
      gray: "#424242",
      lightGray: "#EEEEEE",
      darkGray: "#46444D",
      graphiteGray: '#565656',
      purple: "#EBE5EF",
      lightYellow: "#D9A92F",
      yellow: "#F5E6C2",
      white: "#ffffff",
      red: "#EB5757",
      lightRed: "#f87272",
      mediumPink: "#F0D9D2",
      zinc: "#46444C",
      softPurple: "#EBE5EF"
    },
    extend: {
      screens: {
        'xs': { 'min': '360px', 'max': '639px' }
      },
      width: {
        large: '1024px',
      },
      fontFamily: {
        sans: ['Nunito Sans', 'sans-serif'],
        idealista: ['Idealista Bold'],
        droid: ['Droid Sans']
      },
      colors: {
        'lightPurple': "#FCF8FF", 'lightRed': "#F6E3DD"
      }
    },
  },
  plugins: [
    /**
     * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
     * for forms. If you don't like it or have own styling for forms,
     * comment the line below to disable '@tailwindcss/forms'.
     */
    // require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
    require('@tailwindcss/line-clamp'),
    require('@tailwindcss/aspect-ratio'),
    require("daisyui"),
  ],
}
