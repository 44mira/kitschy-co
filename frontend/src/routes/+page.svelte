<script lang="ts">
	import SignupDialog from './SignupDialog.svelte';
	import type { PageData } from './$types';

	export let data: PageData;
</script>

<SignupDialog data={data.signupForm} />
