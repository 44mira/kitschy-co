<script lang="ts">
	import SignupDialog from './SignupDialog.svelte';
	import HeaderCards from './(headerCards)/HeaderCards.svelte';
	import type { PageData } from './$types';
	export let data: PageData;
</script>

<div class="bg-pink-500 flex flex-col items-center justify-center min-h-screen">
	<SignupDialog data={data.signupForm} />
	<HeaderCards />
</div>
