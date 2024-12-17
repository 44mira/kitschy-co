<script lang="ts">
	import { categories } from './admin.ts';
	import EditProductForm from './EditProductForm.svelte';
	import { type ProductSchema } from '@/api/schema';
	import { formatDate } from '@/lib/utils';
	import { Badge } from '$lib/components/ui/badge';
	import * as Dialog from '$lib/components/ui/dialog';
	import ThumbnailImages from './ThumbnailImages.svelte';

	type Props = {
		product: ProductSchema;
	};
	let { product }: Props = $props();

	let isOpen = $state(false);
</script>

<!-- ROW -->
<tr
	onclick={() => {
		isOpen = true;
	}}
	class="hover:bg-slate-400"
>
	<td>
		<ThumbnailImages products={[product]}/>
	</td>
	<td>{product.name}</td>
	<td>
		<div class="flex justify-center">
			<Badge
				class="text-crinkles text-center"
				style={`background: ${categories[product.category].color}77; border: 1px solid ${categories[product.category].color}`}
			>
				{categories[product.category].label}
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

<style>
	@media only screen and (min-width: 1024px) {
		.desc {
			@apply line-clamp-1;
		}
	}

	td {
		@apply px-3 py-1;
	}
</style>
