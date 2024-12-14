<script lang="ts">
	import HeaderCard from './HeaderCard.svelte';
	import HeaderCardContents from './HeaderCardContents';
</script>

<div class="w-full">
	<div class="bg-brand-base p-8 mb-8 rounded-lg shadow-md">
		<div
			class="grid grid-cols-1 xl:grid-cols-3 lg:grid-cols-2 md:grid-cols-2 sm:grid-cols-1 mb-8 gap-8"
		>
			{#each HeaderCardContents as headerCard}
				<HeaderCard {...headerCard} />
			{/each}
		</div>
	</div>
</div>
