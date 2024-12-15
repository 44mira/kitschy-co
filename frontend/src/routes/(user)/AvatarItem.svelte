<script lang="ts">
	import Icon from '@iconify/svelte';
	interface AvatarItemProps {
		children?: import('svelte').Snippet;
		icon: string;
		label: string;
		link: string;
	}

	let { icon, label, link }: AvatarItemProps = $props();
</script>

<a href={link}>
	<div class="flex gap-3 text-lg items-center text-brand-purple font-giphurs">
		<Icon {icon} class="text-3xl text-brand-purple"></Icon>

		{label}
</div>
</a>
