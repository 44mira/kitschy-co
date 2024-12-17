<script lang="ts">
	import MerchandiseItem from './MerchandiseItem.svelte';
	import Carousel from './Carousel.svelte'; // Import the carousel component
	import { mockProducts } from './mockData';
	import { onMount } from 'svelte';

	// delay the fall
	let isFalling = $state(false);
	onMount(() => {
		isFalling = true;
	});

	const generateTilt = () => {
		/* in degrees */
		const maxTilt = 30;
		const bias = 10; // flat starting to increase tilt bounds

		const tilt = Math.random() * maxTilt + bias;
		return tilt - (maxTilt + bias) / 2;
	};
</script>

<div class="bg-brand-base max-h-fill min-h-[91vh]">
	<!-- Carousel Section -->
	<Carousel />

	<!-- Products  -->
	<div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-5 p-10">
		{#each mockProducts as product}
			<MerchandiseItem {product} tilt={`${generateTilt()}deg`} {isFalling} />
		{/each}
	</div>
</div>
