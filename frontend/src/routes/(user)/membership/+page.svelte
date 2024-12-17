<script lang="ts">
	import blue_girl from '$lib/assets/users/blue_girl.png';
	import logo_purple from '$lib/assets/users/logo_purple.png';
	import Separator from '@/lib/components/ui/separator/separator.svelte';
	import blue_star from '$lib/assets/users/blue_star.png';
	import membership_card from '$lib/assets/users/membership_card.png';
	import Button from '@/lib/components/ui/button/button.svelte';
	//MOCK DATA
	type MembershipInfo = {
	label: string;
	value: string;
	};

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
	<div id="flip-card" class="pt-28 p-8">
		<div id="flip-card-inner" class="bg-membershipWhite">
			<!-- Front of card -->
			<div>
				<div id="flip-card-front" class="flex flex-col">
					<!-- Header section -->
					<div class="flex justify-between p-6 sm:p-10 ml-4 sm:ml-8 mr-4 sm:mr-10">
						<img src={logo_purple} alt="Kitschy Logo" class="w-36 h-11 sm:w-52 sm:h-14" />
						<div class="text-right">
							<p class="uppercase font-extrabold text-purple-900 text-sm sm:text-base">
								Identification Card
							</p>
							<p class="uppercase font-extrabold text-purple-900 text-sm sm:text-base">
								No. {membership_number}
							</p>
						</div>
					</div>

					<!-- Main content section -->
					<div class="flex flex-1 pl-8 sm:pl-16 md:pl-20">
						<div class="absolute bg-admin-pink rounded-3xl border-black w-40 h-40 sm:w-60 sm:h-60 -ml-4 sm:-ml-4 mt-1"></div>
						<div
							class="absolute border-[2px] border-dashed rounded-3xl border-black w-36 h-36 sm:w-56 sm:h-56 -m-2 mt-3"
						></div>
						<img src={blue_girl} alt="Logo" class="absolute w-20 h-20 sm:w-36 sm:h-36 mt-10 ml-6 sm:mt-12 sm:ml-8" />
						<!-- User details section -->
						<div class="flex-1 pl-40 sm:pl-60 md:pl-80 pr-4 sm:pr-10 md:pr-10 flex flex-col">
							<!-- User information -->
							{#each userDetails as detail}
								<div class="flex justify-between items-center mb-2">
									<p class="uppercase text-purple-900 font-extrabold text-xs sm:text-xs md:text-sm">{detail.label}:</p>
									<p class="font-giphursSC text-right font-semibold text-xs sm:text-xs md:text-sm">{detail.value}</p>
								</div>
								<Separator orientation="horizontal" class="border-t-[1px] sm:border-t-2 border-dotted border-black" />
							{/each}

							<!-- Footer section -->
							<div class="bg-admin-pink w-full mt-4">
								<p class="uppercase font-bold text-white text-center text-[0.50rem] sm:text-[0.60rem] p-2">
									This identification card certified the bearer as a kitschy club member.
								</p>
							</div>
						</div>
					</div>
				</div>
			</div>

			<!-- Back of card -->
			<div id="flip-card-back" class="bg-membershipWhite flex h-full">
				<!-- Left side content -->
				<div class="flex flex-col p-8 sm:p-12 flex-1">
					<div class="flex items-start gap-2">
						<h1 class="font-giphurs text-base sm:text-base md:text-2xl lg:text-3xl text-black">Some membership perks...</h1>
					</div>

					<div class="flex items-start gap-2 mt-8 sm:mt-4 md:mt-8" id="back-content">
						<img src={blue_star} alt="Star" class="w-8 sm:w-10 h-8 sm:h-10 mt-1" />
						<div class="flex flex-col text-left pl-6 sm:pl-1 md:pl-10 font-giphurs text-sm sm:text-sm md:text-base lg:text-lg leading-relaxed">
							<p>Your very own physical</p>
							<p>Kitschy Club</p>
							<p>Membership Card</p>
						</div>
					</div>

					<div class="flex items-start gap-2 mt-6 sm:mt-8 md:mt-16" id="back-content">
						<img src={blue_star} alt="Star" class="w-8 sm:w-10 h-8 sm:h-10 mt-1" />
						<div class="flex flex-col text-left pl-6 sm:pl-1 md:pl-10 font-giphurs text-sm sm:text-sm md:text-base lg:text-lg leading-relaxed">
							<p>Lifetime kitschyclub membership</p>
							<p>Birthday and registration freebies</p>
							<p>Early access & discounted product prices!</p>
						</div>
					</div>
				</div>

				<!-- Right side with membership card -->
				<div class="flex flex-col items-center pr-4 sm:pr-12 mt-36 sm:mt-24 md:mt-20">
					<img src={membership_card} alt="Membership Card" class="drop-shadow-lg w-40 sm:w-auto" />
				</div>
			</div>
		</div>
		<div class="flex flex-col items-center justify-center mt-10 sm:mt-20">
			<Button variant="membership">Join the club</Button>
		</div>
	</div>
</div>

<style>
	/* General Styles */
	img {
		image-rendering: -webkit-optimize-contrast; /* For webkit browsers */
		image-rendering: crisp-edges;
	}

	#flip-card {
		background-color: transparent;
		width: 100%;
		max-width: 900px;
		height: auto;
		max-height: 600px;
		perspective: 1000px; /* Important for 3D effect */
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

	/* Default Horizontal Flip (Large screens) */
	#flip-card:hover #flip-card-inner {
		transform: rotateY(180deg);
	}

	/* Front and Back Side Positioning */
	#flip-card-front,
	#flip-card-back {
		position: absolute;
		width: 100%;
		height: 100%;
		-webkit-backface-visibility: hidden; /* Safari */
		backface-visibility: hidden;
	}

	/* Styling the Front Side */
	#flip-card-front {
		color: black;
	}

	/* Styling the Back Side */
	#flip-card-back {
		color: black;
		transform: rotateY(180deg); /* Flip horizontally */
		border-radius: inherit;
	}

	/* Responsive Adjustments for Small Screens */
	@media (max-width: 640px) {
		#flip-card:hover #flip-card-inner {
			transform: rotateX(180deg); /* Flip vertically */
		}

		#flip-card-back {
			transform: rotateX(180deg); /* Adjust back side for vertical flip */
		}
	}
</style>

