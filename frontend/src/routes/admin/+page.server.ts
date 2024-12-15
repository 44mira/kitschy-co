import type { PageServerLoad, Actions } from './$types.js';
import { fail } from '@sveltejs/kit';
import { superValidate } from 'sveltekit-superforms';
import { addProductSchema } from '@/api/adminSchema';
import { zod } from 'sveltekit-superforms/adapters';

export const load: PageServerLoad = async () => {
	return {
		addProductForm: await superValidate(zod(addProductSchema))
	};
};

export const actions: Actions = {
	default: async (event) => {
		const addProductForm = await superValidate(event, zod(addProductSchema));
		if (addProductForm.valid) {
			return fail(400, { addProductForm });
		}
		return {
			addProductForm
		};
	}
};
