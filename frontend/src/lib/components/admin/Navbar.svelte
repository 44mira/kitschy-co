<script>
	import { Button } from '$lib/components/ui/button';
	import { Avatar, AvatarFallback, AvatarImage } from '$lib/components/ui/avatar';
	import { Popover, PopoverTrigger, PopoverContent } from '$lib/components/ui/popover';
	import logo from '$lib/assets/admin/logo.png';
</script>

<nav
	class="h-fit flex items-center bg-brand-base border border-b-[3px] border-b-brand-purple-d p-2 px-10 justify-between sticky"
>
	<div class="h-full">
		<a href="/" target="_blank"><img src={logo} alt="kitschy co." width="200" /></a>
	</div>
	<div class="h-full">
		<Popover>
			<PopoverTrigger>
				<Avatar>
					<AvatarImage src="https://github.com/shadcn.png" alt="@shadcn" />
					<AvatarFallback>CN</AvatarFallback>
				</Avatar>
			</PopoverTrigger>

			<PopoverContent class=" w-fit">
				<div class="flex flex-col gap-2">
					<Button>Account Details</Button>
					<Button>Sign-out</Button>
				</div>
			</PopoverContent>
		</Popover>
	</div>
</nav>
