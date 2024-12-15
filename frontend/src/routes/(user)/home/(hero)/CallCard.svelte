<script lang="ts">
	import hs from './state.svelte.ts';
  
	let { primary, icon: src, theme } = $props();
  </script>
  
  <div class="callcard p-4 shadow shadow-black mx-auto">
	<button class="h-full w-full" onclick={() => (hs.currentTheme = theme)}>
	  <div
		class="card-content h-full w-full border-[3px] rounded-xl flex items-center justify-center"
		style:border-color={primary}
	  >
		<img {src} alt="card icon" class="card-icon" />
	  </div>
	</button>
  </div>
  
  <style>
	.callcard {
	  background-color: rgba(230, 230, 255, 0.95);
	  border-radius: 1.5em;
	  width: 100%; /* Set the width as a percentage of the container */
	  max-width: 335px; /* Ensure it doesn't exceed the max width on larger screens */
	  aspect-ratio: 2 / 3; /* Maintain a 2:3 aspect ratio for the card */
	  margin: auto;
	  padding: 1rem; /* Add some internal space */
	  box-sizing: border-box;
	}
  
	.card-content {
	  height: 100%;
	  width: 100%;
	  display: flex;
	  justify-content: center;
	  align-items: center;
	  border-radius: inherit;
	  overflow: hidden;
	}
  
	.card-icon {
	  width: 100%; /* Set a flexible width for the icon image */
	  height: auto;
	  object-fit: contain; /* Ensure the image maintains its aspect ratio */
	}
  
	/* For smaller screens, adjust card size and icon size */
	@media (max-width: 768px) {
	  .callcard {
		width: 100%; /* Cards take up 85% of the screen on smaller screens */
		max-width: 260px; /* Smaller max-width on mobile */
		padding: 0.8rem; /* Reduce padding for smaller screens */
	  }
  
	  .card-icon {
		width: 100%; /* Slightly bigger icon on smaller screens */
	  }
	}
  
	@media (max-width: 480px) {
	  .callcard {
		width: 80%; /* Cards take up 95% of the screen on very small screens */
		max-width: 250px; /* Even smaller max-width */
		padding: 0.5rem; /* Further reduce padding */
	  }
  
	  .card-icon {
		width: 70%; /* Larger icon size for mobile */
	  }
	}
  
	/* Add a little responsiveness for font sizes in case there's text inside the card */
	@media (max-width: 768px) {
	  .callcard {
		font-size: 0.9rem; /* Adjust font size on smaller screens */
	  }
	}
  
	@media (max-width: 480px) {
	  .callcard {
		font-size: 0.8rem; /* Further reduce font size for very small screens */
	  }
	}
  </style>
  