<script>
    import { goto } from "$app/navigation"
    import "../app.css";
    import plus from "$lib/plus.svg"
</script>
  
<main class="w-full h-full flex flex-col justify-between">
  <header class="w-full min-h-[80px] bg-qdarkblue px-8 font-secondary flex justify-between items-center">
    <h1 on:click={() => goto("/")} class="p-2 text-3xl text-white font-secondary font-[700] hover:bg-qlightblue cursor-pointer">QuizApp</h1>
    <button on:click={() => goto("/quiz/create")} class="p-2 hover:bg-qlightblue cursor-pointer"><img src="{plus}" alt="" class="w-[30px] h-[30px]"></button>
  </header>
    <slot />
  <footer class="w-full bg-qdarkblue min-h-[80px] flex justify-center items-center">
    <h1 class="text-3xl text-white font-secondary font-[700]">FishyDino</h1>
  </footer>
</main>