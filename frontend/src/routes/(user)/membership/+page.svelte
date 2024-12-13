<script lang="ts">
  import blue_girl from '$lib/assets/users/blue_girl.png'
  import logo_purple from '$lib/assets/users/logo_purple.png'
  import Separator from '@/lib/components/ui/separator/separator.svelte';
  import { type MembershipInfo } from '@/api/schema';

  //MOCK DATA
  const userDetails: MembershipInfo[] = [
    {label: "Name", value: "Aaron Dave A. Siapuatco"},
    {label: "Date of Issue", value: "2022-03-2092"},
    {label: "Location", value: "Daet"},
    {label: "Likes", value: "Men I trust Band (band)"},
    {label: "Social Media", value: "@bykitschyclub"},
    {label: "Color", value: "Blue"},
    {label: "Bentables", value: "Stickers & Photocards"},
  ]

  const membership_number = "20231008"
</script>
<div class="flex max-w-screen min-h-screen align-center justify-center bg-brand-purple-l">
  <div id="flip-card" class="pt-28">
    <div id="flip-card-inner" class="bg-membership">
      <!-- Front of card -->
      <div class="h-full">
        <div id="flip-card-front" class="flex flex-col h-full">
          <!-- Header section -->
          <div class="flex justify-between p-6">
            <img src={logo_purple} alt="Kitschy Logo" style="width:200px; height:50px;">
            <div class="text-right">
              <p class="uppercase font-extrabold text-purple-900">Identification Card</p>
              <p class="uppercase font-extrabold text-purple-900">No. {membership_number}</p>
            </div>
          </div>

          <!-- Main content section -->
          <div class="flex flex-1 pl-20">
            <div class="absolute border-4 border-dotted border-purple-900 w-52 h-52 -m-2"></div>
            <!-- Profile image -->
            <img src={blue_girl} alt="Profile Picture" class="w-48 h-48">

            <!-- User details section -->
            <div class="flex-1 pl-20 pr-20 flex flex-col">
              <!-- User information -->
              {#each userDetails as detail}
                <div class="flex justify-between items-center mb-2">
                  <p class="uppercase text-purple-900 font-extrabold">{detail.label}: </p>
                  <p class="font-giphursSC text-right font-semibold">{detail.value}</p>
                </div>
                <Separator className="border-dotted border-t-2 w-full border-purple-900" />
              {/each}

              <!-- Footer section -->
              <div class="bg-admin-pink w-full ">
                <p class="uppercase font-bold text-white text-center text-[0.65rem] p-2">
                  This identification card certified the bearer as a kitshchy club member.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Back of card -->
      <div id="flip-card-back" class="bg-membership flex flex-col items-center justify-center space-y-2">
        <h1 class="font-bold text-lg">Some membership perks...</h1>
        <p>Your very own physical</p>
        <p>Kitschy Club</p>
        <p>Membership Card</p>
      </div>
    </div>
  </div>
</div>

<style>
  #flip-card{
    background-color: transparent;
    width: 900px;
    height: 600px;
    perspective: 1000px; /*Important for 3D effect */
  }

  #flip-card-inner{
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
  #flip-card-front, #flip-card-back {
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