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

export type CartItemSchema = {
	quantity: number;
	product: ProductSchema;
};

