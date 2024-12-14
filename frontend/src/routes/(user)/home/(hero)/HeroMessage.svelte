<script lang="ts">
	const { src, secondary } = $props();
</script>

<div class="flex flex-col grow-0 basis-[30%]" style="--outline: black">
	<div class="font-allura text-7xl">
		where <span class="outlined text-5xl font-gasoekOne" style:color={secondary}>charm</span>
		meets
		<span class="outlined text-5xl font-gasoekOne" style:color={secondary}>convenience</span>
	</div>
	<div class="flex items-center">
		<img class="head--tilt" style:scale="0.40" {src} alt="girl tilting her head" />
		<p class="-mx-10 font-galdeano">Since 2019, kitschy co. has been slaying!</p>
	</div>
</div>

<style>
	.outlined {
		-webkit-text-stroke: 1px var(--outline);
		paint-order: stroke fill;
	}
</style>
