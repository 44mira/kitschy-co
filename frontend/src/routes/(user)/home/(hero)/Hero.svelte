<script lang="ts">
	import redStamp from '$lib/assets/users/redStamp.png';
	import greenStamp from '$lib/assets/users/greenStamp.png';
	import blueStamp from '$lib/assets/users/blueStamp.png';
	import redGirl from '$lib/assets/users/pink_girl.png';
	import greenGirl from '$lib/assets/users/green_girl.png';
	import blueGirl from '$lib/assets/users/blue_girl.png';
	import redFlower from '$lib/assets/users/pink_flower.png';
	import greenButterfly from '$lib/assets/users/green_butterfly.png';
	import blueStar from '$lib/assets/users/blue_star.png';

	import { fade } from 'svelte/transition';
	import hs from './state.svelte.ts';

	import CallCard from './CallCard.svelte';
	import HeroMessage from './HeroMessage.svelte';
	import CallToAction from './CallToAction.svelte';

	const girlSequence = [greenGirl, redGirl, blueGirl];

	const theme = [
		{
			bgStart: '#5EB5E3',
			bgEnd: '#1383BE',
			secondary: '#EF216D',
			stamp: blueStamp,
			icon: blueStar
		},
		{
			bgStart: '#B0D253',
			bgEnd: '#8BAF28',
			secondary: '#5EB5E3',
			stamp: greenStamp,
			icon: greenButterfly
		},
		{
			bgStart: '#F2508B',
			bgEnd: '#AB0A45',
			secondary: '#B0D253',
			stamp: redStamp,
			icon: redFlower
		}
	];

	const nextTheme = () => (hs.currentTheme = ++hs.currentTheme % theme.length);
	const radius = 75;

	let ct = $derived(theme[hs.currentTheme]);
</script>

<svg height="0" width="100%">
	<defs>
		<clipPath id="heroMask">
			<rect x="0" y="-50" width="100%" height="650" rx="50" ry="50"></rect>
			<circle cx="50%" cy="600" r={radius}></circle>
		</clipPath>
	</defs>
</svg>

<div class="relative h-[700px] min-w-full">
	<div
		class="absolute min-h-full min-w-full text-white text-2xl"
		transition:fade={{ duration: 200 }}
		style:clip-path="url(#heroMask)"
	>
		<!-- background needs to be destroyed per change as you cant transition between background-images -->
		{#key hs.currentTheme}
			<div
				class="absolute min-h-full min-w-full z-[-1]"
				transition:fade={{ duration: 250 }}
				style:background-image="linear-gradient({ct.bgStart}, {ct.bgEnd})"
			></div>
		{/key}

		<!-- hero text content -->
		<div class="flex p-28 justify-between">
			<HeroMessage src={girlSequence[hs.currentTheme]} secondary={ct.secondary} />
			<CallToAction src={girlSequence[(hs.currentTheme + 1) % 3]} secondary={ct.secondary} />
		</div>

		<!-- cards -->
		{#each theme as { bgStart, icon }, index}
			<div
				class="callcard absolute bottom-0"
				style:left="40%"
				class:card__left={index == (hs.currentTheme + 2) % 3}
				class:card__middle={index == hs.currentTheme}
				class:card__right={index == (hs.currentTheme + 1) % 3}
			>
				<CallCard primary={bgStart} {icon} theme={index} />
			</div>
		{/each}
	</div>

	<!-- spinning stamp -->
	<div class="absolute flex justify-center w-full bottom-10">
		<button class="w-fit" onclick={nextTheme}>
			<img class="stamp--rotate mx-auto" src={ct.stamp} alt="stamp" />
		</button>
	</div>
</div>

<style>
	:global(.head--tilt) {
		animation: 0.75s tilt linear infinite alternate;
	}

	:global(.head--tilt2) {
		animation: 0.75s tilt linear infinite alternate-reverse;
	}

	.callcard {
		transition: transform 0.5s cubic-bezier(0.68, -0.6, 0.32, 1.6);
	}

	.card__left {
		transform: rotate(-16deg) translate(-10em, 2.5em);
		z-index: 1;
	}

	.card__middle {
		transform: translate(0em, -0.5em);
		z-index: 2;
	}

	.card__right {
		transform: rotate(16deg) translate(10em, 2.5em);
		z-index: 3;
	}

	.stamp--rotate {
		animation: 30s rotate linear infinite;
	}

	@keyframes tilt {
		from {
			transform: rotate(-15deg);
		}
		to {
			transform: rotate(15deg);
		}
	}

	@keyframes rotate {
		to {
			transform: rotate(360deg);
		}
	}
</style>
