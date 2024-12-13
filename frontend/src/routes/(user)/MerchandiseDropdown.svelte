<script lang="ts">
	import Icon from '@iconify/svelte';
	import MerchandiseItem from './MerchandiseItem.svelte';
	import {
		DropdownMenu,
		DropdownMenuTrigger,
		DropdownMenuItem,
		DropdownMenuContent
	} from '$lib/components/ui/dropdown-menu';

	const items = [
		{ label: 'Merchandise', color: 'bg-brand-purple' },
		{ label: 'Cafe & Pastries', color: 'bg-brand-orangeCafe' },
		{ label: 'Printing Services', color: 'bg-brand-pinkPrinting' },
		{ label: 'MiniMart', color: 'bg-brand-yellowMart' },
		{ label: 'Workshop', color: 'bg-brand-mintWorkshop' },
		{ label: 'Membership', color: 'bg-secondary border border-secondary-foreground' }
	];
</script>

<DropdownMenu>
	<DropdownMenuTrigger>
		<Icon
			icon="mdi:hamburger-menu"
			class="h-25 w-25 text-3xl text-brand-purple hover:text-brand-purple-m"
		/>
	</DropdownMenuTrigger>
	<DropdownMenuContent class="mt-5 bg-brand-base p-4 rounded-[0px] rounded-b-2xl">
		{#each items as item}
			<DropdownMenuItem>
				<MerchandiseItem {...item} />
			</DropdownMenuItem>
		{/each}
	</DropdownMenuContent>
</DropdownMenu>
