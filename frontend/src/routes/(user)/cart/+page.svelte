<script lang="ts">
	import Checkout from './Checkout.svelte';
	import CartItems from './CartItems.svelte';
	import pinkFlower from '$lib/assets/users/pink flower.png';
</script>

<div class="bg-brand-base max-h-fill min-h-[91vh] flex flex-col p-6 sm:p-6 md:p-12 lg:p-24 py-12 sm:py-16 md:py-24 overflow-x-hidden">
	<div class="grid grid-cols-1 md:grid-cols-1 lg:grid-cols-3 gap-6 grow">
		<!-- Cart Items Section -->
		<div
			class="segment col-span-2 bg-no-repeat bg-center bg-cover p-4 sm:p-6 md:p-8"
			style="background-image: url({pinkFlower})"
		>
			<CartItems />
		</div>
		<!-- Checkout Section -->
		<div class="segment p-4 sm:p-6 md:p-8">
			<Checkout />
		</div>
	</div>
</div>

<style>
	.segment {
		border: 2px solid black;
		border-radius: 2em;
	}

	/* Adjust the width of the checkout section for different screen sizes */
	@media (max-width: 1024px) {
		.segment {
			min-width: 300px; /* Adjust to prevent shrinking too much */
		}
	}

	/* Ensure the checkout section doesn't shrink too much on mobile */
	@media (max-width: 600px) {
		.segment {
			min-width: 250px; /* Prevent the checkout section from being too narrow */
		}
	}
</style>
