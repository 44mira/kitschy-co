<script lang="ts">
	import { cart } from './state.svelte';
	import CartItemCategory from './CartItemCategory.svelte';

	const columnLabels = ['Unit Price', 'Quantity', 'Total Price', 'Actions'];
	const productsCategories = Object.groupBy(cart, (a) => a.product.category);
</script>

<div class="flex flex-col gap-4 p-12">
	<div class="grid grid-cols-4 gap-[66px] self-end px-6">
		{#each columnLabels as columnLabel}
			<span>{columnLabel}</span>
		{/each}
	</div>
	<div class="flex flex-col gap-8">
		{#each Object.entries(productsCategories) as [productsCategory, cartItems]}
			<CartItemCategory productsCategory={Number(productsCategory)} {cartItems} />
		{/each}
	</div>
</div>
