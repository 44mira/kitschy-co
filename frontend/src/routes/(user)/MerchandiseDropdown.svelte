<script lang="ts">
	import Icon from '@iconify/svelte';
	import {
		DropdownMenu,
		DropdownMenuTrigger,
		DropdownMenuItem,
		DropdownMenuContent
	} from '$lib/components/ui/dropdown-menu';
</script>

<DropdownMenu>
	<DropdownMenuTrigger>
		<Icon icon="mdi:hamburger-menu" class="text-3xl text-brand-purple hover:text-brand-purple-m" />
	</DropdownMenuTrigger>
	<DropdownMenuContent></DropdownMenuContent>
</DropdownMenu>
