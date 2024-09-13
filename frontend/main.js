import express from 'express'
import proxy from 'express-http-proxy';
import { handler } from './build/handler.js'

const app = express()

app.use('/api', proxy(`http://localhost:8000`, {
    proxyReqPathResolver: (req) => "/api" + req.url
}));

// let SvelteKit handle everything else, including serving prerendered pages and static assets
app.use(handler);

app.listen(3000, () => {
	console.log('listening on port 3000');
});