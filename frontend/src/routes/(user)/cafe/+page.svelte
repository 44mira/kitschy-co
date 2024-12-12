<script lang="ts">
	import roof from '$lib/assets/users/roof.png';
	import Hero from './Hero.svelte';
	import CafeItem from './CafeItem.svelte';
	import mockProducts from './mockData';
</script>

<div class="cafe__body max-h-screen min-h-screen flex flex-col">
	<!-- Sticky Header -->
	<div class="overflow-clip top-0 sticky z-10">
		<img
	src={roof}
	class="object-cover -translate-y-10 w-full scale-75 scale-x-105 min-h-[175px] sm:min-h-[175px] md:min-h-[200px] lg:min-h-[200px]"
	alt="cafe and pastries roof"
/>
	</div>

	<Hero />

	<!-- Content Section -->
	<div class="px-4 sm:px-6 md:px-8 bg-inherit">
		<div class="m-4 sm:m-4 md:m-4 bg-brand-base min-h-52 grow relative -mt-[150px] sm:-mt-[200px] p-4 sm:p-6 md:p-8 rounded-lg">
			<div class="grid xl:grid-cols-4 lg:grid-cols-3 md:grid-cols-2 grid-cols-1 gap-10">
				{#each mockProducts as mockProduct}
					<CafeItem {...mockProduct} />
				{/each}
			</div>
		</div>
	</div>
</div>

<style>
	.cafe__body {
		background-color: #ffe3cc;
	}
</style>
