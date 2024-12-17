<script lang="ts">
	import * as Form from '$lib/components/ui/form';
	import Combobox from '@/lib/components/Combobox.svelte';

	let { form } = $props();

	const getData = async (endpoint: string) => {
		const res = await fetch(`https://psgc.gitlab.io/api/${endpoint}/`);
		const data = await res.json();
		const filteredData = data.map((region: (typeof data)[0]) => ({
			value: region.code,
			label: region.name
		}));
		return filteredData;
	};

	let addressCodes = $state({ region: '', city: '', barangay: '' });
</script>

<div class="grid grid-cols-2 gap-4 gap-y-0">
	<Form.Field {form} name="first_name">
		<Form.Control>
			<div class="field">
				<Form.Label>First Name:</Form.Label>
				<input class="col-span-2" placeholder="Samantha" />
			</div>
		</Form.Control>
	</Form.Field>

	<Form.Field {form} name="last_name">
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

	<Form.Field {form} name="phone_number">
		<Form.Control>
			<div class="field">
				<Form.Label>Phone No.:</Form.Label>
				<input class="col-span-2" placeholder="09XXXXXXXXX" />
			</div>
		</Form.Control>
	</Form.Field>

	<Form.Field {form} name="password1">
		<Form.Control>
			<div class="field">
				<Form.Label>Password:</Form.Label>
				<input class="col-span-2" type="password" placeholder="**********" />
			</div>
		</Form.Control>
	</Form.Field>

	<Form.Field {form} name="password2">
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
					<Combobox data={regions} bind:chosenValue={addressCodes.region} />
				{/await}
			</div>
		</Form.Control>
	</Form.Field>

	<Form.Field {form} name="city">
		<Form.Control>
			<div class="field">
				<Form.Label>City:</Form.Label>
				{#if addressCodes.region}
					{#await getData(`regions/${addressCodes.region}/cities/`)}
						<p>Loading...</p>
					{:then regions}
						<Combobox data={regions} bind:chosenValue={addressCodes.city} />
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
				{#if addressCodes.city}
					{#await getData(`cities/${addressCodes.city}/barangays/`)}
						<p>Loading...</p>
					{:then regions}
						<Combobox data={regions} chosenValue={addressCodes.barangay} />
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
