import type { PageServerLoad, Actions } from './$types.js';
import { fail } from '@sveltejs/kit';
import { superValidate } from 'sveltekit-superforms';
import { addProductSchema } from '@/api/adminSchema';
import { zod } from 'sveltekit-superforms/adapters';

export const load: PageServerLoad = async () => {
	return {
		form: await superValidate(zod(addProductSchema))
	};
};

export const actions: Actions = {
	default: async (event) => {
		const form = await superValidate(event, zod(addProductSchema));
		if (form.valid) {
			return fail(400, { form });
		}
		return {
			form
		};
	}
};
