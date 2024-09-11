/** @type {import('@sveltejs/kit').HandleFetch} */
export async function handleFetch({ request, fetch }) {
	// if (request.url.startsWith('https://api.yourapp.com/')) {
	// 	// clone the original request, but change the URL
	// 	request = new Request(
	// 		request.url.replace('https://api.yourapp.com/', 'http://localhost:9999/'),
	// 		request
	// 	);
	// }

	return fetch(request);
}