<script lang="ts">
	import Separator from '@/lib/components/ui/separator/separator.svelte';
	import Button from '@/lib/components/ui/button/button.svelte';

	import { cart } from './state.svelte.ts';

	const fees = $derived([
		{
			label: 'Merchandise Subtotal',
			value: cart.reduce((s, a) => s + a.product.price * a.quantity, 0)
		},
		{ label: 'Shipping Fee', value: 100 },
		{ label: 'Voucher Discount', value: 0 }
	]);

	const totalFee = $derived(fees.reduce((a, { value }) => a + value, 0).toFixed(2));
</script>

<div class="flex flex-col p-6 sm:p-8 gap-4 min-h-full max-h-full">
	<h2 class="font-giphurs text-2xl sm:text-2xl md:text-3xl">Checkout</h2>
	<Separator class="bg-black w-full sm:px-12 md:px-16 lg:px-20 xl:px-24" />
	<ul class="flex flex-col gap-4 font-giphurs text-base sm:text-lg lg:text-base xl:text-xl py-2">
		{#each fees as fee}
			<li class="flex justify-between gap-4">
				<span>{fee.label}</span>
				<span>{fee.value < 0 ? '-' : ''}₱{Math.abs(fee.value).toFixed(2)}</span>
			</li>
		{/each}
	</ul>
	<Separator class="bg-black w-full sm:px-12 md:px-16 lg:px-20 xl:px-24" />
	<span class="self-end font-giphurs text-lg sm:text-xl md:text-2xl font-bold">₱{totalFee}</span>

	<div class="grow"></div>

	<div class="flex gap-2 items-center text-2xl sm:text-3xl lg:text-2xl xl:text-3xl justify-center font-bold font-giphurs">
		Total: <span class="text-brand-purple">₱{totalFee}</span>
	</div>
	<Button variant="big" class="self-center text-white p-12 sm:p-12 lg:p-10 xl:p-12 max-w-xs sm:max-w-md mb-8">Checkout</Button>
</div>

<style>
	
</style>
