/** @type {import('tailwindcss').Config} */
export default {
	content: ['./src/**/*.{html,js,svelte,ts}'],
	theme: {
		extend: {
			fontFamily: {
				// font-weight: 300 - 700, 400: normal
				primary: ['Hind', 'sans-serif'],
				// font-weight: 100 - 900
				secondary: ['Montserrat', 'system-ui']
			},
			colors: {
				qred: '#D00000',
				qyellow: '#FFBA08',
				'qyellow-light': '#FFF1CD',
				qlightblue: '#3F88C5',
				qdarkblue: '#032B43',
				qgreen: '#136F63'
			}
		}
	},
	plugins: []
};
