<script lang="ts">
	import { type ProductSchema } from '@/api/schema';
	import { elasticOut } from 'svelte/easing';

	type MerchandiseItemProps = {
		product: ProductSchema;
		tilt: string;
		isFalling: boolean;
		children?: import('svelte').Snippet;
	};

	// convert a math function into a linear() curve
	const createEase = (fn: (x: number) => number, points = 100) => {
		// generate points the curve follows
		const result = [...new Array(points)]
			.map((_, i) => {
				const x = i * (1 / points);
				return fn(x);
			})
			.join(',');

		return `linear(${result})`;
	};

	const { product, tilt, isFalling }: MerchandiseItemProps = $props();
	const thumbnail = product.images[0];
</script>

<div
	class="relative flex flex-col polaroid min-h-[250px] min-w-full p-3 drop-shadow-lg bg-gradient-to-t from-[#eeeeff] to-[#ffffff]"
	style="--tilt:{tilt}"
	style:transition-timing-function={createEase(elasticOut)}
	class:polaroid--down={isFalling}
>
	<!-- pin -->
	<div class="absolute h-5 w-5 -top-3 inset-x-0 mx-auto pin rounded-3xl"></div>

	<!-- image -->
	<div class="polaroid__image grow min-w-full">
		<img src={thumbnail.img_url} alt={thumbnail.alt_desc} class="min-h-full min-w-full" />
	</div>

	<!-- description -->
	<div class="pt-2 basis-12 bg-transparent font-bold text-2xl flex flex-col">
		<span class="font-giphursSC h-20">
			{product.name}
		</span>
		<span class="self-end font-giphurs text-brand-purple-d">
			₱{product.price}
		</span>
	</div>
</div>

<style>
	.pin {
		box-shadow: 0px 0px 2px 1px rgba(0, 0, 0, 0.3) inset;
		background-image: radial-gradient(#faea9d, #f2b63f);
	}

	.polaroid {
		transform-origin: top;
		transform: rotate(var(--tilt));

		transition-duration: 5s;
		transition-property: transform;

		border: 1px solid rgba(0, 0, 0, 0.5);
	}

	.polaroid__image {
		border: 1px solid black;
	}

	.polaroid--down {
		transform: none;
	}
</style>
