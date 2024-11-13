<!-- main page, contains the entire folder system (not separated into their own routes) -->
<script lang="ts">
	import { toImageUrl } from '$lib/utils/index';
	import polkaBg from '$lib/assets/admin/polkaBg.png';
	import Button from '$lib/components/ui/button/button.svelte';

	let tab = $state('insights_tab');
	let bg_colors = {
		insights_tab: '#FFD9E7',
		products_tab: '#D3F0FF',
		orders_tab: '#F6FFDE'
	};
	let bg_color = $state(bg_colors['insights_tab']);

	function switchTab(t: string) {
		tab = t;
		bg_color = bg_colors[tab as keyof typeof bg_colors];
	}
</script>

<div
	class="h-[calc(100vh-62px)] w-screen px-10 pt-10"
	style="background-image: {toImageUrl(polkaBg)}; 
        background-size: cover;
        background-color: {bg_color};"
>
	<!-- TODO: edit css for button variant -->
	<div id="tabs" class="flex gap-2 pl-5">
		<Button variant="tab" onclick={() => switchTab('insights_tab')}>Business Insights</Button>
		<Button variant="tab" onclick={() => switchTab('products_tab')}>Products</Button>
		<Button variant="tab" onclick={() => switchTab('orders_tab')}>Order Tracker</Button>
	</div>

	<!-- folder part -->
	<div class="bg-[#FFFADE] h-full w-full rounded-t-3xl border border-[#804B7A] px-5 pt-5">

	</div>
</div>
