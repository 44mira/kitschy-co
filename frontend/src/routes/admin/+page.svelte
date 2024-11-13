<!-- main page, contains the entire folder system (not separated into their own routes) -->
<script lang="ts">
	import Button from '$lib/components/ui/button/button.svelte';
	import * as DropdownMenu from '$lib/components/ui/dropdown-menu';
	import { toImageUrl } from '$lib/utils/index';
	import polkaBg from '$lib/assets/admin/polkaBg.png';
	import InsightsTab from './InsightsTab.svelte';
	import ProductsTab from './ProductsTab.svelte';
	import OrdersTab from './OrdersTab.svelte';
	import { RadioGroup } from 'bits-ui';

	let tab = $state('insights_tab');
	let durationFilter = $state('Day');
	let presetDurations = ['Day', 'Month', 'Year', 'All Time'];
	let offeringFilter = $state('All');

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
	class="h-[calc(100vh-62px)] w-screen px-10 pt-10 flex flex-col"
	style="background-image: {toImageUrl(polkaBg)}; 
        background-size: cover;
        background-color: {bg_color};"
>
	<!-- TODO: edit css for button variant -->
	<div class="flex justify-around w-full">
		<div id="tabs" class="flex gap-2">
			<Button
				variant="tab"
				onclick={() => switchTab('insights_tab')}
				class="bg-admin-pink text-brand-base">Business Insights</Button
			>
			<Button variant="tab" onclick={() => switchTab('products_tab')} class="bg-admin-blue"
				>Products</Button
			>
			<Button variant="tab" onclick={() => switchTab('orders_tab')} class="bg-admin-green"
				>Order Tracker</Button
			>
		</div>

		<div id="filters" class="h-full flex items-center">
			<DropdownMenu.Root>
				<DropdownMenu.Trigger class="px-5 py-1 rounded-lg bg-brand-purple-d text-brand-base"
					>{durationFilter}</DropdownMenu.Trigger
				>
				<DropdownMenu.Content>
					<DropdownMenu.RadioGroup bind:value={durationFilter}>
						<DropdownMenu.RadioItem value="Day">Day</DropdownMenu.RadioItem>
						<DropdownMenu.RadioItem value="Month">Month</DropdownMenu.RadioItem>
						<DropdownMenu.RadioItem value="Year">Year</DropdownMenu.RadioItem>
						<DropdownMenu.RadioItem value="All Time">All Time</DropdownMenu.RadioItem>
					</DropdownMenu.RadioGroup>
				</DropdownMenu.Content>
			</DropdownMenu.Root>
		</div>
	</div>

	<!-- folder part -->
	<div class="flex-1 bg-[#FFFADE] w-full rounded-t-3xl border border-brand-purple-m px-5 pt-5">
		{#if tab === 'insights_tab'}
			<InsightsTab />
		{:else if tab === 'products_tab'}
			<ProductsTab />
		{:else if tab === 'orders_tab'}
			<OrdersTab />
		{/if}
	</div>
</div>
