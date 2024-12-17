<script lang="ts">
	import * as Dialog from '$lib/components/ui/dialog';
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
			<Dialog.Root>
				<Dialog.Trigger>
					<MerchandiseItem {product} tilt={`${generateTilt()}deg`} {isFalling} />
				</Dialog.Trigger>
				<Dialog.Content class="bg-white w-[700px]">
					<!-- Product Details -->
					<p class="text-2xl font-giphursSC">{product.name}</p>
					<div class="flex gap-10">
						<!-- image -->
						<div class="shrink-0 rounded-xl bg-brand-purple-l border-4 border-brand-purpleMerch">
							<img
								class="rounded-xl h-[300px] w-[300px]"
								src={product.images[0].img_url}
								alt={product.images[0].alt_desc}
							/>
						</div>
						<div class="grow flex flex-col gap-2">
							<div class="flex gap-3">
								<p>Price:</p>
								<p>₱{product.price.toFixed(2)}</p>
							</div>
							<p>Description:</p>
							<p>{product.desc}</p>
						</div>
					</div>
				</Dialog.Content>
			</Dialog.Root>
		{/each}
	</div>
</div>
