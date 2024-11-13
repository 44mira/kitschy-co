<script>
  import Navbar from "$lib/components/admin/Navbar.svelte";
  import {toImageUrl} from '$lib/utils/index'
  import polkaBg from "$lib/assets/admin/polkaBg.png"
</script>

<div class="h-screen w-screen" style='background-image: {toImageUrl(polkaBg)}; background-size: cover'>
  <Navbar/>
</div>
