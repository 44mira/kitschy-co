<script lang="ts">
	import OrdersTable from './OrdersTable.svelte';
	import { type OrderSchema } from '@/api/schema';
	import { mockOrders } from './mockData';
	import Icon from '@iconify/svelte';
	import { Switch } from '$lib/components/ui/switch';

	// api call to get orders, for now we use mock data
	let orders = $state(mockOrders);

	let searchInput = $state('');
	let filteredOrders: OrderSchema[] = $state(orders);

	$effect(() => {
		filteredOrders = orders.filter((order: OrderSchema) => {
			let productNames = order.items.map((item) => item.product.name);

			return productNames.some((name) => name.toLowerCase().includes(searchInput.toLowerCase()));
		});
	});

	let descending = $state(false);
</script>

<div class="h-full flex flex-col">
	<!-- SEARCH BAR & FILTER -->
	<div class="flex gap-4 items-center">
		<div class="relative">
			<input
				type="text"
				class="w-50 h-10 pl-10 pr-4 py-2 border border-gray-300 rounded-lg"
				placeholder="Search product..."
				bind:value={searchInput}
			/>
			<div
				class="absolute inset-y-0 left-0 pl-3
                  flex items-center
                  pointer-events-none"
			>
				<Icon icon="mdi:search" class="w-6 h-6 text-gray-400" />
			</div>
		</div>

		<div class="flex items-center bg-brand-purple-d rounded-full px-2">
			<select name="filter" id="filter" class="font-giphursSC text-brand-base bg-transparent">
				<option value="order_date">Order Date</option>
				<option value="delivery_date">Delivery Date</option>
				<option value="status">Status</option>
				<option value="amount">Amount</option>
			</select>
		</div>

		<!-- ASCENDING DESCENDING SWITCH -->
		<div class="flex bg-brand-purple-m rounded-full w-[6.5rem]">
			<Switch bind:checked={descending} />
			<span class="pl-2">{descending ? 'Desc' : 'Asc'}</span>
		</div>
	</div>

	<!-- -------- -->
	<div class="grow">
		<OrdersTable bind:orders={filteredOrders} />
	</div>
</div>
