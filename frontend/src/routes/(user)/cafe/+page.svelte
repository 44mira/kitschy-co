<script lang="ts">
	import roof from '$lib/assets/users/roof.png';
	import Hero from './Hero.svelte';
	import CafeItem from './CafeItem.svelte';
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
		<div class="min-w-full px-5 py-24 bg-brand-base min-h-52 grow -z-10">
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
