<script lang="ts">
	import type { PageData } from './$types.js';
	import AddProductsForm from './AddProductsDialog.svelte';
	let { data } = $props();
</script>

<div>
	<AddProductsForm data={data.form} />
</div>
