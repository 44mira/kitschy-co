<script lang="ts">
	import Search from 'lucide-svelte/icons/search';
	import { cn } from '$lib/utils.js';
  import type { HTMLInputAttributes } from 'svelte/elements';

  type Props = {
    input: string;
    classname?: string;
  };

  let { input = $bindable(), classname, ...restProps }: Props & HTMLInputAttributes= $props();

</script>

<div class="flex items-center border-b px-2">
	<Search class="mr-2 h-4 w-4 shrink-0 opacity-50" />
	<input
		class={cn(
			'placeholder:text-muted-foreground flex h-11 w-full rounded-md bg-transparent py-3 text-sm outline-none disabled:cursor-not-allowed disabled:opacity-50',
      classname
		)}
		bind:value={input}
    {...restProps}
	/>
</div>
