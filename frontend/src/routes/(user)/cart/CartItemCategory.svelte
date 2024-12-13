<script lang="ts">
	import { type CartItemSchema, CATEGORY } from '@/api/schema';
	import Button from '@/lib/components/ui/button/button.svelte';
	import Checkbox from '@/lib/components/ui/checkbox/checkbox.svelte';
	import Icon from '@iconify/svelte';

	type CartItemCategoryProps = {
		cartItems: CartItemSchema[];
		productsCategory: CATEGORY;
		children?: import('svelte').Snippet;
	};

	const categoryLabels = {
		[CATEGORY.MERCH]: "Kitschy's Merchandise",
		[CATEGORY.CAFE]: 'Cafe & Pastries',
		[CATEGORY.PRINT]: "Misbeek's Printing",
		[CATEGORY.MINIMART]: 'Mini-mart',
		[CATEGORY.WORKSHOP]: 'Kitschy Workshop'
	};

	const { productsCategory, cartItems: _cartItems }: CartItemCategoryProps = $props();
	const cartItems = $state(_cartItems);
</script>

<div class="border-2 border-black rounded-3xl overflow-hidden">
	<div class="flex items-center gap-4 p-3 border-b-2 border-black">
		<Checkbox />
		<h1 class="font-giphurs text-xl md:text-2xl">{categoryLabels[productsCategory]}</h1>
	</div>
	<ul class="flex flex-col gap-4 p-4">
		{#each cartItems as { quantity, product }, i}
			<li class="grid grid-cols-[auto,1fr,auto,auto,auto,auto] items-center gap-4 py-4 px-4 font-giphurs text-sm sm:text-base md:text-lg">
				<Checkbox />
				<div class="flex flex-col items-start">
					<span class="break-words">{product.name}</span>
				</div>

				<!-- Unit Price with Label -->
				<div class="flex flex-col items-start">
					<p class="text-xs sm:text-sm">Unit Price</p>
					<span class="break-words">₱{product.price}</span>
				</div>

				<!-- Quantity with Label -->
				<div class="flex flex-col items-start">
					<p class="text-xs sm:text-sm ml-[52px] mb-2">Quantity</p>
					<div class="flex items-center gap-4">
						<Button
							variant="outline"
							size="icon"
							class="bg-brand-base border-dotted border-black hover:bg-brand-purple-l text-sm sm:text-base"
							onclick={() => (cartItems[i].quantity = Math.max(0, Number(quantity) - 1))}>-</Button>
						<input
							type="number"
							bind:value={cartItems[i].quantity}
							class="w-12 text-center text-sm sm:text-base md:text-lg border border-black rounded"
						/>
						<Button
							variant="outline"
							size="icon"
							class="bg-brand-base border-dotted border-black hover:bg-brand-purple-l text-sm sm:text-base"
							onclick={() => (cartItems[i].quantity = Number(quantity) + 1)}>+</Button>
					</div>
				</div>

				<!-- Total Price with Label -->
				<div class="flex flex-col items-start">
					<p class="text-xs sm:text-sm">Total Price</p>
					<span class="text-sm sm:text-base md:text-lg">₱{(product.price * quantity).toFixed(2)}</span>
				</div>

				<!-- Actions with Label -->
				<div class="flex flex-col items-start">
					<p class="text-xs sm:text-sm mr-4">Actions</p>
					<Button size="icon" class="bg-transparent hover:bg-brand-purple-l">
						<Icon icon="mdi:trash-can" class="text-brand-purple text-lg sm:text-xl ml-2" />
					</Button>
				</div>
			</li>
		{/each}
	</ul>
</div>

<style>
	input::-webkit-outer-spin-button,
	input::-webkit-inner-spin-button {
		-webkit-appearance: none;
		margin: 0;
	}

	input[type='number'] {
		-moz-appearance: textfield;
		appearance: textfield;

		background-color: transparent;
		text-align: center;
		max-width: 3em;
	}

	/* Allow product name and price to wrap and not overflow */
	.break-words {
		word-wrap: break-word;
	}

	/* Ensures items are displayed properly on small screens */
	ul {
		overflow-x: auto;  /* Enable horizontal scrolling */
		padding: 0;
	}

	/* Make input fields and buttons responsive on smaller screens */
	@media (max-width: 600px) {
		/* Adjust button and input sizes */
		.text-sm {
			font-size: 0.875rem; /* Smaller text for mobile */
		}
		.w-12 {
			width: 2.5rem; /* Adjust input width */
		}
	}

	/* Ensure layout scales well on larger screens */
	@media (min-width: 768px) {
		.text-sm {
			font-size: 1rem;
		}
	}
</style>
