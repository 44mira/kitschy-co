<script lang="ts">
	import * as Dialog from '$lib/components/ui/dialog';
	import { toImageUrl } from '$lib/utils/index';
	import ticketBg from '$lib/assets/admin/ticketBg.png';
	import * as Form from '$lib/components/ui/form';
	import * as DropdownMenu from '$lib/components/ui/dropdown-menu';
	import { Input } from '$lib/components/ui/input';
	import { Button } from '$lib/components/ui/button';
	import { signupSchema, type SignupSchema } from './schema';
	import { type SuperValidated, type Infer, superForm } from 'sveltekit-superforms';
	import { zodClient } from 'sveltekit-superforms/adapters';

	let { data } = $props();
	const form = superForm(data, { validators: zodClient(signupSchema) });
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
							<Input class="col-span-2" placeholder="Samantha" />
						</div>
					</Form.Control>
				</Form.Field>

				<Form.Field {form} name="lastName">
					<Form.Control>
						<div class="field">
							<Form.Label>Last Name:</Form.Label>
							<Input class="col-span-2" placeholder="Cruz" />
						</div>
					</Form.Control>
				</Form.Field>

				<Form.Field {form} name="email">
					<Form.Control>
						<div class="field">
							<Form.Label>E-mail:</Form.Label>
							<Input class="col-span-2" placeholder="stay@kitschy.com" />
						</div>
					</Form.Control>
				</Form.Field>

				<Form.Field {form} name="phoneNo">
					<Form.Control>
						<div class="field">
							<Form.Label>Phone No.:</Form.Label>
							<Input class="col-span-2" placeholder="09XXXXXXXXX" />
						</div>
					</Form.Control>
				</Form.Field>

				<Form.Field {form} name="password">
					<Form.Control>
						<div class="field">
							<Form.Label>Password:</Form.Label>
							<Input class="col-span-2" type="password" placeholder="**********" />
						</div>
					</Form.Control>
				</Form.Field>

				<Form.Field {form} name="confirmPassword">
					<Form.Control>
						<div class="field">
							<Form.Label>Confirm Password:</Form.Label>
							<Input class="col-span-2" type="password" placeholder="**********" />
						</div>
					</Form.Control>
				</Form.Field>

				<Form.Field {form} name="region">
					<Form.Control>
						<div class="field">
							<Form.Label>Region:</Form.Label>
							<Input class="col-span-2" />
						</div>
					</Form.Control>
				</Form.Field>

				<Form.Field {form} name="city">
					<Form.Control>
						<div class="field">
							<Form.Label>City:</Form.Label>
							<Input class="col-span-2" />
						</div>
					</Form.Control>
				</Form.Field>

				<Form.Field {form} name="barangay">
					<Form.Control>
						<div class="field">
							<Form.Label>Barangay:</Form.Label>
							<Input class="col-span-2" />
						</div>
					</Form.Control>
				</Form.Field>

				<Form.Field {form} name="postalCode">
					<Form.Control>
						<div class="field">
							<Form.Label>Postal Code:</Form.Label>
							<Input class="col-span-2" />
						</div>
					</Form.Control>
				</Form.Field>

				<Form.Field {form} name="detailedAddress" class="col-span-2">
					<Form.Control>
						<div class="field">
							<Form.Label>Detailed Address:</Form.Label>
							<Input class="col-span-2" placeholder="Street Name, Building, Unit/House No." />
						</div>
					</Form.Control>
				</Form.Field>
			</div>

			<div class="flex flex-col items-center pt-6">
				<Form.Button class="w-32">Claim my ticket!</Form.Button>
				<a href="/" class="text-center">Already have a ticket? Sign in!</a>
			</div>
		</form>
	</Dialog.Content>
</Dialog.Root>

<style>
	.field {
		@apply grid grid-cols-3 items-center gap-2;
	}
</style>
