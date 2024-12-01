<script lang="ts">
	interface MerchandiseItemProps {
		children?: import('svelte').Snippet;
		color: string;
		label: string;
	}

	let { color, label }: MerchandiseItemProps = $props();

	const circleRadius = '[25px]';
</script>

<div class="flex gap-3 text-lg items-center font-giphurs">
	<div class="rounded-3xl h-{circleRadius} w-{circleRadius} {color}"></div>
	{label}
</div>
