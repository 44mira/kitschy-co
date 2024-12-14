<script lang='ts'>
	import AddProductDialog from './AddProductDialog.svelte';
  import ProductsTable from './ProductsTable.svelte';
	import { addProductSchema, type AddProductSchema } from '@/api/adminSchema';
	import {type ProductSchema } from '@/api/schema';
	import mockProducts from '../(user)/cafe/mockData';

  // api call to get products, for now we use mock data
  let products = $state(mockProducts);
  
  let filteredProducts : ProductSchema[] = $state(products);
  
  let addProduct: AddProductSchema = $state(addProductSchema)
</script>

<div>
  <ProductsTable bind:products={filteredProducts} />
	<AddProductDialog/>
</div>
