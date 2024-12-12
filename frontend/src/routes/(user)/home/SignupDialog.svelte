<script lang="ts">
	import * as Dialog from '$lib/components/ui/dialog';
	import { toImageUrl } from '$lib/utils/index';
	import ticketBg from '$lib/assets/users/ticketBg.png';
	import * as Form from '$lib/components/ui/form';
	import { signupSchema } from '$lib/api/schema';
	import { superForm } from 'sveltekit-superforms';
	import { zodClient } from 'sveltekit-superforms/adapters';
	import Combobox from '@/lib/components/Combobox.svelte';

	let { data } = $props();
	const form = superForm(data, { validators: zodClient(signupSchema) });

	const getData = async (endpoint: string) => {
		const res = await fetch(`https://psgc.gitlab.io/api/${endpoint}/`);
		const data = await res.json();
		const filteredData = data.map((region: (typeof data)[0]) => ({
			value: region.code,
			label: region.name
		}));
		return filteredData;
	};

	let regionCode = $state('');
	let cityCode = $state('');
	let barangayCode = $state('');
</script>

<Dialog.Root open="true">
	<Dialog.Trigger>Sign Up!</Dialog.Trigger>

	<Dialog.Content
		class="w-[1000px] h-[472px] bg-transparent border-none shadow-none"
		style={`background-image: ${toImageUrl(ticketBg)}; background-size: cover;`}
	>
		<form method="POST" class="py-4 pr-16 pl-60 flex flex-col justify-center">
			<div class="grid grid-cols-2 gap-4 gap-y-0">
				<Form.Field {form} name="firstName">
					<Form.Control>
						<div class="field">
							<Form.Label>First Name:</Form.Label>
							<input class="col-span-2" placeholder="Samantha" />
						</div>
					</Form.Control>
				</Form.Field>

				<Form.Field {form} name="lastName">
					<Form.Control>
						<div class="field">
							<Form.Label>Last Name:</Form.Label>
							<input class="col-span-2" placeholder="Cruz" />
						</div>
					</Form.Control>
				</Form.Field>

				<Form.Field {form} name="email">
					<Form.Control>
						<div class="field">
							<Form.Label>E-mail:</Form.Label>
							<input class="col-span-2" placeholder="stay@kitschy.com" />
						</div>
					</Form.Control>
				</Form.Field>

				<Form.Field {form} name="phoneNo">
					<Form.Control>
						<div class="field">
							<Form.Label>Phone No.:</Form.Label>
							<input class="col-span-2" placeholder="09XXXXXXXXX" />
						</div>
					</Form.Control>
				</Form.Field>

				<Form.Field {form} name="password">
					<Form.Control>
						<div class="field">
							<Form.Label>Password:</Form.Label>
							<input class="col-span-2" type="password" placeholder="**********" />
						</div>
					</Form.Control>
				</Form.Field>

				<Form.Field {form} name="confirmPassword">
					<Form.Control>
						<div class="field">
							<Form.Label>Confirm Password:</Form.Label>
							<input class="col-span-2" type="password" placeholder="**********" />
						</div>
					</Form.Control>
				</Form.Field>

				<Form.Field {form} name="region">
					<Form.Control>
						<div class="field">
							<Form.Label>Region:</Form.Label>
							{#await getData('regions/')}
								<p>Loading...</p>
							{:then regions}
								<Combobox data={regions} bind:chosenValue={regionCode} />
							{/await}
						</div>
					</Form.Control>
				</Form.Field>

				<Form.Field {form} name="city">
					<Form.Control>
						<div class="field">
							<Form.Label>City:</Form.Label>
							{#if regionCode}
								{#await getData(`regions/${regionCode}/cities/`)}
									<p>Loading...</p>
								{:then regions}
									<Combobox data={regions} bind:chosenValue={cityCode} />
								{/await}
							{:else}
								<p class="col-span-2 text-gray-400 align-middle">Select a region first</p>
							{/if}
						</div>
					</Form.Control>
				</Form.Field>

				<Form.Field {form} name="barangay">
					<Form.Control>
						<div class="field">
							<Form.Label>Barangay:</Form.Label>
							{#if cityCode}
								{#await getData(`cities/${cityCode}/barangays/`)}
									<p>Loading...</p>
								{:then regions}
									<Combobox data={regions} chosenValue={barangayCode} />
								{/await}
							{:else}
								<p class="col-span-2 text-gray-400 align-middle">Select a city first</p>
							{/if}
						</div>
					</Form.Control>
				</Form.Field>

				<Form.Field {form} name="postalCode">
					<Form.Control>
						<div class="field">
							<Form.Label>Postal Code:</Form.Label>
							<input class="col-span-2" />
						</div>
					</Form.Control>
				</Form.Field>

				<Form.Field {form} name="detailedAddress" class="col-span-2">
					<Form.Control>
						<div class="field">
							<Form.Label>Detailed Address:</Form.Label>
							<input class="col-span-2" placeholder="Street Name, Building, Unit/House No." />
						</div>
					</Form.Control>
				</Form.Field>
			</div>

			<div class="flex flex-col items-center pt-6">
				<Form.Button
					class="w-fit rounded-full bg-transparent border-4 p-4 border-brand-yellow font-lockergnome text-brand-yellow text-2xl hover:bg-gradient-to-t from-brand-yellow to-brand-base"
					style="-webkit-text-stroke: 6px #804B7A;  paint-order: stroke fill;"
					variant="ghost">Claim my ticket!</Form.Button
				>
				<a href="/" class="text-center text-brand-purple-d underline hover:text-brand-purple"
					>Already have a ticket? Sign in!</a
				>
			</div>
		</form>
	</Dialog.Content>
</Dialog.Root>

<style>
	.field {
		@apply grid grid-cols-3 items-center gap-2 text-brand-purple-d h-10;
	}
</style>
