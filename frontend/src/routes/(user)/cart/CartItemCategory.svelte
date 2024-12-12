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

<div class="border-2 border-black rounded-3xl">
	<div class="flex gap-4 items-center p-3 border-b-2 border-black">
		<Checkbox />
		<h1 class="font-giphurs text-2xl">{categoryLabels[productsCategory]}</h1>
	</div>
	<ul>
		{#each cartItems as { quantity, product }, i}
			<li class="flex gap-4 items-center py-4 pl-4 font-giphurs">
				<Checkbox />
				<span>{product.name}</span>
				<div class="grow"></div>
				<div class="grid grid-cols-4 items-center justify-items-center">
					<span>₱{product.price}</span>
					<div class="flex items-center gap-3">
						<Button
							variant="outline"
							size="icon"
							class="bg-brand-base border-dotted border-black hover:bg-brand-purple-l"
							onclick={() => (cartItems[i].quantity = Math.max(0, Number(quantity) - 1))}>-</Button
						>
						<input type="number" bind:value={cartItems[i].quantity} />
						<Button
							variant="outline"
							size="icon"
							class="bg-brand-base border-dotted border-black hover:bg-brand-purple-l"
							onclick={() => (cartItems[i].quantity = Number(quantity) + 1)}>+</Button
						>
					</div>
					<div class="w-24 text-center truncate">₱{(product.price * quantity).toFixed(2)}</div>
					<Button size="icon" class="bg-transparent hover:bg-brand-purple-l">
						<Icon icon="mdi:trash-can" class="text-brand-purple text-2xl"></Icon>
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
		max-width: 2.3em;
		text-align: center;
	}
</style>
