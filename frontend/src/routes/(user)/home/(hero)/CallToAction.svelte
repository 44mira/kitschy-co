<script lang="ts">
	import { getContext } from 'svelte';
	import SignupDialog from './SignupDialog.svelte';

	import type { PageData } from '../$types';

	const data: PageData = getContext('data');

	const { src, primary } = $props();
</script>

<div class="grow-0 basis-[30%]">
	<p class="mb-5 font-galdeano">
		At kitschy co. ✨, our goal is to create a unique experience 🌟 and a welcoming environment 🏡
		that will entice our customers' to return time and time again 💫.
	</p>
	<div class="flex h-52">
		<img style:scale="0.40" class="head--tilt2" {src} alt="girl tilting her head" />
		<SignupDialog data={data.signupForm} {primary} />
	</div>
</div>
