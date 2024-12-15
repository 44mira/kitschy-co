<script lang="ts">
	import { icons } from './admin.ts';
	import ProductForm from './ProductForm.svelte';
	import * as Form from '$lib/components/ui/form';
	import * as Dialog from '$lib/components/ui/dialog';
	import { Button } from '$lib/components/ui/button';
	import { addProductSchema, type AddProductSchema } from '@/api/adminSchema';
	import { type SuperValidated, type Infer, superForm } from 'sveltekit-superforms';
	import { zodClient } from 'sveltekit-superforms/adapters';
	import Icon from '@iconify/svelte';
	import { getContext } from 'svelte';

	let data: SuperValidated<Infer<AddProductSchema>> = getContext('addProductForm');
	let { isOpen = $bindable(), product } = $props();

	const addProductForm = superForm(data, {
		validators: zodClient(addProductSchema)
	});
</script>

<form method="POST">
	<ProductForm form={addProductForm} values={product} />

	<div id="actions" class="flex justify-end gap-4">
		<!-- CLOSE BUTTON -->
		<Dialog.Root>
			<Dialog.Trigger
				class="bg-transparent border-[2px] border-destructive text-destructive text-lg gap-1 hover:border-text-crinkles hover:text-crinkles w-fit flex items-center justify-center rounded-md px-3 py-1"
			>
				<Icon icon={icons.delete} class="w-6 h-6" />
				<span>Delete</span>
			</Dialog.Trigger>

			<Dialog.Content
				class="bg-white flex flex-col items-center justify-center pt-14 px-10 rounded-2xl"
			>
				<span>
					This will <span class="font-bold">permanently delete</span> all files and order data related
					to this product.
				</span>
				<span>
					If you plan on bringing this item back in the future, consider
					<span class="font-bold">archiving</span> instead.
				</span>

				<div class="w-full flex justify-around pt-6">
					<Dialog.Close>
						<Button
							variant="outline"
							class="flex gap-1 text-destructive hover:text-destructive hover:bg-destructive/20 border-destructive border-2"
							onclick={() => {
								isOpen = false;
							}}
						>
							<Icon icon={icons.delete} class="w-6 h-6 font-bold" />
							<span class="font-semibold">Delete</span>
						</Button>
					</Dialog.Close>
					<Dialog.Close>
						<Button
							variant="outline"
							class="flex gap-1 text-[#126A99] hover:text-[#126A99] hover:bg-[#126A99]/20 border-[#126A99] border-2"
							onclick={() => {
								isOpen = false;
								console.log(isOpen);
							}}
						>
							<Icon icon={icons.archive} class="w-6 h-6 font-bold" />
							<span class="font-semibold">Archive</span>
						</Button>
					</Dialog.Close>
				</div>
			</Dialog.Content>
		</Dialog.Root>

		<Form.Button
			variant="outline"
			class="bg-[#99D8FA] hover:bg-[#6f9efc] border-[2px] border-[#126A99] text-crinkles text-lg gap-1"
		>
			<Icon icon={icons.save} class="w-6 h-6" />
			<span>Save</span>
		</Form.Button>
	</div>
</form>
