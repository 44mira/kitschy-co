<script lang="ts">
	import Navbar from './Navbar.svelte';

	interface Props {
		children?: import('svelte').Snippet;
	}

	let { children }: Props = $props();
</script>

<div class="flex flex-col min-h-screen max-h-screen">
	<Navbar />
	{@render children?.()}
</div>
