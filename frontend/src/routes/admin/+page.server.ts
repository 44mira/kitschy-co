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
        console.log(addProductForm);
        if (!addProductForm.valid) {
            return fail(400, { addProductForm });
        }

        try {
            const response = await fetch('http:localhost:8000/kitschy_api/products', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(addProductForm.data)
            });

            if (!response.ok) {
                // Handle API errors
                const errorData = await response.json();
                return fail(response.status, { 
                    addProductForm,
                    error: errorData.message || 'Failed to create product'
                });
            }

            // Return success state with the form
            return {
                addProductForm,
                success: true
            };
        } catch (error) {
            // Handle network or other errors
            return fail(500, { 
                addProductForm,
                error: 'Server error occurred while creating product'
            });
        }
    }
};