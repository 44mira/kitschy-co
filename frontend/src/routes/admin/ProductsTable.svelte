<script lang="ts">
	import { type ProductSchema } from '@/api/schema';
	type Props = {
		products: ProductSchema[];
	};

	let { products = $bindable() }: Props = $props();
</script>
