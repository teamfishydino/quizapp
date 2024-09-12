<script>
	export let quiz;
	let date = new Date(quiz.created_at).toDateString();
</script>

<section class="flex flex-col w-11/12 lg:w-3/4 xl:w-1/2 m-2 md:m-4 p-4 md:p-6 border-4 border-qdarkblue rounded justify-center items-start bg-qlightblue">
	<h1 class="text-2xl md:text-3xl text-white font-secondary font-[600] border-b-2 mb-2">{quiz.name}</h1>
	<h2 class="text-base md:text-xl text-qdarkblue font-primary font-[500]">By {quiz.creator}</h2>
	<p class="text-sm md:text-lg text-white font-primary font-[300]">{quiz.questions.length} Questions | {date}</p>
	<div class="flex justify-start items-center">
		{#each quiz.tags as tag (tag)}
			<p class="px-2 py-0.5 md:px-3 md:py-1 mt-2 mr-2 border-qdarkblue border-2 bg-white rounded text-center text-qdarkblue font-primary font-[500] text-xs md:text-base">{tag}</p>
		{/each}
	</div>
</section>
