<script lang="ts">
	import AddProductDialog from './AddProductDialog.svelte';
	import ProductsTable from './ProductsTable.svelte';
	import { type ProductSchema } from '@/api/schema';
	import mockProducts from '../(user)/cafe/mockData';

	// api call to get products, for now we use mock data
	let products = $state(mockProducts);

	let filteredProducts: ProductSchema[] = $state(products);
</script>

<div>
	<ProductsTable bind:products={filteredProducts} />
	<div class="z-10 absolute bottom-10 right-24">
		<AddProductDialog />
	</div>
</div>
