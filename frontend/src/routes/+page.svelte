<script>
	import QuizFeedCard from '$lib/QuizFeedCard.svelte';
	export let data;
</script>

<main class="flex flex-col justify-center items-center m-2 md:m-8">
	{#each data.quizzes as quiz (quiz.id)}
		<QuizFeedCard {quiz} />
	{/each}
</main>
