import type { PageServerLoad, Actions } from './$types.js';
import { fail } from '@sveltejs/kit';
import { superValidate } from 'sveltekit-superforms';
import { signupSchema } from '@/api/schema';
import { zod, type ValidationAdapter } from 'sveltekit-superforms/adapters';

export const load: PageServerLoad = async () => {
	return {
		signupForm: await superValidate(zod(signupSchema))
	};
};

export const actions: Actions = {
	// runs when the signup form is submitted
	default: async (event) => {
		const signupForm = await superValidate(event, zod(signupSchema));
		if (!signupForm.valid) {
			return fail(300, {
				signupForm
			});
		}

		let data = signupForm.data;
		let postData = {
			...data,
			address: {
				region: data.region,
				city: data.city,
				barangay: data.barangay,
				postal_code: data.postal_code,
				detailed_address: data.detailed_address
			}
		};

		return postData;
	}
};
