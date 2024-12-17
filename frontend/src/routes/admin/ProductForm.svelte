<script lang="ts">
	import type { ProductSchema } from '@/api/schema';
	import { creators, categories, icons, darkTextCategories } from './admin.ts';
	import * as Form from '$lib/components/ui/form';
	import * as DropdownMenu from '$lib/components/ui/dropdown-menu';
	import { Textarea } from '$lib/components/ui/textarea';
	import Icon from '@iconify/svelte';
	import ImagesField from './ImagesField.svelte';

	type Props = {
		form: any;
		values?: ProductSchema;
	};
	let { form, values }: Props = $props();

	let { form: formData, constraints } = form;

	if (values) {
		formData.set(values);
	}

	const triggerCategory = $derived(
		categories.find((c) => c.value == $formData.category)?.label ?? 'Select Category'
	);

	let checkedCreators = $state(creators.map((c) => false));
	if (values) {
		checkedCreators = creators.map((c) => values.creators.includes(c.uuid));
	}

	$effect(() => {
		$formData.creators = creators.filter((c, i) => checkedCreators[i]).map((c) => c.uuid);
	});
</script>

<Form.Field {form} name="name">
	<Form.Control let:attrs>
		<input
			{...attrs}
			placeholder="Product Name"
			class="p-0 bg-transparent border-none text-2xl font-semibold"
			bind:value={$formData.name}
			{...$constraints.name}
		/>
	</Form.Control>
</Form.Field>

<div class="flex gap-4">
	<div id="left">
		<ImagesField {form} preloadedImages={values ? values.images : undefined} />

		<Form.Field {form} name="quantity" class="flex items-center">
			<Form.Control let:attrs>
				<Form.Label class="text-brand-purple-d text-lg font-normal mt-2">In Stock:</Form.Label>
				<input
          {...attrs}
					type="number"
					placeholder="0"
					class="remove-arrow bg-transparent border-none text-lg w-40"
					bind:value={$formData.quantity}
					{...$constraints.quantity}
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
						style={`background-color: ${categories.find((c) => c.value == $formData.category)?.color}; 
                      color: ${darkTextCategories.includes($formData.category) ? '#000' : '#fff'}`}
					>
						{triggerCategory}
					</DropdownMenu.Trigger>
					<DropdownMenu.Content>
						<DropdownMenu.RadioGroup
							onValueChange={(v) => ($formData.category = v ? Number(v) : 0)}
							value={$formData.category}
							{...$constraints.category}
						>
							{#each categories as c}
								<DropdownMenu.RadioItem value={c.value}>{c.label}</DropdownMenu.RadioItem>
							{/each}
						</DropdownMenu.RadioGroup>
					</DropdownMenu.Content>
				</DropdownMenu.Root>
			</Form.Control>
		</Form.Field>

		<Form.Field {form} name="creators" class="grid grid-cols-9 items-center gap-2">
			<Form.Control let:attrs>
				<Form.Label class="col-span-2 text-brand-purple-d text-lg font-normal">
					Creator/s:
				</Form.Label>

				<DropdownMenu.Root>
					<DropdownMenu.Trigger>
						<Icon
							icon={icons.add}
							class="w-6 h-6 text-brand-purple-d bg-brand-purple-l rounded-full"
						/>
					</DropdownMenu.Trigger>
					<DropdownMenu.Content class="">
						<DropdownMenu.Group>
							{#each creators as creator, i}
								<DropdownMenu.CheckboxItem bind:checked={checkedCreators[i]}
									>{creator.name}</DropdownMenu.CheckboxItem
								>
							{/each}
						</DropdownMenu.Group>
					</DropdownMenu.Content>
				</DropdownMenu.Root>

				<div class="flex gap-2">
					{#each checkedCreators as checked, i}
						{#if checked}
							<div
								class="text-brand-base text-sm px-3 py-1 rounded-full flex items-center"
								style={`background-color: ${creators[i].color}`}
							>
								<span>{creators[i].name}</span>
								<Icon
									icon={icons.close}
									class="w-4 h-4 ml-1 hover:text-brand-purple"
									onclick={() => (checkedCreators[i] = false)}
								/>
							</div>
						{/if}
					{/each}
				</div>
			</Form.Control>
		</Form.Field>

		<Form.Field {form} name="price" class="grid grid-cols-9 items-center gap-2">
			<Form.Control let:attrs>
				<Form.Label class="text-brand-purple-d text-lg font-normal col-span-2 mt-2"
					>Price:</Form.Label
				>
				<div class="col-span-7 flex items-center">
					<span>₱</span>
					<input
						{...attrs}
						type="number"
						step=".01"
						placeholder="0.00"
						class="remove-arrow bg-transparent border-none text-md p-0"
						bind:value={$formData.price}
						{...$constraints.price}
					/>
				</div>
			</Form.Control>
		</Form.Field>

		<Form.Field {form} name="desc" class="space-y-0">
			<Form.Control let:attrs>
				<Form.Label class="text-brand-purple-d text-lg font-normal">Description:</Form.Label>
				<Textarea
					{...attrs}
					placeholder="Add a description to give users more context on the product. Be detailed and thorough. Possible important information: units, dimensions, material."
					class="bg-transparent border-none resize-none h-[150px]"
					bind:value={$formData.desc}
				/>
			</Form.Control>
			<Form.FieldErrors />
		</Form.Field>
	</div>
</div>

<style>
	.remove-arrow::-webkit-inner-spin-button,
	.remove-arrow::-webkit-outer-spin-button {
		-webkit-appearance: none;
		margin: 0;
	}
	.remove-arrow {
		-moz-appearance: textfield;
	}
</style>
