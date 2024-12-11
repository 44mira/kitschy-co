<script lang="ts">
	import roof from '$lib/assets/users/roof.png';
	import Hero from './Hero.svelte';
	import mockProducts from './mockData';
</script>

<div class="cafe__body max-h-screen min-h-screen flex flex-col">
	<div class="overflow-clip top-0 sticky z-10">
		<img
			src={roof}
			class="object-cover -translate-y-10 w-full scale-75 scale-x-105"
			alt="cafe and pastries roof"
		/>
	</div>
	<Hero />
	<div class="px-6 bg-inherit">
		<div class="min-w-full bg-brand-base min-h-52 grow"></div>
	</div>
</div>

<style>
	.cafe__body {
		background-color: #ffe3cc;
	}

	.cafe__door {
		background-color: #949494;
	}
</style>
