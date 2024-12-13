<script lang="ts">
	import type { LayoutData } from './$types';
	import logo from '$lib/assets/logo.png';
	import { slide } from 'svelte/transition';
	import Navbar from './Navbar.svelte';

	interface Props {
		data: LayoutData & { url: string };
		children?: import('svelte').Snippet;
	}

	let { data, children }: Props = $props();
	const duration = 550;
</script>

<div class="flex flex-col min-h-screen max-h-screen bg-brand-base">
	<Navbar />
	<div
		class="absolute inset-x bottom-0 h-[80%] max-h-screen w-full self-center bg-no-repeat bg-contain"
		style="background-image: url({logo}); background-position: 50%"
	></div>
	{#key data.url}
		<div class="z-[1]" in:slide={{ duration, delay: duration }} out:slide={{ duration }}>
			{@render children?.()}
		</div>
	{/key}
</div>
