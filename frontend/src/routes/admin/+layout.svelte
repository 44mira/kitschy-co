<script>
	import Navbar from '$lib/components/admin/Navbar.svelte';

	let { children } = $props();
</script>

<Navbar />

{@render children()}
