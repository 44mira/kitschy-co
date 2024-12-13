<script lang="ts">
	import blue_girl from '$lib/assets/users/blue_girl.png';
	import logo_purple from '$lib/assets/users/logo_purple.png';
	import Separator from '@/lib/components/ui/separator/separator.svelte';
	import { type MembershipInfo } from '@/api/schema';
	import blue_star from '$lib/assets/users/blue_star.png';
	import membership_card from '$lib/assets/users/membership_card.png';
	import Button from '@/lib/components/ui/button/button.svelte';
	//MOCK DATA
	const membership_number = '20231217';
	const userDetails: MembershipInfo[] = [
		{ label: 'Name', value: 'Aaron Dave A. Siapuatco' },
		{ label: 'Date of Issue', value: '2022-03-2092' },
		{ label: 'Location', value: 'Daet' },
		{ label: 'Likes', value: 'Men I trust Band (band)' },
		{ label: 'Social Media', value: '@bykitschyclub' },
		{ label: 'Color', value: 'Blue' },
		{ label: 'Bentables', value: 'Stickers & Photocards' }
	];
</script>

<div class="flex max-w-screen min-h-screen align-center justify-center bg-brand-purple-l">
	<div id="flip-card" class="pt-28">
		<div id="flip-card-inner" class="bg-membership">
			<!-- Front of card -->
			<div>
				<div id="flip-card-front" class="flex flex-col">
					<!-- Header section -->
					<div class="flex justify-between p-10 ml-8 mr-10">
						<img src={logo_purple} alt="Kitschy Logo" style="width:200px; height:50px;" />
						<div class="text-right">
							<p class="uppercase font-extrabold text-purple-900">Identification Card</p>
							<p class="uppercase font-extrabold text-purple-900">No. {membership_number}</p>
						</div>
					</div>

					<!-- Main content section -->
					<div class="flex flex-1 pl-20">
						<div class="absolute bg-admin-pink rounded-3xl border-black w-60 h-60 -ml-4 mt-1"></div>
						<div
							class="absolute border-[2px] border-dashed rounded-3xl border-black w-56 h-56 -m-2 mt-3"
						></div>
						<img src={blue_girl} alt="Logo" class="absolute w-36 h-36 mt-12 ml-8" />
						<!-- User details section -->
						<div class="flex-1 pl-80 pr-20 flex flex-col">
							<!-- User information -->
							{#each userDetails as detail}
								<div class="flex justify-between items-center mb-2">
									<p class="uppercase text-purple-900 font-extrabold">{detail.label}:</p>
									<p class="font-giphursSC text-right font-semibold">{detail.value}</p>
								</div>
								<Separator orientation="horizontal" class="border-t-2 border-dotted border-black" />
							{/each}

							<!-- Footer section -->
							<div class="bg-admin-pink w-full mt-4">
								<p class="uppercase font-bold text-white text-center text-[0.60rem] p-2">
									This identification card certified the bearer as a kitshchy club member.
								</p>
							</div>
						</div>
					</div>
				</div>
			</div>

			<!-- Back of card -->
			<div id="flip-card-back" class="bg-membership flex h-full">
				<!-- Left side content -->
				<div class="flex flex-col p-12 flex-1">
					<div class="flex items-start gap-2">
						<h1 class="font-giphurs text-3xl text-black">Some membership perks...</h1>
					</div>

					<div class="flex items-start gap-2 mt-8" id="back-content">
						<img src={blue_star} alt="Star" class="w-10 h-10 mt-1" />
						<div class="flex flex-col text-left pl-10 font-giphurs text-xl leading-relaxed">
							<p>Your very own physical</p>
							<p>Kitschy Club</p>
							<p>Membership Card</p>
						</div>
					</div>

					<div class="flex items-start gap-2 mt-20" id="back-content">
						<img src={blue_star} alt="Star" class="w-10 h-10 mt-1" />
						<div class="flex flex-col text-left pl-10 font-giphurs text-xl leading-relaxed">
							<p>Lifetime kitschyclub membership</p>
							<p>Birthday and registration freebies</p>
							<p>Early access & discounted product prices!</p>
						</div>
					</div>
				</div>

				<!-- Right side with membership card -->
				<div class="flex flex-col items-center pr-12 mt-20">
					<img src={membership_card} alt="Membership Card" class="drop-shadow-lg" />
				</div>
			</div>
		</div>
		<div class="flex flex-col items-center justify-center mt-20">
			<Button variant="membership">Join the club</Button>
		</div>
	</div>
</div>

<style>
	img {
		image-rendering: -webkit-optimize-contrast; /* For webkit browsers */
		image-rendering: crisp-edges;
	}
	#back-content {
		color: black;
		font: giphurs;
		font-weight: 500;
	}
	#flip-card {
		background-color: transparent;
		width: 900px;
		height: 600px;
		perspective: 1000px; /*Important for 3D effect */
	}

	#flip-card-inner {
		position: relative;
		width: 100%;
		height: 100%;
		text-align: center;
		transition: transform 0.8s;
		transform-style: preserve-3d;
		border-radius: 22px;
	}

	/* Do an horizontal flip when you move the mouse over the flip box container */
	#flip-card:hover #flip-card-inner {
		transform: rotateY(180deg);
	}
	/* Position the front and back side */
	#flip-card-front,
	#flip-card-back {
		position: absolute;
		width: 100%;
		height: 100%;
		-webkit-backface-visibility: hidden; /* Safari */
		backface-visibility: hidden;
	}

	/* Style the front side (fallback if image is missing) */
	#flip-card-front {
		color: black;
	}

	/* Style the back side */
	#flip-card-back {
		color: white;
		transform: rotateY(180deg);
		border-radius: inherit;
	}
</style>
