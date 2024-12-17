<script lang="ts">
	import SignupForm from './SignupForm.svelte';
	import * as Form from '$lib/components/ui/form';
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

	let isSignup = $state(true);
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
		{#if isSignup}
			<form
				action="?/signupForm"
				method="POST"
				class="py-4 pr-16 pl-60 flex flex-col justify-center"
				use:enhance
			>
				<SignupForm {form} />

				<!-- ACTIONS -->
				<div class="flex flex-col items-center pt-6">
					<Form.Button
						class="w-fit rounded-full bg-transparent border-4 p-4 border-brand-yellow font-lockergnome text-brand-yellow text-2xl hover:bg-gradient-to-t from-brand-yellow to-brand-base"
						style="-webkit-text-stroke: 6px #804B7A;  paint-order: stroke fill;"
						variant="ghost">Claim my ticket!</Form.Button
					>
					<button onclick={() => isSignup = false} class="text-center text-brand-purple-d underline hover:text-brand-purple" >
            Already have a ticket? Sign in!
          </button >
				</div>
			</form>
		{:else}
			<form
				action="?/loginForm"
				method="POST"
				class="py-4 pr-16 pl-60 flex flex-col justify-center"
				use:enhance
			>

        <!-- ACTIONS -->
        <div class="flex flex-col items-center pt-6">
          <Form.Button
            class="w-fit rounded-full bg-transparent border-4 p-4 border-brand-yellow font-lockergnome text-brand-yellow text-2xl hover:bg-gradient-to-t from-brand-yellow to-brand-base"
            style="-webkit-text-stroke: 6px #804B7A;  paint-order: stroke fill;"
            variant="ghost">Claim my ticket!</Form.Button
          >
          <button onclick={() => isSignup = true} class="text-center text-brand-purple-d underline hover:text-brand-purple" >
            Don't have a ticket yet? Register here!
          </button >
        </div>
			</form>
		{/if}
	</Dialog.Content>
</Dialog.Root>

<style>
	.field {
		@apply grid grid-cols-3 items-center gap-2 text-brand-purple-d h-10;
	}
</style>
