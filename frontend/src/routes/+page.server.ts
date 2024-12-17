import { redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = () => {
	// redirect to home route with status code 301 (permanent redirect)
	redirect(301, '/home');
};
