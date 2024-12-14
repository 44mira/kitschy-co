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
		{ label: 'Merchandise', color: 'bg-brand-purple', link: 'merch' },
		{ label: 'Cafe & Pastries', color: 'bg-brand-orangeCafe', link: 'cafe' },
		{ label: 'Printing Services', color: 'bg-brand-pinkPrinting', link: 'coming-soon' },
		{ label: 'MiniMart', color: 'bg-brand-yellowMart', link: 'coming-soon' },
		{ label: 'Workshop', color: 'bg-brand-mintWorkshop', link: 'coming-soon' },
		{
			label: 'Membership',
			color: 'bg-secondary border border-secondary-foreground',
			link: 'membership'
		}
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
