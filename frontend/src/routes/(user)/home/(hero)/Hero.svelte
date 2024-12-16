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
			<rect x="0" y="-50" width="100%" height="750" rx="50" ry="50"></rect>
			<circle cx="50%" cy="700" r={radius}></circle>
		</clipPath>
	</defs>
</svg>

<div class="relative min-h-[800px] w-full">
	<div class="min-h-full w-full text-white text-2xl" style:clip-path="url(#heroMask)">
		{#key hs.currentTheme}
			<div
				class="absolute min-h-full min-w-full z-[-1]"
				transition:fade={{ duration: 250 }}
				style:background-image="linear-gradient({ct.bgStart}, {ct.bgEnd})"
			></div>
		{/key}

		<!-- Hero text content -->
		<div class="flex flex-col md:flex-row lg:flex-row p-8 md:p-16 lg:p-20 xl:p-28 justify-between">
			<!-- Left div for HeroMessage -->
			<div class="flex-1">
				<HeroMessage src={girlSequence[hs.currentTheme]} secondary={ct.secondary} />
			</div>

			<!-- Right div for CallToAction -->
			<div class="flex-1">
				<CallToAction src={girlSequence[(hs.currentTheme + 1) % 3]} secondary={ct.secondary} />
			</div>
		</div>

		<!-- cards -->
		{#each theme as { bgStart, icon }, index}
			<div
				class="callcard absolute bottom-0 inset-x-0 max-w-fit mx-auto"
				class:card__left={index == (hs.currentTheme + 2) % 3}
				class:card__middle={index == hs.currentTheme}
				class:card__right={index == (hs.currentTheme + 1) % 3}
			>
				<CallCard primary={bgStart} {icon} theme={index} />
			</div>
		{/each}

		<!-- spinning stamp -->
		<button
			class="absolute bottom-12 inset-x-0 mx-auto max-w-fit z-[5] border-2 border-black border-dotted rounded-[99px]"
			onclick={nextTheme}
		>
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

	/* Responsive styles */
	@media (max-width: 768px) {
		.relative {
			height: auto; /* Let the container height adjust based on content */
		}

		.text-2xl {
			font-size: 1.5rem; /* Adjust font size for mobile */
		}

		.flex {
			flex-direction: column; /* Stack hero text vertically on smaller screens */
		}
	}

	@media (max-width: 480px) {
		.flex {
			padding: 4rem 1rem; /* Reduce padding on smaller screens */
		}
	}
</style>
