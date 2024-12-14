<script lang="ts">
	import { type ProductSchema } from '@/api/schema';
	import { formatDate } from '@/lib/utils';
	import { Badge } from '$lib/components/ui/badge';

	type Props = {
		products: ProductSchema[];
	};

	let { products = $bindable() }: Props = $props();

	// there's probably a cleaner way to do this
	let categories = [
		{ color: '#4D1078', text: 'Merchandise' },
		{ color: '#F1ABFF', text: 'Printing' },
		{ color: '#FB7A4F', text: 'Cafe & Pastries' },
		{ color: '#F9F871', text: 'Mini-Mart' },
		{ color: '#32BEAF', text: 'Workshop' }
	];
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
				<tr onclick={() => {}} class="hover:bg-slate-400">
					<td>{product.images[0]}</td>
					<td>{product.name}</td>
					<td>
						<div class="flex justify-center">
							<Badge
								class="text-crinkles text-center"
								style={`background: ${categories[product.category].color}77; border: 1px solid ${categories[product.category].color}`}
							>
								{categories[product.category].text}
							</Badge>
						</div>
					</td>
					<td class="desc hidden">{product.desc}</td>
					<td class="text-center">{product.price}</td>
					<td class="text-center">{formatDate(product.updated_at)}</td>
					<td class="text-center">{product.quantity}</td>
				</tr>
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
