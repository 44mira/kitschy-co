enum Status {
	READY,
	ARCHIVED
}

enum Category {
	MERCH,
	PRINT,
	CAFE,
	MINIMART,
	WORKSHOP
}

interface ProductImagesSchema {
	img_url: string;
	alt_desc: string;
}

interface ProductSchema {
	product_id: string; // uuid
	images: ProductImagesSchema[];
	name: string;
	desc: string;
	price: number;
	quantity: number;
	status: Status;
	category: Category;
	created_at: Date;
	updated_at: Date;
	creators: string[]; // uuid[]
}
