<script lang="ts">
	import EditProductForm from './EditProductForm.svelte';
	import { type ProductSchema } from '@/api/schema';
	import { formatDate } from '@/lib/utils';
	import { Badge } from '$lib/components/ui/badge';
	import * as Dialog from '$lib/components/ui/dialog';

	type Props = {
		product: ProductSchema;
	};
	let { product }: Props = $props();

	let categories = [
		{ color: '#4D1078', text: 'Merchandise' },
		{ color: '#F1ABFF', text: 'Printing' },
		{ color: '#FB7A4F', text: 'Cafe & Pastries' },
		{ color: '#F9F871', text: 'Mini-Mart' },
		{ color: '#32BEAF', text: 'Workshop' }
	];

	let isOpen = $state(false);
</script>

<!-- ROW -->
<tr
	onclick={() => {
		isOpen = true;
	}}
	class="hover:bg-slate-400"
>
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

<!-- DIALOG -->
<Dialog.Root bind:open={isOpen}>
	<Dialog.Content class="bg-[#fff5fe] border-none w-[750px]">
		<EditProductForm bind:isOpen {product} />
	</Dialog.Content>
</Dialog.Root>
