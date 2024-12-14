<script lang="ts">
	import HeaderCards from './(headerCards)/HeaderCards.svelte';
	import Hero from './(hero)/Hero.svelte';

	import type { PageData } from './$types';
	export let data: PageData;
</script>

<div class="bg-brand-base flex flex-col items-center justify-center min-h-screen px-8">
	<Hero {data} />
	<HeaderCards />
</div>
