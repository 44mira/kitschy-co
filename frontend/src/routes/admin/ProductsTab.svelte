<script lang="ts">
	import AddProductDialog from './AddProductDialog.svelte';
	import ProductsTable from './ProductsTable.svelte';
	import { type ProductSchema } from '@/api/schema';
	import { mockProducts } from '../(user)/cafe/mockData';
	import Icon from '@iconify/svelte';

	// api call to get products, for now we use mock data
	let products = $state(mockProducts);

	let searchInput = $state('');
	let filteredProducts: ProductSchema[] = $state(products);

	$effect(() => {
		filteredProducts = products.filter((product) => {
			return product.name.toLowerCase().includes(searchInput.toLowerCase());
		});
	});
</script>

<div>
	<!-- SEARCH BAR & FILTER -->
	<div class="flex gap-4 items-center">
		<div class="relative">
			<input
				type="text"
				class="w-50 h-10 pl-10 pr-4 py-2 border border-gray-300 rounded-lg"
				placeholder="Search..."
				bind:value={searchInput}
			/>
			<div
				class="absolute inset-y-0 left-0 pl-3
                  flex items-center
                  pointer-events-none"
			>
				<Icon icon="mdi:search" class="w-6 h-6 text-gray-400" />
			</div>
		</div>

		<div class="flex items-center bg-brand-purple-d rounded-full px-2">
			<select name="filter" id="filter" class="font-giphursSC text-brand-base bg-transparent">
				<option value="sales">By Sales</option>
				<option value="price">By Price</option>
				<option value="stock">By Stock</option>
				<option value="recent">Last Updated</option>
			</select>
		</div>
	</div>

	<!-- -------- -->
	<ProductsTable bind:products={filteredProducts} />
	<div class="z-10 absolute bottom-10 right-24">
		<AddProductDialog />
	</div>
</div>
