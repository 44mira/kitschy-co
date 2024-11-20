<script lang="ts">
	import * as Form from '$lib/components/ui/form';
	import * as Dialog from '$lib/components/ui/dialog';
	import { Input } from '$lib/components/ui/input';
	import { Textarea } from '$lib/components/ui/textarea';
	import { Button } from '@/components/ui/button';
	import { addProductSchema, type AddProductSchema } from './schema';
	import { type SuperValidated, type Infer, superForm } from 'sveltekit-superforms';
	import { zodClient } from 'sveltekit-superforms/adapters';
	import AddIcon from 'virtual:icons/mdi/add';
	import dndIcon from '$lib/assets/admin/icons/dndIcon.svg';

	// export let data: SuperValidated<Infer<AddProductSchema>>;
	let { data } = $props();

	const addProductForm = superForm(data, {
		validators: zodClient(addProductSchema)
	});

	let isHoveredMainImage = $state(false);
</script>

<Dialog.Root open="True">
	<Dialog.Trigger
		class="w-[75px] h-[75px] bg-[#094F7B4D] hover:bg-[#094F7B] flex items-center justify-center rounded-3xl z-10"
	>
		<AddIcon class="text-brand-base w-[70px] h-[70px]" />
	</Dialog.Trigger>
	<Dialog.Content class="bg-[#fff5fe] border-none w-[750px]">
		<form method="POST">
			<Form.Field form={addProductForm} name="category">
				<Form.Control>
					<Input
						type="text"
						placeholder="Product Name"
						class="p-0 bg-transparent border-none text-2xl font-semibold"
					/>
				</Form.Control>
				<Form.FieldErrors />
			</Form.Field>
			<div class="flex gap-4">
				<div id="left">
					<Form.Field form={addProductForm} name="productImages">
						<Form.Control>
							<Form.Label for="images-input">
								<div
									class={`${isHoveredMainImage ? 'hiddenl' : ''} w-[250px] h-[250px] transition ease-in bg-brand-purple-l hover:bg-[#F8EEFF] rounded-xl flex items-center justify-center`}
									role="button"
									tabindex="0"
									onmouseenter={() => (isHoveredMainImage = true)}
									onmouseleave={() => (isHoveredMainImage = false)}
								>
									<AddIcon
										class={`${isHoveredMainImage ? 'hidden' : ''} opacity-100 transition-opacity ease-in hover:opacity-0 w-[250px] h-[250px] text-brand-purple-d`}
									/>
									<div
										class={`${isHoveredMainImage ? '' : 'hidden'} opacity-0 transition-opacity ease-in hover:opacity-100 flex flex-col items-center justify-center w-full h-full border-[5px] hover:border-brand-purple-d border-brand-purple-l rounded-2xl`}
									>
										<img src={dndIcon} alt="Drag and drop icon" class="w-[123px] h-[110px]" />
										<p
											class="text-brand-purple-d text-center pt-2 text-xl font-giphurs font-semibold"
										>
											Drag and drop or click here
										</p>
									</div>
								</div>
							</Form.Label>
							<Input id="images-input" type="file" multiple class="w-0 h-0 p-0" accept="image/*" />
						</Form.Control>
						<Form.FieldErrors />
					</Form.Field>
				</div>
				<div id="right" class="flex-grow">
					<Form.Field form={addProductForm} name="category">
						<Form.Control>
							<Form.Label class="text-brand-purple-d text-lg font-normal">Category:</Form.Label>
							<Input type="text" />
						</Form.Control>
						<Form.FieldErrors />
					</Form.Field>

					<Form.Field form={addProductForm} name="creators">
						<Form.Control>
							<Form.Label class="text-brand-purple-d text-lg font-normal">Creator/s:</Form.Label>
							<Input type="text" />
						</Form.Control>
						<Form.FieldErrors />
					</Form.Field>
					<Form.Field form={addProductForm} name="price">
						<Form.Control>
							<Form.Label class="text-brand-purple-d text-lg font-normal">Price:</Form.Label>
							<Input type="text" />
						</Form.Control>
						<Form.FieldErrors />
					</Form.Field>
					<Form.Field form={addProductForm} name="desc" class="space-y-0">
						<Form.Control>
							<Form.Label class="text-brand-purple-d text-lg font-normal">Description:</Form.Label>
							<Textarea
								placeholder="Add a description to give users more context on the product. Be detailed and thorough. Possible important information: units, dimensions, material."
								class="bg-transparent border-none resize-none h-[150px]"
							/>
						</Form.Control>
						<Form.FieldErrors />
					</Form.Field>
				</div>
			</div>
			<div id="actions" class="flex justify-end gap-4">
				<Button>Cancel</Button>
				<Form.Button>Add Item</Form.Button>
			</div>
		</form>
	</Dialog.Content>
</Dialog.Root>
