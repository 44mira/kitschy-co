<script lang="ts">
	import heartbg from '$lib/assets/users/heartbg.png';
</script>

<div
	class="z-0 relative flex flex-col items-center justify-center min-w-screen min-h-screen overflow-clip"
>
	<div
		class="absolute inset-0 h-svh w-svh outer bg-cover"
		style="background-image: url({heartbg})"
	></div>

	<div class="z-10 flex flex-col gap-6 items-center text-brand-base">
		<span class="text-brand-yellow text-7xl font-lockergnome outlined">Oops!</span>
		<div class="font-giphurs text-4xl outlined flex flex-col items-center gap-3">
			<span>Looks like you found a service</span>
			<span>that is <span class="font-giphursSC font-bold">coming soon!</span></span>
		</div>
	</div>
</div>

<style>
	.outlined {
		-webkit-text-stroke: 10px #804b7a;
		paint-order: stroke fill;
	}

	.outer {
		z-index: -1;
		scale: 1.5;
		background-position-y: 50%;
		animation: 15s zoom linear infinite alternate;
	}

	@keyframes zoom {
		to {
			transform: scale(3);
			transform-origin: center;
		}
	}
</style>
