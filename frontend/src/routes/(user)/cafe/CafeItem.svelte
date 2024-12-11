<script lang="ts">
	import { type ProductSchema } from '@/api/schema';
	import plate from '$lib/assets/users/plate.png';

	import Button from '@/lib/components/ui/button/button.svelte';

	type ProductSchemaProps = ProductSchema & { children?: import('svelte').Snippet };

	let product: ProductSchemaProps = $props();
</script>

<div class="flex flex-col items-center justify-center min-h-fit min-w-fit">
	<div class="relative z-0">
		<img src={plate} alt="plate backdrop" class="z-0" />
		<!-- product.images[0] goes here at a higher z -->
	</div>

	<div class="bg-white min-w-full min-h-40 max-h-52 p-4 -mt-12 z-[2]">
		<h1 class="item__desc text-2xl font-bold">{product.name}</h1>
		<p class="item__desc text-lg px-1">{product.desc}</p>

		<div class="flex pt-5">
			<Button
				class="text-5xl content-center text-secondary-foreground border-secondary-foreground"
				variant="outline"
				size="icon">+</Button
			>
			<div class="grow"></div>
			<div class="text-brand-orangePastries font-giphurs text-3xl font-bold">P{product.price}</div>
		</div>
	</div>
</div>

<style>
	.item__desc {
		@apply font-giphursSC text-[#762804];
	}
</style>
