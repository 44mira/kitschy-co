<script lang="ts">
	import { Button } from '$lib/components/ui/button';
</script>

<div class="cafe__hero bg-inherit h-screen">
	<div class="px-32 flex justify-between">
		<div class="flex flex-col gap-10 py-24">
			<h1 class="text-9xl text-brand-orangeCafe font-gladiola font-bold drop-shadow-lg">
				Cafe & Pastries
			</h1>
			<div class="text-[#5C1700] font-giphurs text-2xl leading-relaxed max-w-[500px] text-justify">
				This is a pretty short call to action text.
				<span class="text-[#BF3A0E]">I am very excited</span>
				and I want you to know too!
			</div>

			<Button
				class="py-6 w-52 border-t-2 border-l-2 border-b-8 border-r-8 border-brand-orangeCafe"
				variant="cafe">Menu</Button
			>
		</div>

		<div
			class="cafe__door rounded rounded-t-[999px] min-h-[600px] max-h-[600px] min-w-[600px]"
		></div>
	</div>
</div>

<style>
	.cafe__door {
		background-color: #949494;
	}
</style>
