<script lang="ts">
	import redStamp from '$lib/assets/users/redStamp.png';
	import greenStamp from '$lib/assets/users/greenStamp.png';
	import blueStamp from '$lib/assets/users/blueStamp.png';
	import redGirl from '$lib/assets/users/pink_girl.png';
	import greenGirl from '$lib/assets/users/green_girl.png';
	import blueGirl from '$lib/assets/users/blue_girl.png';
	import { fade } from 'svelte/transition';

	import type { PageData } from '../$types';
	import SignupDialog from './SignupDialog.svelte';

	let { data }: { data: PageData } = $props();

	const girlSequence = [greenGirl, redGirl, blueGirl];

	const theme = [
		{ bgStart: '#5EB5E3', bgEnd: '#1383BE', primary: '#EF216D', stamp: blueStamp },
		{ bgStart: '#B0D253', bgEnd: '#8BAF28', primary: '#5EB5E3', stamp: greenStamp },
		{ bgStart: '#F2508B', bgEnd: '#AB0A45', primary: '#B0D253', stamp: redStamp }
	];

	const nextTheme = () => (currentTheme = ++currentTheme % theme.length);
	const radius = 75;

	let currentTheme = $state(0);
	let ct = $derived(theme[currentTheme]);
</script>

<svg height="0" width="100%">
	<defs>
		<clipPath id="heroMask">
			<rect x="0" y="-50" width="100%" height="600" rx="50" ry="50"></rect>
			<circle cx="50%" cy="550" r={radius}></circle>
		</clipPath>
	</defs>
</svg>

<div class="relative h-[650px] min-w-full">
	{#key currentTheme}
		<div
			class="absolute min-h-full min-w-full text-white text-2xl"
			transition:fade={{ duration: 200 }}
			style:background-image="linear-gradient({ct.bgStart} 50%, {ct.bgEnd})"
			style:clip-path="url(#heroMask)"
		>
			<div class="flex p-28 justify-between">
				<div class="flex flex-col grow-0 basis-[30%]">
					<div class="font-allura text-7xl">
						where <span class="outlined text-5xl font-gasoekOne" style:color={ct.primary}
							>charm</span
						>
						meets
						<span class="outlined text-5xl font-gasoekOne" style:color={ct.primary}
							>convenience</span
						>
					</div>
					<div class="flex items-center">
						<img
							class="head--tilt"
							style:scale="0.40"
							src={girlSequence[currentTheme]}
							alt="girl tilting her head"
						/>
						<p class="-mx-10 font-galdeano">Since 2019, kitschy co. has been slaying!</p>
					</div>
				</div>

				<div class="grow-0 basis-[30%]">
					<p class="mb-5 font-galdeano">
						At kitschy co. ✨, our goal is to create a unique experience 🌟 and a welcoming
						environment 🏡 that will entice our customers' to return time and time again 💫.
					</p>
					<div class="flex h-52">
						<img
							style:scale="0.40"
							class="head--tilt2"
							src={girlSequence[(currentTheme + 1) % 3]}
							alt="girl tilting her head"
						/>
						<SignupDialog data={data.signupForm} primary={ct.primary} />
					</div>
				</div>
			</div>
		</div>
	{/key}
	<button class="absolute min-w-full self-end bottom-10 inset-x-0" onclick={nextTheme}>
		<img class="stamp--rotate mx-auto" src={ct.stamp} alt="stamp" />
	</button>
</div>

<style>
	.outlined {
		-webkit-text-stroke: 2px white;
		paint-order: stroke fill;
	}

	.head--tilt {
		animation: 0.75s tilt linear infinite alternate;
	}

	.head--tilt2 {
		animation: 0.75s tilt linear infinite alternate-reverse;
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
