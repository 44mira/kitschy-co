<script lang="ts">
	import { type ProductSchema } from '@/api/schema';
  import ProductRow from './ProductRow.svelte';

	type Props = {
		products: ProductSchema[];
	};

	let { products = $bindable() }: Props = $props();

</script>

<div class="overflow-scroll h-full">
	<table class="w-full">
		<thead class="border-b-2 border-brand-purple-d">
			<tr>
				<th class="w-20">Image</th>
				<th class="min-w-20 w-[15%]">Product Name</th>
				<th class="min-w-20 w-fit">Category</th>
				<th class="hidden lg:block min-w-20 w-[15%]">Description</th>
				<th class="min-w-20 w-[10%]">Price</th>
				<th class="min-w-28 max-w-40">Last Updated</th>
				<th class="min-w-20 w-[10%]">In Stock</th>
				<th class="min-w-20 w-[10%]">Orders</th>
			</tr>
		</thead>

		<tbody>
			{#each products as product}
				<ProductRow {product} />
			{/each}
		</tbody>
	</table>
</div>

<style>
	th {
		@apply font-normal text-brand-purple-d font-giphurs text-lg;
	}

	th,
	td {
		@apply px-3 py-1;
	}

	@media only screen and (min-width: 1024px) {
		.desc {
			@apply line-clamp-1;
		}
	}
</style>
