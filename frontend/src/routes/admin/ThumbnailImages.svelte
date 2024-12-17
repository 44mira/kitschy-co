<script lang="ts">
	import { type ProductSchema } from '@/api/schema';
	type Props = {
		products: ProductSchema[];
		order?: boolean;
	};
	let { products, order = false }: Props = $props();
</script>

<div class="flex items-center" style="position: relative;">
	{#if order}
		{#each products.slice(0, 4) as product, index}
			{#if index < 3}
				<img
					src={product.images[0].img_url}
					alt={product.name}
					class="h-12 w-12 object-cover rounded-lg mr-[-35px] lg:mr-[-15px]"
				/>
			{:else}
				<div class="h-fit w-fit flex items-center px-2 rounded-lg ml-[35px] lg:ml-[15px]">
					<span>+ {products.length - index}</span>
				</div>
			{/if}
		{/each}
	{:else}
		{#each products[0].images as image, index}
			{#if index < 3}
				<img
					src={image.img_url}
					alt={products[0].name}
					class="h-12 w-12 object-cover rounded-lg mr-[-35px] lg:mr-[-15px]"
				/>
			{:else}
				<div class="h-fit w-fit flex items-center px-2 rounded-lg ml-[35px] lg:ml-[15px]">
					<span>+ {products[0].images.length - index}</span>
				</div>
			{/if}
		{/each}
	{/if}
</div>
