<script lang="ts">
	import { cart } from './state.svelte';
	import CartItemCategory from './CartItemCategory.svelte';

	// requires Node.js 21.x
	// const productsCategories = Object.groupBy(cart, (a) => a.product.category);

	// requires Node.js 20.x
	const productsCategories = cart.reduce((a, x) => {
		a[x.product.category] = a[x.product.category] || [];
		a[x.product.category].push(x);
		return a;
	}, Object.create(null));
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
