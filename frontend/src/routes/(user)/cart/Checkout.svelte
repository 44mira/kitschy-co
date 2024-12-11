<script lang="ts">
	import Separator from '@/lib/components/ui/separator/separator.svelte';
	import Button from '@/lib/components/ui/button/button.svelte';

	const fees = $derived([
		{ label: 'Merchandise Subtotal', value: 2100 },
		{ label: 'Shipping Fee', value: 2100 },
		{ label: 'Voucher Discount', value: -2100 }
	]);

	const totalFee = $derived(fees.reduce((a, { value }) => a + value, 0));
</script>

<div class="flex flex-col p-8 gap-3 min-h-full max-h-full">
	<h2 class="font-giphurs text-3xl">Checkout</h2>
	<Separator class="bg-black px-28" />
	<ul class="flex flex-col gap-3 font-giphurs text-lg py-2">
		{#each fees as fee}
			<li class="flex justify-between">
				<span>{fee.label}</span>
				<span>{fee.value < 0 ? '-' : ''}₱{Math.abs(fee.value)}</span>
			</li>
		{/each}
	</ul>
	<Separator class="bg-black px-28" />
	<span class="self-end font-giphurs text-lg font-bold">₱{totalFee}</span>

	<div class="grow"></div>

	<div class="flex gap-2 items-center text-2xl justify-center font-bold font-giphurs">
		Total: <span class="text-brand-purple">₱{totalFee}</span>
	</div>
	<Button variant="big" class="self-center text-white p-16 max-w-64 mb-8">Checkout</Button>
</div>
