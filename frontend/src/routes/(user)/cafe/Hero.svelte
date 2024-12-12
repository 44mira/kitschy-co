<script lang="ts">
	import { Button } from '$lib/components/ui/button';
</script>

<!-- Hero Section -->
<div class="cafe__hero bg-inherit h-auto flex flex-col justify-between">
	<div class="px-12 sm:px-12 md:px-24 lg:px-24 xl:px-32 flex flex-col md:flex-row justify-between items-center gap-10 pt-4 pb-16 md:pb-20">
		<!-- Text Section -->
		<div class="flex flex-col gap-6 md:gap-10 pb-16 sm:pb-20 md:pb-24 lg:pb-32 md:-mt-12 lg:-mt-16">
			<h1 class="text-7xl sm:text-8xl md:text-7xl lg:text-7xl xl:text-8xl text-brand-orangePastries font-gladiola font-bold drop-shadow-lg text-center md:text-left">
				Cafe & Pastries
			</h1>
			<div class="text-[#5C1700] font-giphurs text-2xl sm:text-2xl md:text-xl lg:text-2xl leading-relaxed max-w-full md:max-w-[500px] text-justify">
				This is a pretty short call to action text.
				<span class="text-[#BF3A0E]">I am very excited</span>
				and I want you to know too!
			</div>

			<Button
				class="py-4 sm:py-4 md:py-6 w-40 sm:w-48 md:w-52 border-t-2 border-l-2 border-b-8 border-r-8 border-brand-orangePastries mx-auto md:mx-0"
				variant="cafe">Menu</Button>
		</div>

		<!-- Cafe Door -->
		<div
			class="cafe__door rounded rounded-t-[999px] h-[350px] sm:h-[450px] md:h-[600px] lg:h-[600px] w-[350px] sm:w-[450px] md:w-[600px] lg:w-[600px] self-center md:self-end"
		></div>
	</div>
</div>

<style>
	.cafe__door {
		background-color: #949494;
	}
</style>
