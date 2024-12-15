<script lang="ts">
	const { src, secondary } = $props();
</script>

<div
	class="flex flex-col grow-0 basis-[30%] px-4 sm:px-6 lg:px-8 space-y-4 sm:space-y-6"
	style="--outline: black"
>
	<!-- Responsive Header -->
	<div class="font-allura text-5xl sm:text-3xl xl:text-6xl text-center sm:text-center md:text-left">
		where
		<span
			class="outlined text-3xl sm:text-4xl lg:text-5xl font-gasoekOne"
			style:color={secondary}
		>
			charm
		</span>
		meets
		<span
			class="outlined text-3xl sm:text-4xl lg:text-5xl font-gasoekOne"
			style:color={secondary}
		>
			convenience
		</span>
	</div>

	<!-- Image on the Left, Text on the Right -->
	<div class="flex flex-row items-center justify-center md:justify-start">
		<img
			class="head--tilt w-28 sm:w-32 md:w-36 lg:w-40 object-contain"
			style:scale="0.40"
			{src}
			alt="girl tilting her head"
		/>
		<p class="text-base sm:text-lg lg:text-xl text-left font-galdeano">
			Since 2019, kitschy co. has been slaying!
		</p>
	</div>
</div>

<style>
	.outlined {
		-webkit-text-stroke: 1px var(--outline);
		paint-order: stroke fill;
	}
</style>
