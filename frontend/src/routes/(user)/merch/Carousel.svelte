<script lang="ts">
	import { items } from './mockData';

	let currentIndex = $state(0); // Start from the first slide

	function move(count: number) {
		currentIndex = (currentIndex + count) % 3;
		if (currentIndex < 0) currentIndex = 2; // loop back
	}
</script>

<div class="carousel-container">
	<div class="carousel-wrapper" style="transform: translateX(-{currentIndex * 100}%);">
		{#each items as { image, alt }}
			<div class="carousel-slide">
				<!-- Background Image -->
				<div class="carousel-image" style="background-image: url({image});" aria-label={alt}></div>
				<!-- Overlay -->
				<div class="carousel-overlay"></div>
			</div>
		{/each}
	</div>

	<!-- Navigation Controls -->
	<button onclick={() => move(-1)} class="carousel-nav prev">&lt;</button>
	<button onclick={() => move(1)} class="carousel-nav next">&gt;</button>

	<!-- Dots Indicator -->
	<div class="dots-container">
		{#each items as _, index}
			<button
				class="dot"
				class:active={currentIndex == index}
				onclick={() => (currentIndex = index)}
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

	.carousel-wrapper {
		display: flex;
		width: 100%;
		height: 100%;
		transition: transform 0.5s ease-in-out;
	}

	.carousel-slide {
		position: relative;
		min-width: 100%;
		height: 100%;
	}

	.carousel-image {
		width: 100%;
		height: 100%;
		background-size: contain; /* Ensures the image fits within container */
		background-position: center;
		background-repeat: no-repeat;
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

	.prev {
		left: 10px;
	}

	.next {
		right: 10px;
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
