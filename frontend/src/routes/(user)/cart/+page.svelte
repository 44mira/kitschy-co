<script lang="ts">
	import Checkout from './Checkout.svelte';
	import pinkFlower from '$lib/assets/users/pink flower.png';
</script>

<div class="bg-brand-base max-h-fill min-h-[91vh] flex flex-col p-36 py-24">
	<div class="grid grid-cols-3 gap-3 grow">
		<div
			class="segment col-span-2 bg-no-repeat bg-center"
			style="background-image: url({pinkFlower})"
		></div>
		<div class="segment min-w-96">
			<Checkout />
		</div>
	</div>
</div>

<style>
	.segment {
		border: 2px solid black;
		border-radius: 2em;
	}
</style>
