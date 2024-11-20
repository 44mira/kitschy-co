<script lang="ts">
	import * as Form from '$lib/components/ui/form';
	import * as Dialog from '$lib/components/ui/dialog';
	import { Input } from '$lib/components/ui/input';
	import { Button } from '@/components/ui/button';
	import { addProductSchema, type AddProductSchema } from './schema';
	import { type SuperValidated, type Infer, superForm } from 'sveltekit-superforms';
	import { zodClient } from 'sveltekit-superforms/adapters';

	// export let data: SuperValidated<Infer<AddProductSchema>>;
	let { data } = $props();

	const addProductForm = superForm(data, {
		validators: zodClient(addProductSchema)
	});
</script>

<Dialog.Root>
	<Dialog.Trigger>Open</Dialog.Trigger>
	<Dialog.Content>
		<form method="POST">
			<div id="form" class="flex gap-4">
				<div id="left">
					<Form.Field form={addProductForm} name="productImages">
						<Form.Control>
							<Form.Label for="images-input">
								<div class="w-[250px] h-[250px] border"></div>
							</Form.Label>
							<Input id="images-input" type="file" multiple class="w-0 h-0 p-0" accept='image/*'/>
						</Form.Control>
						<Form.FieldErrors />
					</Form.Field>
				</div>
				<div id="right">
					<Form.Field form={addProductForm} name="category">
						<Form.Control>
							<Form.Label>Category:</Form.Label>
							<Input type="text" />
						</Form.Control>
						<Form.FieldErrors />
					</Form.Field>

					<Form.Field form={addProductForm} name="creators">
						<Form.Control>
							<Form.Label>Creator/s:</Form.Label>
							<Input type="text" />
						</Form.Control>
						<Form.FieldErrors />
					</Form.Field>
					<Form.Field form={addProductForm} name="price">
						<Form.Control>
							<Form.Label>Price:</Form.Label>
							<Input type="text" />
						</Form.Control>
						<Form.FieldErrors />
					</Form.Field>
					<Form.Field form={addProductForm} name="desc">
						<Form.Control>
							<Form.Label>Description:</Form.Label>
							<Input
								type="text"
								placeholder="Add a description to give users more context on the product. Be detailed and thorough. Possible important information: units, dimensions, material."
							/>
						</Form.Control>
						<Form.FieldErrors />
					</Form.Field>
				</div>
			</div>
			<div id="actions" class="flex justify-end gap-4">
				<Button>Cancel</Button>
				<Form.Button>Add Item</Form.Button>
			</div>
		</form>
	</Dialog.Content>
</Dialog.Root>
