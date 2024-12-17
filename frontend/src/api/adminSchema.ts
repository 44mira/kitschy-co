import { z } from 'zod';

export const addProductSchema = z.object({
	name: z.string().min(1),
	images: z
		.instanceof(File)
		.array(),
	category: z.number(),
	creators: z.array(z.string()).min(1),
	price: z.number().min(0),
	description: z.string().min(1),
	quantity: z.number().min(0)
});

export type AddProductSchema = typeof addProductSchema;
