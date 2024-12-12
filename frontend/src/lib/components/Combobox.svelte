<script lang="ts">
	import Check from 'lucide-svelte/icons/check';
	import ChevronsUpDown from 'lucide-svelte/icons/chevrons-up-down';
	import * as Command from '$lib/components/ui/command';
	import * as Popover from '$lib/components/ui/popover';
	import { Button } from '$lib/components/ui/button';
	import { cn } from '$lib/utils.js';
	import { tick } from 'svelte';

	type Props = {
		data: { value: string; label: string }[];
		chosenValue: string;
	};
	let { data, chosenValue = $bindable() }: Props = $props();

	let open = $state(false);
	let value = $state('');

	let input = $state('');
	let filteredData = $derived(
		data.filter((f) => f.label.toLowerCase().includes(input.toLowerCase()))
	);
	let chosen = $derived(data.find((f) => f.value === value)?.label ?? 'Select a choice...');

	$effect(() => {
		chosenValue = value;
	});

	$effect(() => {
		console.log(input);
	});
 
	// We want to refocus the trigger button when the user selects
	// an item from the list so users can continue navigating the
	// rest of the form with the keyboard.
	function closeAndFocusTrigger(triggerId: string) {
		open = false;
		tick().then(() => {
			document.getElementById(triggerId)?.focus();
		});
	}
</script>

<Popover.Root bind:open let:ids>
	<Popover.Trigger asChild let:builder>
		<Button
			builders={[builder]}
			variant="ghost"
			role="combobox"
			aria-expanded={open}
			class="w-[200px] p-0 justify-between pr-3 text-crinkles"
		>
			{chosen}
			<ChevronsUpDown class="ml-2 h-5 w-5 shrink-0 text-brand-purple" />
		</Button>
	</Popover.Trigger>
	<Popover.Content class="w-[200px] p-0">
		<Command.Root>
			<Command.Input placeholder="Search choice..." bind:input />
			<Command.Empty>No choice found.</Command.Empty>
			<Command.Group>
				{#each filteredData || data as choice}
					<Command.Item
						value={choice.value}
						onSelect={(currentValue: string) => {
							value = currentValue;
							closeAndFocusTrigger(ids.trigger);
						}}
					>
						<Check class={cn('mr-2 h-4 w-4', value !== choice.value && 'text-transparent')} />
						{choice.label}
					</Command.Item>
				{/each}
			</Command.Group>
		</Command.Root>
	</Popover.Content>
</Popover.Root>
