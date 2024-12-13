import type { PageServerLoad, Actions } from './$types.js';
import { fail } from '@sveltejs/kit';
import { superValidate } from 'sveltekit-superforms';
import { signupSchema } from '$lib/api/schema';
import { zod, type ValidationAdapter } from 'sveltekit-superforms/adapters';

export const load: PageServerLoad = async () => {
	return {
		signupForm: await superValidate(zod(signupSchema))
	};
};

export const actions: Actions = {
	default: async (event) => {
		const form = await superValidate(event, zod(signupSchema));
		if (!form.valid) {
			return fail(400, {
				form
			});
		}
		return {
			form
		};
	}
};
