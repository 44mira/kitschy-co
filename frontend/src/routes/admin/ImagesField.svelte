<script lang="ts">
	import * as Form from '$lib/components/ui/form';
	import dndIcon from '$lib/assets/admin/icons/dndIcon.svg';
	import { icons } from './admin.ts';
	import { filesProxy } from 'sveltekit-superforms';
  import Icon from '@iconify/svelte';

	type Props = {
		form: any;
		preloadedImages?: any;
	};
	let { form, preloadedImages }: Props = $props();
	let isHoveringMainImage = $state(false);

	const images = filesProxy(form, 'images');
</script>

<Form.Field {form} name="images">
	<Form.Control let:attrs>
		<div class="flex flex-col gap-0">
			<div id="big-image">
				<Form.Label for="images-input">
					<div
						class={`${isHoveringMainImage ? 'hiddenl' : ''} w-[250px] h-[250px] transition ease-in bg-brand-purple-l hover:bg-[#F8EEFF] rounded-xl flex items-center justify-center`}
						role="button"
						tabindex="0"
						onmouseenter={() => (isHoveringMainImage = true)}
						onmouseleave={() => (isHoveringMainImage = false)}
					>
						{#if preloadedImages && preloadedImages.length > 0}
							{#each preloadedImages as image}
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

						{#if $images.length > 0}
							<img
								src={URL.createObjectURL($images[0])}
								alt="Product"
								class="w-[250px] h-[250px] rounded-xl"
							/>
						{/if}
					</div>
				</Form.Label>
				<input
					id="images-input"
					type="file"
					multiple
					class="w-0 h-0 p-0"
					accept="image/*"
					bind:files={$images}
				/>
			</div>
			{#if $images.length > 1}
				<div id="small-images">
					{#each $images as image, i}
						{#if i > 0}
							<img
								src={URL.createObjectURL(image)}
								alt="Product"
								class="w-[75px] h-[75px] rounded-xl bg-brand-purple-l p-2"
							/>
						{/if}
					{/each}
				</div>
			{/if}
		</div>
	</Form.Control>
</Form.Field>
