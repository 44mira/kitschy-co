<script lang="ts">
	import { items } from './mockData';
	import { fly } from 'svelte/transition';
	import { backInOut } from 'svelte/easing';

	let currentIndex = $state(0); // Start from the first slide
	let direction = $state(1);

	function setIndex(new_idx: number) {
		direction = new_idx > currentIndex ? 1 : -1;
		currentIndex = new_idx;
	}

	function move(count: 1 | -1) {
		direction = count;
		currentIndex = (currentIndex + count) % 3;
		if (currentIndex < 0) currentIndex = 2; // loop back
	}
</script>

<div class="carousel-container">
	<div class="flex w-full h-full">
		<div class="h-full min-w-full">
			{#key currentIndex}
				<div
					class="absolute h-full w-full bg-contain bg-center bg-no-repeat"
					style:background-image="url({items[currentIndex].image})"
					out:fly={{ x: -1000 * direction, duration: 500, easing: backInOut }}
					in:fly={{ x: 1000 * direction, delay: 100, duration: 500, easing: backInOut }}
				></div>
			{/key}
		</div>
		<div class="carousel-overlay"></div>
	</div>

	<!-- Navigation Controls -->
	<button onclick={() => move(-1)} class="carousel-nav left-3">&lt;</button>
	<button onclick={() => move(1)} class="carousel-nav right-3">&gt;</button>

	<!-- Dots Indicator -->
	<div class="dots-container">
		{#each items as _, index}
			<button
				class="dot"
				class:active={currentIndex == index}
				onclick={() => setIndex(index)}
				aria-label="dot"
			></button>
		{/each}
	</div>
</div>

<style>
	.carousel-container {
		position: relative;
		width: 100%;
		height: 50vh; /* Adjust based on your design */
		max-width: 100%;
		margin: 0 auto;
		overflow: hidden;
	}

	.carousel-overlay {
		position: absolute;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		background-color: rgba(77, 16, 120, 0.4); /* Overlay color */
		z-index: 1;
	}

	.carousel-nav {
		position: absolute;
		top: 50%;
		transform: translateY(-50%);
		background-color: rgba(0, 0, 0, 0.5);
		color: white;
		border: none;
		padding: 10px;
		cursor: pointer;
		font-size: 24px;
		border-radius: 50%;
		z-index: 10;
	}

	.carousel-nav:hover {
		background-color: rgba(0, 0, 0, 0.8);
	}

	.dots-container {
		display: flex;
		justify-content: center;
		gap: 10px;
		padding: 10px;
		position: absolute;
		bottom: 10px;
		width: 100%;
		z-index: 10;
	}

	.dot {
		width: 12px;
		height: 12px;
		border-radius: 50%;
		background-color: rgba(249, 248, 113, 0.5);
		border: none;
		cursor: pointer;
		transition: background-color 0.3s ease;
	}

	.dot.active {
		background-color: #f9f871;
	}

	.dot:hover {
		background-color: rgba(249, 248, 113, 0.8);
	}

	/* Media Query for smaller screens */
	@media (max-width: 768px) {
		.carousel-container {
			height: 31vh; /* Adjust the height for smaller screens */
		}
	}
</style>
