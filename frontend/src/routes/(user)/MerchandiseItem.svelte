<script lang="ts">
	interface MerchandiseItemProps {
		children?: import('svelte').Snippet;
		color: string;
		label: string;
		link: string;
	}

	let { color, label, link }: MerchandiseItemProps = $props();
</script>

<a href={link}>
	<div class="flex gap-3 text-lg items-center font-giphurs">
		<div class="rounded-3xl h-[1.6em] w-[1.6em] {color}"></div>

		{label}
	</div>
</a>
