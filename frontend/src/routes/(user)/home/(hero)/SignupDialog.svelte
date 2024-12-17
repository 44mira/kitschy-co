<script lang="ts">
	import SignupForm from './SignupForm.svelte';
	import * as Dialog from '$lib/components/ui/dialog';
	import ticketBg from '$lib/assets/users/ticketBg.png';
	import { signupSchema } from '@/api/schema';
	import SuperDebug, { superForm } from 'sveltekit-superforms';
	import { zodClient } from 'sveltekit-superforms/adapters';
	import { getContext } from 'svelte';
	import type { PageData } from '../$types';

	const data: PageData = getContext('data');
	let { primary } = $props();
	const form = superForm(data.signupForm, { validators: zodClient(signupSchema) });

	const { form: formData, enhance } = form;
</script>

<Dialog.Root open={false}>
	<Dialog.Trigger>
		<div
			class="font-gasoekOne text-white p-5 rounded-[3em] text-xl md:text-lg lg:text-xl xl:text-2xl"
			style:background-color={primary}
		>
			Register here!
		</div>
	</Dialog.Trigger>

	<Dialog.Content
		class="w-[1000px] h-[472px] bg-transparent border-none shadow-none"
		style={`background-image: url(${ticketBg}); background-size: cover`}
	>
		<form action="?/signupForm" method="POST" class="py-4 pr-16 pl-60 flex flex-col justify-center" use:enhance>
			<SignupForm {form} />
		</form>
	</Dialog.Content>
</Dialog.Root>

<style>
	.field {
		@apply grid grid-cols-3 items-center gap-2 text-brand-purple-d h-10;
	}
</style>
