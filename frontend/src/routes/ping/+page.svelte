<script>
	async function getPing() {
		const res = await fetch('/api/ping');
		const data = await res.json();

		if (!data.message) {
			return 'Error, no pong!';
		}
		
		return data.message;
	}
</script>

<a href="/">Home</a>

{#await getPing() then message}
	<h1 class="text-3xl font-bold">{message}!</h1>
{:catch}
	<p>Error: API is not running or not reachable</p>
{/await}
