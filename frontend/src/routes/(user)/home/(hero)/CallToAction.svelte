<script lang="ts">
	import { getContext } from 'svelte';
	import SignupDialog from './SignupDialog.svelte';

	import type { PageData } from '../$types';

	const data: PageData = getContext('data');

	const { src, secondary } = $props();
</script>

<div class="grow-0 basis-full sm:basis-[30%] px-4 sm:px-6 lg:px-8">
	<!-- Responsive Text -->
	<p class="mb-5 font-galdeano text-base sm:text-base lg:text-lg xl:text-xl text-center sm:text-center md:text-left">
		At kitschy co. ✨, our goal is to create a unique experience 🌟 and a welcoming environment 🏡
		that will entice our customers' to return time and time again 💫.
	</p>

	<!-- Responsive Image and Signup Dialog -->
	<div class="flex sm:flex-row items-center justify-center md:justify-start h-auto">
		<img
			class="head--tilt2 w-28 sm:w-32 md:w-36 lg:w-40 object-contain"
			style:scale="0.40"
			{src}
			alt="girl tilting her head"
		/>
		<SignupDialog data={data.signupForm} primary={secondary} />
	</div>
</div>
