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

	let { form: formData } = form;

	if (values) {
		formData.set(values);
	}

	let isHoveringMainImage = $state(false);

	let categoryValue = $derived($formData.category);
	const triggerCategory = $derived(
		categories.find((c) => c.value == categoryValue)?.label ?? 'Select Category'
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
		/>
	</Form.Control>
</Form.Field>

<div class="flex gap-4">
	<div id="left">
		<Form.Field {form} name="images">
			<Form.Control let:attrs>
				<Form.Label for="images-input">
					<div
						class={`${isHoveringMainImage ? 'hiddenl' : ''} w-[250px] h-[250px] transition ease-in bg-brand-purple-l hover:bg-[#F8EEFF] rounded-xl flex items-center justify-center`}
						role="button"
						tabindex="0"
						onmouseenter={() => (isHoveringMainImage = true)}
						onmouseleave={() => (isHoveringMainImage = false)}
					>
						{#if values && values.images && values.images.length > 0}
							{#each values.images as image}
								<img
									src={image.img_url}
									alt={image.alt_desc}
									class="w-[250px] h-[250px] rounded-xl"
								/>
							{/each}
						{:else}
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
						{/if}
					</div>
				</Form.Label>
				<input id="images-input" type="file" multiple class="w-0 h-0 p-0" accept="image/*" />
			</Form.Control>
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
						style={`background-color: ${categories.find((c) => c.value == categoryValue)?.color}; 
                      color: ${darkTextCategories.includes(categoryValue) ? '#000' : '#fff'}`}
					>
						{triggerCategory}
					</DropdownMenu.Trigger>
					<DropdownMenu.Content>
						<DropdownMenu.RadioGroup bind:value={$formData.category}>
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
						placeholder="0.00"
						class="bg-transparent border-none text-md p-0"
						bind:value={$formData.price}
					/>
				</div>
			</Form.Control>
		</Form.Field>

		<Form.Field {form} name="description" class="space-y-0">
			<Form.Control>
				<Form.Label class="text-brand-purple-d text-lg font-normal">Description:</Form.Label>
				<Textarea
					placeholder="Add a description to give users more context on the product. Be detailed and thorough. Possible important information: units, dimensions, material."
					class="bg-transparent border-none resize-none h-[150px]"
					bind:value={$formData.desc}
				/>
			</Form.Control>
		</Form.Field>
	</div>
</div>
