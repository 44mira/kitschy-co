<script lang="ts">
	import roof from '$lib/assets/users/roof.png';
	import { Button } from '@/components/ui/button';
</script>

<div class="cafe__body max-h-screen min-h-screen flex flex-col">
	<div class="overflow-clip top-0 sticky z-10">
		<img
			src={roof}
			class="object-cover -translate-y-10 w-full scale-75 scale-x-105"
			alt="cafe and pastries roof"
		/>
	</div>
	<div class="cafe__hero bg-inherit h-screen">
		<div class="px-32 flex justify-between">
			<div class="flex flex-col gap-10 py-24">
				<h1 class="text-9xl text-brand-orangePastries font-gladiola font-bold drop-shadow-lg">
					Cafe & Pastries
				</h1>
				<div
					class="text-[#5C1700] font-giphurs text-2xl leading-relaxed max-w-[500px] text-justify"
				>
					This is a pretty short call to action text.
					<span class="text-[#BF3A0E]">I am very excited</span>
					and I want you to know too!
				</div>

				<Button
					class="py-6 w-52 border-t-2 border-l-2 border-b-8 border-r-8 border-brand-orangePastries"
					variant="cafe">Menu</Button
				>
			</div>

			<div
				class="cafe__door rounded rounded-t-[999px] min-h-[600px] max-h-[600px] min-w-[600px]"
			></div>
		</div>
	</div>

	<div class="px-6 bg-inherit">
		<div class="min-w-full bg-brand-base min-h-52 grow"></div>
	</div>
</div>

<style>
	.cafe__body {
		background-color: #ffe3cc;
	}

	.cafe__door {
		background-color: #949494;
	}
</style>
