<script lang="ts">
	import type { ProductSchema } from '@/api/schema';
	import { creators, categories, icons, darkTextCategories } from './admin.ts';
	import * as Form from '$lib/components/ui/form';
	import * as DropdownMenu from '$lib/components/ui/dropdown-menu';
	import { Textarea } from '$lib/components/ui/textarea';
	import Icon from '@iconify/svelte';
	import dndIcon from '$lib/assets/admin/icons/dndIcon.svg';

	type Props = {
		form: any;
		values?: ProductSchema;
	};
	let { form, values }: Props = $props();

	let isHoveringMainImage = $state(false);

	let categoryValue = $state(values ? categories[values.category].value : '');
	const triggerCategory = $derived(
		categories.find((c) => c.value === categoryValue)?.label ?? 'Select Category'
	);

	// uuids of the creators
	let creatorsValue = $state(values ? values.creators : []) as string[];

	/**
	 * Adds a creator to the creatorsValue list if it's not there yet, otherwise remove
	 * @param uuid uuid of the creator
	 */
	function toggleCreator(uuid: string) {
		if (creatorsValue.includes(uuid)) {
			// remove from list
			let popped_creator = creatorsValue.indexOf(uuid);
			creatorsValue.splice(popped_creator, 1);
		} else {
			// add to list
			creatorsValue.push(uuid);
		}
	}
</script>

<Form.Field {form} name="category">
	<Form.Control>
		<input
			type="text"
			placeholder="Product Name"
			class="p-0 bg-transparent border-none text-2xl font-semibold"
			value={values ? values.name : ''}
		/>
	</Form.Control>
	<Form.FieldErrors />
</Form.Field>

<div class="flex gap-4">
	<div id="left">
		<Form.Field {form} name="productImages">
			<Form.Control>
				<Form.Label for="images-input">
					<div
						class={`${isHoveringMainImage ? 'hiddenl' : ''} w-[250px] h-[250px] transition ease-in bg-brand-purple-l hover:bg-[#F8EEFF] rounded-xl flex items-center justify-center`}
						role="button"
						tabindex="0"
						onmouseenter={() => (isHoveringMainImage = true)}
						onmouseleave={() => (isHoveringMainImage = false)}
					>
						<Icon
							icon={icons.add}
							class={`${isHoveringMainImage ? 'hidden' : ''} opacity-100 transition-opacity ease-in hover:opacity-0 w-[250px] h-[250px] text-brand-purple-d`}
						/>
						<div
							class={`${isHoveringMainImage ? '' : 'hidden'} opacity-0 transition-opacity ease-in hover:opacity-100 flex flex-col items-center justify-center w-full h-full border-[5px] hover:border-brand-purple-d border-brand-purple-l rounded-2xl`}
						>
							<img src={dndIcon} alt="Drag and drop icon" class="w-[123px] h-[110px]" />
							<p class="text-brand-purple-d text-center pt-2 text-xl font-giphurs font-semibold">
								Drag and drop or click here
							</p>
						</div>
					</div>
				</Form.Label>
				<input id="images-input" type="file" multiple class="w-0 h-0 p-0" accept="image/*" />
			</Form.Control>
			<Form.FieldErrors />
		</Form.Field>

		<Form.Field {form} name="quantity" class="flex items-center">
			<Form.Control>
				<Form.Label class="text-brand-purple-d text-lg font-normal mt-2">In Stock:</Form.Label>
				<input
					type="number"
					placeholder="0"
					class="bg-transparent border-none text-lg w-40"
					value={values ? values.quantity : ''}
				/>
			</Form.Control>
		</Form.Field>
	</div>

	<div id="right" class="flex-grow">
		<Form.Field {form} name="category" class="grid grid-cols-9 items-center gap-2">
			<Form.Control>
				<Form.Label class="col-span-2 text-brand-purple-d text-lg font-normal">Category:</Form.Label
				>
				<DropdownMenu.Root>
					<DropdownMenu.Trigger
						class="bg-slate-600 col-span-7 w-fit px-3 py-[2px] rounded-full text-brand-base"
						style={`background-color: ${categories.find((c) => c.value === categoryValue)?.color}; 
                      color: ${darkTextCategories.includes(categoryValue) ? '#000' : '#fff'}`}
						>{triggerCategory}</DropdownMenu.Trigger
					>
					<DropdownMenu.Content>
						<DropdownMenu.RadioGroup bind:value={categoryValue}>
							{#each categories as c}
								<DropdownMenu.RadioItem value={c.value}>{c.label}</DropdownMenu.RadioItem>
							{/each}
						</DropdownMenu.RadioGroup>
					</DropdownMenu.Content>
				</DropdownMenu.Root>
			</Form.Control>
			<Form.FieldErrors />
		</Form.Field>

		<Form.Field {form} name="creators" class="grid grid-cols-9 items-center gap-2">
			<Form.Control>
				<Form.Label class="col-span-2 text-brand-purple-d text-lg font-normal"
					>Creator/s:</Form.Label
				>
				<DropdownMenu.Root>
					<DropdownMenu.Trigger>
						<Icon
							icon={icons.add}
							class="w-6 h-6 text-brand-purple-d bg-brand-purple-l rounded-full"
						/>
					</DropdownMenu.Trigger>
					<DropdownMenu.Content class="">
						<DropdownMenu.Group>
							{#each creators as creator}
								<DropdownMenu.CheckboxItem
									checked={creatorsValue.includes(creator.uuid)}
									onCheckedChange={() => toggleCreator(creator.uuid)}
									>{creator.name}</DropdownMenu.CheckboxItem
								>
							{/each}
						</DropdownMenu.Group>
					</DropdownMenu.Content>
				</DropdownMenu.Root>

				<div class="flex gap-2">
					{#each creatorsValue as creator}
						<div
							class="text-brand-base text-sm px-3 py-1 rounded-full flex items-center"
							style={`background-color: ${creators.find((c) => c.uuid === creator)?.color}`}
						>
							<span>{creators.find((c) => c.uuid === creator)?.name}</span>
							<Icon
								icon={icons.close}
								class="w-4 h-4 ml-1 hover:text-brand-purple"
								onclick={() => toggleCreator(creator)}
							/>
						</div>
					{/each}
				</div>
			</Form.Control>
			<Form.FieldErrors />
		</Form.Field>

		<Form.Field {form} name="price" class="grid grid-cols-9 items-center gap-2">
			<Form.Control>
				<Form.Label class="text-brand-purple-d text-lg font-normal col-span-2 mt-2"
					>Price:</Form.Label
				>
				<div class="col-span-7 flex items-center">
					<span>₱</span>
					<input
						type="text"
						placeholder="0.00"
						class="bg-transparent border-none text-md p-0"
						value={values ? values.price : ''}
					/>
				</div>
			</Form.Control>
			<Form.FieldErrors />
		</Form.Field>

		<Form.Field {form} name="description" class="space-y-0">
			<Form.Control>
				<Form.Label class="text-brand-purple-d text-lg font-normal">Description:</Form.Label>
				<Textarea
					placeholder="Add a description to give users more context on the product. Be detailed and thorough. Possible important information: units, dimensions, material."
					class="bg-transparent border-none resize-none h-[150px]"
					value={values ? values.desc : ''}
				/>
			</Form.Control>
			<Form.FieldErrors />
		</Form.Field>
	</div>
</div>
