<script lang="ts">
	const { src, primary } = $props();
</script>

<div class="flex flex-col grow-0 basis-[30%]">
	<div class="font-allura text-7xl">
		where <span class="outlined text-5xl font-gasoekOne" style:color={primary}>charm</span>
		meets
		<span class="outlined text-5xl font-gasoekOne" style:color={primary}>convenience</span>
	</div>
	<div class="flex items-center">
		<img class="head--tilt" style:scale="0.40" {src} alt="girl tilting her head" />
		<p class="-mx-10 font-galdeano">Since 2019, kitschy co. has been slaying!</p>
	</div>
</div>

<style>
	.outlined {
		-webkit-text-stroke: 2px white;
		paint-order: stroke fill;
	}
</style>
