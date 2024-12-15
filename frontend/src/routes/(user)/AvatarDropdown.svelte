<script lang="ts">
	import AvatarItem from './AvatarItem.svelte';
	import { Avatar, AvatarImage, AvatarFallback } from '$lib/components/ui/avatar';
	import {
		DropdownMenu,
		DropdownMenuTrigger,
		DropdownMenuItem,
		DropdownMenuContent
	} from '$lib/components/ui/dropdown-menu';

	const items = [
		{ label: 'Profile', icon: 'mdi:face-man-shimmer', link: 'profile' },
		{ label: 'Orders', icon: 'mdi:package-variant', link: 'orders' },
		{ label: 'Sign-out', icon: 'mdi:logout', link: 'home' },
		{ label: 'Membership', icon: 'mdi:tag-heart', link: 'membership' }
	];
</script>

<DropdownMenu>
	<DropdownMenuTrigger>
		<Avatar>
			<AvatarImage src="https://github.com/shadcn.png" alt="@shadcn" class="h-25 w-25" />
			<AvatarFallback>CN</AvatarFallback>
		</Avatar>
	</DropdownMenuTrigger>
	<DropdownMenuContent class="mt-5 bg-brand-base p-4 rounded-[0px] rounded-b-2xl">
		{#each items as item}
			<DropdownMenuItem>
				<AvatarItem {...item} />
			</DropdownMenuItem>
		{/each}
	</DropdownMenuContent>
</DropdownMenu>
