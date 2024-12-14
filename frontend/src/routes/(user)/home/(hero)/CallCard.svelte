<script lang="ts">
	import hs from './state.svelte.ts';

	let { primary, icon: src, theme } = $props();
</script>

<div class="callcard p-4 shadow shadow-black mx-auto">
	<div
		class="h-full w-full border-[3px] rounded-xl flex items-center justify-center"
		style:border-color={primary}
	>
		<button onclick={() => (hs.currentTheme = theme)}>
			<img {src} alt="card icon" class="" />
		</button>
	</div>
</div>

<style>
	.callcard {
		background-color: rgba(230, 230, 255, 0.95);
		border-radius: 1.5em;
		height: 474px;
		width: 335px;
	}
</style>
