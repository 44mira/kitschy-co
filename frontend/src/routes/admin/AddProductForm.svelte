<script lang="ts">
	import * as Form from '$lib/components/ui/form';
	import * as Dialog from '$lib/components/ui/dialog';
	import { Button } from '$lib/components/ui/button';
	import { addProductSchema, type AddProductSchema } from '@/api/adminSchema';
	import SuperDebug, { type SuperValidated, type Infer, superForm } from 'sveltekit-superforms';
	import { zodClient } from 'sveltekit-superforms/adapters';
	import Icon from '@iconify/svelte';
	import { getContext } from 'svelte';
	import ProductForm from './ProductForm.svelte';

	const icons = {
		add: 'mdi:add',
		delete: 'mdi:delete-forever-outline',
		save: 'mdi:content-save-outline',
		close: 'mdi:close'
	};

	let data: SuperValidated<Infer<AddProductSchema>> = getContext('addProductForm');
	let { isOpen = $bindable() } = $props();

	const addProduct = superForm(data, {
		validators: zodClient(addProductSchema)
	});

	const { form: formData, enhance } = addProduct;
</script>

<form action="?/addProduct" method="POST" enctype="multipart/form-data" use:enhance>
	<ProductForm form={addProduct} />

	<div id="actions" class="flex justify-end gap-4">
		<!-- CLOSE BUTTON -->
		<Dialog.Root>
			<Dialog.Trigger
				class="bg-transparent border-[2px] border-gray-400 text-gray-400 text-lg gap-1 hover:border-text-crinkles hover:text-crinkles w-fit flex items-center justify-center rounded-md px-3 py-1"
			>
				<Icon icon={icons.delete} class="w-6 h-6" />
				<span>Cancel</span>
			</Dialog.Trigger>
			<Dialog.Content
				class="bg-white flex flex-col items-center justify-center pt-14 px-10 rounded-2xl"
			>
				<span>Are you sure you wish to cancel?</span>
				<div class="w-full flex justify-around pt-6">
					<Dialog.Close>
						<Button
							variant="outline"
							class="text-destructive hover:text-destructive hover:bg-destructive/20 border-destructive border-2"
							onclick={() => {
								isOpen = false;
							}}>Yes</Button
						>
					</Dialog.Close>
					<Dialog.Close>
						<Button
							variant="outline"
							class="text-[#126A99] hover:text-[#126A99] hover:bg-[#126A99]/20 border-[#126A99] border-2"
							>No</Button
						>
					</Dialog.Close>
				</div>
			</Dialog.Content>
		</Dialog.Root>

		<Form.Button
			variant="outline"
			class="bg-[#99D8FA] hover:bg-[#6f9efc] border-[2px] border-[#126A99] text-crinkles text-lg gap-1"
		>
			<Icon icon={icons.save} class="w-6 h-6" />
			<span>Add Item</span></Form.Button
		>
	</div>
</form>
