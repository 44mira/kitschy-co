import type { PageServerLoad, Actions } from './$types.js';
import { fail } from '@sveltejs/kit';
import { superValidate } from 'sveltekit-superforms';
import { addProductSchema } from '@/api/adminSchema';
import { zod } from 'sveltekit-superforms/adapters';

export const load: PageServerLoad = async () => {
	const addProductForm = await superValidate(zod(addProductSchema));
	const editProductForm = await superValidate(zod(addProductSchema));

	return { addProductForm, editProductForm };
};

export const actions: Actions = {
	addProduct: async ({ request }) => {
		const addProductForm = await superValidate(request, zod(addProductSchema));
		if (addProductForm.valid) {
			return fail(400, { addProductForm });
		}

		// Add product
		postProduct(addProductForm.data);
	},
	editProduct: async ({ request }) => {
		const editProductForm = await superValidate(request, zod(addProductSchema));
		if (editProductForm.valid) {
			return fail(400, { editProductForm });
		}

		// Edit product
		putProduct(editProductForm.data);
	}
} satisfies Actions;

function postProduct(data) {}

function putProduct(data) {}
