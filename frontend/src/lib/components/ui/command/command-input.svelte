<script lang="ts">
	import Search from 'lucide-svelte/icons/search';
	import type { HTMLInputAttributes } from 'svelte/elements';

	type Props = {
		input: string;
		classname?: string;
	};

	let { input = $bindable(), classname, ...restProps }: Props & HTMLInputAttributes = $props();
</script>

<div class="flex items-center border-b px-2">
	<Search class="ml-4 mr-2 h-4 w-4 shrink-0 opacity-50" />
	<input class={classname} bind:value={input} {...restProps} />
</div>
