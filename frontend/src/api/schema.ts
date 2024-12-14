import { z } from 'zod';

export enum PRODUCT_STATUS {
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

export enum ORDER_STATUS {
	PENDING,
	PROCESSING,
	DELIVERED,
	CANCELLED
}

export enum PAYMENT_METHOD {
	COD,
	ONLINE
};

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
	status: PRODUCT_STATUS;
	category: CATEGORY;
	created_at: Date;
	updated_at: Date;
	creators: string[]; // uuid[]
};

export type CartItemSchema = {
	quantity: number;
	product: ProductSchema;
};

export type OrderItemSchema = CartItemSchema 

export type OrderSchema = {
	order_id: string; // uuid
	total: number;
	items: OrderItemSchema[];
	method: PAYMENT_METHOD;
	status: ORDER_STATUS;
	delivery_date: Date;
	created_at: Date;
	updated_at: Date;
	user: string; // uuid
};

export const signupSchema = z.object({
	email: z.string().email(),
	first_name: z.string().min(1).max(255),
	last_name: z.string().min(1).max(255),
	password1: z.string().min(6).max(255),
	password2: z.string().min(6).max(255),
	phone_number: z.string(), // should have a regex for phone number
	region: z.string().min(1).max(255),
	city: z.string().min(1).max(255),
	barangay: z.string().min(1).max(255),
	postal_code: z.string().min(1).max(255),
	detailed_address: z.string().min(1)
});
export type SignupSchema = typeof signupSchema;

export const loginSchema = z.object({}).merge(signupSchema.pick({ email: true, password1: true }));
export type LoginSchema = typeof loginSchema;
