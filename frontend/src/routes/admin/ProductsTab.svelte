<script>
	import AddProductsDialog from './AddProductsDialog.svelte';
	let { data } = $props();
</script>

<div>
	<AddProductsDialog data={data.form} />
</div>
