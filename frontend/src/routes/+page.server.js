// src: https://stackoverflow.com/a/72839244
/** @type {import('./$types').PageServerLoad} */
export async function load({ fetch }) {
	// const res = await fetch('http://api:8000/api/quizzes');
	const res = await fetch('/api/quizzes');
	const data = await res.json();

	if (data.length == 0) {
		return {
			quizzes: [
				{
					id: '1',
					name: 'Ayyy Lmao',
					creator: 'Anonymoose',
					created_at: '2024-09-11T23:24:33.979000',
					tags: ['moon', 'aliens'],
					questions: [
						{
							question: 'There are aliens on the moon',
							answer: true
						},
						{
							question: 'Planet mars is red?',
							answer: true
						}
					]
				}
			]
		};
	}

	return {
		quizzes: data
	};
}
