<script lang="ts">
	import banner from '$lib/assets/users/carousel_banner.png';
	export let items = [
		{
			image: banner,
			alt: "Banner 1"
		},
		{
			image: banner,
			alt: "Banner 2"
		},
		{
			image: banner,
			alt: "Banner 3"
		}
	];

	let currentIndex = 0; // Start from the first slide

	// Adjust index to reflect the "virtual" position
	const adjustIndex = () => {
		if (currentIndex < 0) {
			// If at the first slide, jump to the last slide
			currentIndex = items.length - 1;
		} else if (currentIndex >= items.length) {
			// If at the last slide, jump to the first slide
			currentIndex = 0;
		}
	};

	// Move to the next slide
	const nextSlide = () => {
		currentIndex++;
		adjustIndex(); // Ensure the index is adjusted for looping
	};

	// Move to the previous slide
	const prevSlide = () => {
		currentIndex--;
		adjustIndex(); // Ensure the index is adjusted for looping
	};

	// Jump to a specific slide (dot navigation)
	const goToSlide = (index: number) => {
		currentIndex = index;
	};
</script>

<div class="carousel-container">
	<div
		class="carousel-wrapper"
		style="transform: translateX(-{currentIndex * 100}%);"
	>
		{#each items as { image, alt }}
			<div class="carousel-slide">
				<!-- Background Image -->
				<div
					class="carousel-image"
					style="background-image: url({image});"
					aria-label={alt}
				></div>
				<!-- Overlay -->
				<div class="carousel-overlay"></div>
			</div>
		{/each}
	</div>

	<!-- Navigation Controls -->
	<button on:click={prevSlide} class="carousel-nav prev">&lt;</button>
	<button on:click={nextSlide} class="carousel-nav next">&gt;</button>

	<!-- Dots Indicator -->
	<div class="dots-container">
		{#each items as _, index}
			<!-- svelte-ignore a11y_consider_explicit_label -->
			<button
				class="dot {currentIndex === index ? 'active' : ''}"
				on:click={() => goToSlide(index)}
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
