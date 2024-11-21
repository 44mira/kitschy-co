<script lang="ts">
	import * as Form from '$lib/components/ui/form';
	import * as Dialog from '$lib/components/ui/dialog';
	import * as DropdownMenu from '$lib/components/ui/dropdown-menu';
	import { Input } from '$lib/components/ui/input';
	import { Textarea } from '$lib/components/ui/textarea';
	import { Button } from '@/components/ui/button';
	import { addProductSchema, type AddProductSchema } from './schema';
	import { type SuperValidated, type Infer, superForm } from 'sveltekit-superforms';
	import { zodClient } from 'sveltekit-superforms/adapters';
	import AddIcon from 'virtual:icons/mdi/add';
	import DeleteIcon from 'virtual:icons/mdi/delete-forever-outline';
	import SaveIcon from 'virtual:icons/mdi/content-save-outline';
	import dndIcon from '$lib/assets/admin/icons/dndIcon.svg';
	import { Control } from 'formsnap';

	// export let data: SuperValidated<Infer<AddProductSchema>>;
	let { data } = $props();

	const addProductForm = superForm(data, {
		validators: zodClient(addProductSchema)
	});

	let isHoveredMainImage = $state(false);

	let categories = [
		{ value: 'merch', label: 'Merchandise', color: '#4D1078' },
		{ value: 'cafe', label: 'Cafe & Pastries', color: '#FB7A4F' },
		{ value: 'print', label: "Misbeek's Printing", color: '#ffabff' },
		{ value: 'minimart', label: 'Mini-mart', color: '#F9F871' },
		{ value: 'workshop', label: 'Workshop', color: '#32beaf' }
	];
	let darkTextCategories = ['print', 'minimart'];
	let category = $state('');
	const triggerCategory = $derived(
		categories.find((c) => c.value === category)?.label ?? 'Select Category'
	);
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

					<Form.Field form={addProductForm} name="quantity" class="flex items-center">
						<Form.Control>
							<Form.Label class="text-brand-purple-d text-lg font-normal mt-2">In Stock:</Form.Label
							>
							<Input
								type="number"
								placeholder="0"
								class="bg-transparent border-none text-lg w-40"
							/>
						</Form.Control>
					</Form.Field>
				</div>
				<div id="right" class="flex-grow">
					<Form.Field
						form={addProductForm}
						name="category"
						class="grid grid-cols-9 items-center gap-2"
					>
						<Form.Control>
							<Form.Label class="col-span-2 text-brand-purple-d text-lg font-normal"
								>Category:</Form.Label
							>
							<DropdownMenu.Root>
								<DropdownMenu.Trigger
									class="bg-slate-600 col-span-7 w-fit px-3 py-[2px] rounded-full text-brand-base"
									style={`background-color: ${categories.find((c) => c.value === category)?.color}; 
                          color: ${darkTextCategories.includes(category) ? '#000' : '#fff'}`}
									>{triggerCategory}</DropdownMenu.Trigger
								>
								<DropdownMenu.Content>
									<DropdownMenu.RadioGroup bind:value={category}>
										{#each categories as c}
											<DropdownMenu.RadioItem value={c.value}>{c.label}</DropdownMenu.RadioItem>
										{/each}
									</DropdownMenu.RadioGroup>
								</DropdownMenu.Content>
							</DropdownMenu.Root>
						</Form.Control>
						<Form.FieldErrors />
					</Form.Field>

					<Form.Field
						form={addProductForm}
						name="creators"
						class="grid grid-cols-9 items-center gap-2"
					>
						<Form.Control>
							<Form.Label class="col-span-2 text-brand-purple-d text-lg font-normal"
								>Creator/s:</Form.Label
							>
							<Input type="text" />
						</Form.Control>
						<Form.FieldErrors />
					</Form.Field>
					<Form.Field
						form={addProductForm}
						name="price"
						class="grid grid-cols-9 items-center gap-2"
					>
						<Form.Control>
							<Form.Label class="text-brand-purple-d text-lg font-normal col-span-2"
								>Price:</Form.Label
							>
							<Input
								type="text"
								placeholder="0.00"
								class="bg-transparent border-none text-md col-span-7"
							/>
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
				<Button
					variant="outline"
					class="bg-transparent border-[2px] border-gray-400 text-gray-400 text-lg gap-1 hover:border-text-crinkles"
				>
					<DeleteIcon class="w-6 h-6" />
					<span>Cancel</span></Button
				>
				<Form.Button
					variant="outline"
					class="bg-[#99D8FA] hover:bg-[#6f9efc] border-[2px] border-[#126A99] text-crinkles text-lg gap-1"
				>
					<SaveIcon class="w-6 h-6" />
					<span>Add Item</span></Form.Button
				>
			</div>
		</form>
	</Dialog.Content>
</Dialog.Root>
