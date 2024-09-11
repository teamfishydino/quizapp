import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
	server: {
		// see: https://patrickdesjardins.com/blog/docker-vitejs-hot-reload
		host: true,
		// hmr: { host: 8001},
		port: 8001,
		proxy: {
			"/api": {
				target: "http://api:8000",
				changeOrigin: true,
				secure: false
			}
		}
	},
    // see https://vitejs.dev/config/server-options#server-watch
    watch: {usePolling: true},
});