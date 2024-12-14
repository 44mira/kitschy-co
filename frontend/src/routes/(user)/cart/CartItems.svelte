<script lang="ts">
	import { cart } from './state.svelte';
	import CartItemCategory from './CartItemCategory.svelte';

	const productsCategories = Object.groupBy(cart, (a) => a.product.category);
</script>

<div class="flex flex-col gap-2 p-12">
	<div class="grid grid-cols-5 gap-4 place-items-center auto-cols-max p-3">
		<div class="col-start-2 text-center">Unit Price</div>
		<div class="text-center">Quantity</div>
		<div class="text-center">Total Price</div>
		<div class="text-center">Actions</div>
	</div>
	<div class="flex flex-col gap-8">
		{#each Object.entries(productsCategories) as [productsCategory, cartItems]}
			<CartItemCategory productsCategory={Number(productsCategory)} {cartItems} />
		{/each}
	</div>
</div>
