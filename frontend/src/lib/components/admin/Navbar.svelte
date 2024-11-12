<script>
  import * as Avatar from '@/components/ui/avatar'
  import logo from '@/assets/logo.png'
</script>

<nav class="h-fit flex items-center bg-slate-400 p-2 px-10 justify-between">
<div class="h-full"><a href="/" target="_blank"><img src={logo} alt="kitschy co." width="200"></a></div>
<div>
  <Avatar.Root>
    <Avatar.Image src="https://github.com/shadcn.png" alt="@shadcn" />
    <Avatar.Fallback>CN</Avatar.Fallback>
  </Avatar.Root>
</div>
</nav>