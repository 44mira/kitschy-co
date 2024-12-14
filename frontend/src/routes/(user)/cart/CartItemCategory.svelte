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
		<div class="overflow-x-auto">
			<!-- Parent grid for products -->
			<div class="min-w-[600px] px-8 mb-4">
				<!-- Labels for the first item -->
				<div class="grid grid-cols-5 gap-4 p-4 font-bold">
					<div class="text-center">Product</div>
					<div class="text-center">Unit Price</div>
					<div class="text-center">Quantity</div>
					<div class="text-center">Total Price</div>
					<div class="text-center">Actions</div>
				</div>

				{#each cartItems as { product, quantity }, i}
				<!-- Grid for each product's row -->
				<div class="grid grid-cols-5 gap-4 p-4">
					<!-- Product Column -->
					<div class="flex items-center gap-4">
						<Checkbox />
						<div class="flex flex-col">
							<span class="text-xs lg:text-sm">{product.name}</span>
						</div>
					</div>

					<!-- Unit Price Column -->
					<div class="text-center">
						<span class="break-words">₱{product.price.toFixed(2)}</span>
					</div>

					<!-- Quantity Column -->
					<div class="text-center">
						<div class="flex items-center gap-2">
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

					<!-- Total Price Column -->
					<div class="text-center">
						<span class="break-words">₱{(product.price * quantity).toFixed(2)}</span>
					</div>

					<!-- Actions Column -->
					<div class="text-center">
						<div>
							<Button size="icon" class="bg-transparent hover:bg-brand-purple-l">
								<Icon icon="mdi:trash-can" class="text-brand-purple text-lg sm:text-xl" />
							</Button>
						</div>
					</div>
				</div>
				{/each}
			</div>
		</div>
	</ul>
</div>

<style>
	.break-words {
	  word-wrap: break-word;
	}

	.overflow-x-auto {
	  overflow-x: auto;
	}

	input[type='number'] {
	  -moz-appearance: textfield;
	  appearance: textfield;
	  background-color: transparent;
	  text-align: center;
	  max-width: 3em;
	}

	input::-webkit-outer-spin-button,
	input::-webkit-inner-spin-button {
	  -webkit-appearance: none;
	  margin: 0;
	}

	@media (max-width: 600px) {
	  .text-sm {
		font-size: 0.875rem;
	  }
	  .w-12 {
		width: 2.5rem;
	  }
	}

	@media (min-width: 768px) {
	  .text-sm {
		font-size: 1rem;
	  }
	}
</style>
