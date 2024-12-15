<script lang="ts">
	import type { HeaderCard } from './HeaderCardContents.ts';

	type HeaderCardProps = HeaderCard & { children?: import('svelte').Snippet };

	const { bgColor, bgIcon, headerColor, headerContent, bgContent }: HeaderCardProps = $props();
</script>

<div class="flex-1 relative">
	<img src={bgIcon} alt="background icon" class="absolute opacity-25 top-20 mix-blend-dodge z-0" />
	<div
		class="h-[700px] rounded-lg flex flex-col items-center justify-start overflow-hidden bg-center bg-no-repeat"
		style="background-color: {bgColor}"
	>
		<p
			class="font-gasoekOne text-center text-[56px] lg:text-[50px] md:text-[52px] sm:text-[56px] font-bold px-8 mt-12 mb-12"
			style="color: {headerColor}"
		>
			{headerContent}
		</p>
		<p
			class="text-black text-left text-xl sm:text-xl md:text-lg lg:text-xl xl:text-xl font-giphurs px-8 break-words max-w-full overflow-auto z-[1]"
		>
			{bgContent}
		</p>
	</div>
</div>
