<script>
	import AvatarDropdown from './AvatarDropdown.svelte';
	import CartLink from './CartLink.svelte';
	import MerchandiseDropdown from './MerchandiseDropdown.svelte';

	import logo from '$lib/assets/admin/logo.png';
</script>

<nav
	class="min-h-[9.82vh] z-10 flex items-center bg-brand-base border border-b-[3px] border-b-brand-purple-d p-2 px-10 justify-between sticky"
>
	<div class="min-h-fit flex items-center">
		<a href="/home"><img src={logo} alt="kitschy co." width="200" /></a>
	</div>

	<!-- side items -->
	<div class="flex items-center gap-5">
		<AvatarDropdown />
		<CartLink />
		<MerchandiseDropdown />
	</div>
</nav>
