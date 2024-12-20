import type { PageServerLoad, Actions } from './$types.js';
import { fail } from '@sveltejs/kit';
import { message, superValidate } from 'sveltekit-superforms';
import { signupSchema, loginSchema } from '@/api/schema';
import { zod, type ValidationAdapter } from 'sveltekit-superforms/adapters';

export const load: PageServerLoad = async () => {
	const signupForm = await superValidate(zod(signupSchema));
	const loginForm = await superValidate(zod(loginSchema));
	return { signupForm, loginForm };
};

export const actions: Actions = {
	// runs when the signup form is submitted
	signupForm: async (request) => {
		const signupForm = await superValidate(request, zod(signupSchema));
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
	},

	loginForm: async ({ request }) => {
		const loginForm = await superValidate(request, zod(loginSchema));

		if (!loginForm.valid) return fail(400, { loginForm });

		return message(loginForm, 'Login form submitted');
	}
};
