import { z } from 'zod';

export enum STATUS {
	READY,
	ARCHIVED
}

export enum CATEGORY {
	MERCH,
	PRINT,
	CAFE,
	MINIMART,
	WORKSHOP
}

export type ProductImagesSchema = {
	img_url: string;
	alt_desc: string;
};

export type ProductSchema = {
	product_id: string; // uuid
	images: ProductImagesSchema[];
	name: string;
	desc: string;
	price: number;
	quantity: number;
	status: STATUS;
	category: CATEGORY;
	created_at: Date;
	updated_at: Date;
	creators: string[]; // uuid[]
};

export const signupSchema = z.object({
	firstname: z.string().min(1).max(255),
	lastname: z.string().min(1).max(255),
	email: z.string().email(),
	phoneNo: z.string(), // should have a regex for phone number
	password: z.string().min(6).max(255),
	confirmPassword: z.string().min(6).max(255),
	region: z.string().min(1).max(255),
	city: z.string().min(1).max(255),
	barangay: z.string().min(1).max(255),
	postalCode: z.string().min(1).max(255),
	detailedAddress: z.string().min(1)
});
export type SignupSchema = typeof signupSchema;

export const loginSchema = z.object({}).merge(signupSchema.pick({ email: true, password: true }));
export type LoginSchema = typeof loginSchema;
