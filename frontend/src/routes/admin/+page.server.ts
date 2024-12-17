import type { PageServerLoad, Actions } from './$types.js';
import { fail } from '@sveltejs/kit';
import { superValidate } from 'sveltekit-superforms';
import { addProductSchema, type AddProductSchema } from '@/api/adminSchema';
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
		//putProduct(editProductForm.data);
	}
} satisfies Actions;

async function postProduct(data: any) {
	try {
		const response = await fetch('http://localhost:8000/api/products', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(data)
		});

		if (!response.ok) {
			const errorData = await response.json();
			throw new Error(errorData.message || 'Failed to add product');
		}

		return await response.json();
	} catch (error) {
		throw new Error(error instanceof Error ? error.message : 'Failed to make API request');
	}
}

//function putProduct(data) {}
