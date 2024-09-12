<form method="POST" class="w-10/12 lg:w-7/12 xl:w-6/12 h-full flex flex-col justify-start items-center gap-y-4 mx-auto">
	<main class="w-full mt-8 px-6 py-4 flex flex-col justify-center items-start gap-y-4 border-4 border-qdarkblue rounded bg-qlightblue">
		<section class="w-full">
			<label for="name" class="text-white text-xl font-primary font-[500]">Title:</label>
			<input type="text" name="name" id="name" class="block w-full border-2 border-qdarkblue rounded" />
		</section>
		<section class="w-full">
			<label for="tags" class="text-white text-xl font-primary font-[500]">Tags:</label>
			<input type="text" name="tags" id="tags" class="block w-full border-2 border-qdarkblue rounded" />
		</section>
		<hr class="w-full h-[1px]" />
		<section class="w-full">
			<section class="w-full">
				<label for="name" class="text-white text-xl font-primary">Question:</label>
				<input type="text" name="name" id="name" class="block w-full border-2 border-qdarkblue rounded" />
			</section>
			<section class="mt-2">
				<p class="text-white text-xl font-primary">Answer:</p>
				<button type="button" class="w-16 px-2 py-1 mr-2 border-qdarkblue border-2 bg-white rounded text-center align-center text-qdarkblue font-primary font-[600] text-xs md:text-base hover:bg-qyellow-light">True</button>
				<button type="button" class="w-16 px-2 py-1 mr-2 border-qdarkblue border-2 bg-white rounded text-center align-center text-qdarkblue font-primary font-[600] text-xs md:text-base hover:bg-qyellow-light">False</button>
			</section>
		</section>
	</main>
	<button type="submit" class="block w-full p-2 bg-qlightblue border-4 border-qdarkblue rounded text-white text-xl font-primary font-[500] text-center align-center uppercase">Add Question</button>
	<button type="submit" class="block w-full p-2 bg-qlightblue border-4 border-qdarkblue rounded text-white text-xl font-primary font-[500] text-center align-center uppercase">Create Quiz</button>
</form>
