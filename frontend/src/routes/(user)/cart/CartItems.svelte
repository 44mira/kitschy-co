<script lang="ts">
	import { cart } from './state.svelte';
	import CartItemCategory from './CartItemCategory.svelte';

	
	const productsCategories = Object.groupBy(cart, (a) => a.product.category);
</script>

<div class="flex flex-col gap-4 p-12">
	<div class="flex flex-col gap-8">
		{#each Object.entries(productsCategories) as [productsCategory, cartItems]}
			<CartItemCategory productsCategory={Number(productsCategory)} {cartItems} />
		{/each}
	</div>
</div>
