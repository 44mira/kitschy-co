<script lang="ts">
	import * as Dialog from '$lib/components/ui/dialog';
	import { type AddProductSchema } from '../../lib/api/adminSchema';
	import { type SuperValidated, type Infer } from 'sveltekit-superforms';
	import Icon from '@iconify/svelte';
	import AddProductsForm from './AddProductsForm.svelte';

	const icons = {
		add: 'mdi:add',
		delete: 'mdi:delete-forever-outline',
		save: 'mdi:content-save-outline',
		close: 'mdi:close'
	};

	let { data }: { data: SuperValidated<Infer<AddProductSchema>> } = $props();

	let isOpen = $state(false);
</script>

<Dialog.Root bind:open={isOpen}>
	<Dialog.Trigger
		class="w-[75px] h-[75px] bg-[#094F7B4D] hover:bg-[#094F7B] flex items-center justify-center rounded-3xl z-10"
	>
		<Icon icon={icons.add} class="text-brand-base w-[70px] h-[70px]" />
	</Dialog.Trigger>
	<Dialog.Content class="bg-[#fff5fe] border-none w-[750px]">
		<AddProductsForm {data} />
	</Dialog.Content>
</Dialog.Root>
