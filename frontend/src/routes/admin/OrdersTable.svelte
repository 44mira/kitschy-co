<script lang="ts">
	import { type OrderSchema } from '@/api/schema';
	import { formatDate } from '@/lib/utils';
	import { Badge } from '$lib/components/ui/badge';
	import { ORDER_STATUS, PAYMENT_METHOD } from '@/api/schema';
	import ThumbnailImages from './ThumbnailImages.svelte';

	type Props = {
		orders: OrderSchema[];
	};

	let { orders = $bindable() }: Props = $props();

	// there's probably a cleaner way to do this
	let statusColors = {
		[ORDER_STATUS.PENDING]: {
			text: 'Pending',
			color: '#FFD700'
		},
		[ORDER_STATUS.PROCESSING]: {
			text: 'Processing',
			color: '#FFA500'
		},
		[ORDER_STATUS.DELIVERED]: {
			text: 'Delivered',
			color: '#32CD32'
		},
		[ORDER_STATUS.CANCELLED]: {
			text: 'Cancelled',
			color: '#FF0000'
		}
	};

	let paymentMethods = {
		[PAYMENT_METHOD.COD]: {
			text: 'COD',
			color: '#FFD700'
		},
		[PAYMENT_METHOD.ONLINE]: {
			text: 'Online',
			color: '#FFA500'
		}
	};

	function getName(uid: string) {
		let user = {
			first_name: 'Sharif',
			last_name: 'Khan'
		};

		return `${user.first_name} ${user.last_name}`;
	}
</script>

<div class="overflow-scroll h-full">
	<table class="w-full">
		<thead class="border-b-2 border-brand-purple-d">
			<tr>
				<th class="w-20">Order ID</th>
				<th class="min-w-36 w-[15%]">Products</th>
				<th class="min-w-20 w-fit">Name</th>
				<th class="">Method</th>
				<th class="min-w-20 w-[10%]">Order Date</th>
				<th class="min-w-20 w-[10%]">Delivery Date</th>
				<th class="min-w-20 w-[10%]">Status</th>
				<th class="min-w-20 w-[10%]">Amount</th>
			</tr>
		</thead>

		<tbody>
			{#each orders as order}
				<tr onclick={() => {}}>
					<td>{order.order_id}</td>

					<td>
						<ThumbnailImages products={order.items.map((i) => i.product)} order={true}/>
					</td>

					<td>{getName(order.user)}</td>

					<td>
						<div class="flex justify-center">
							<Badge
								class="text-crinkles text-center"
								style={`background: ${paymentMethods[order.method].color}77; border: 1px solid ${paymentMethods[order.method].color}`}
							>
								{paymentMethods[order.method].text}
							</Badge>
						</div>
					</td>

					<td class="text-center">{formatDate(order.created_at)}</td>
					<td class="text-center">{formatDate(order.delivery_date)}</td>

					<td>
						<div class="flex justify-center">
							<Badge
								class="text-crinkles text-center"
								style={`background: ${statusColors[order.status].color}77; border: 1px solid ${statusColors[order.status].color}`}
							>
								{statusColors[order.status].text}
							</Badge>
						</div>
					</td>

					<td>₱{order.total.toFixed(2)}</td>
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
