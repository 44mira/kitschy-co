import { type ProductSchema, STATUS, CATEGORY } from '../../../api/schema';

const mockCreators = [
	'69a723cd-fc42-4522-b30b-eb7a2b20f23f',
	'c9327099-1876-4710-b068-f6b706a814a0'
];

const mockProducts: ProductSchema[] = [
	{
		product_id: 'bd58c563-0af3-4eee-bdd8-8716e842f7ac',
		images: [
			{
				img_url: 'https://example.com/images/product1.jpg',
				alt_desc: 'A sleek ceramic mug with a modern design'
			}
		],
		name: 'Modern Ceramic Mug',
		desc: 'A stylish ceramic mug, perfect for coffee lovers.',
		price: 15.99,
		quantity: 120,
		status: STATUS.READY,
		category: CATEGORY.CAFE,
		created_at: new Date('2024-01-15T10:30:00Z'),
		updated_at: new Date('2024-02-20T08:15:00Z'),
		creators: [mockCreators[0]]
	},
	{
		product_id: '8327e528-c4e2-41ed-9e01-10ab2b03b868',
		images: [
			{
				img_url: 'https://example.com/images/product2.jpg',
				alt_desc: 'A vibrant abstract art print'
			}
		],
		name: 'Abstract Art Print',
		desc: 'A beautiful abstract art print, ideal for home decor.',
		price: 45.0,
		quantity: 50,
		status: STATUS.READY,
		category: CATEGORY.PRINT,
		created_at: new Date('2024-02-01T12:00:00Z'),
		updated_at: new Date('2024-03-05T09:45:00Z'),
		creators: [mockCreators[1]]
	},
	{
		product_id: '36fdd7aa-fb09-4fe2-b8c2-b3b841526e18',
		images: [
			{
				img_url: 'https://example.com/images/product3.jpg',
				alt_desc: 'A handy multipurpose keychain'
			}
		],
		name: 'Multipurpose Keychain',
		desc: 'A durable keychain with bottle opener and LED light.',
		price: 9.99,
		quantity: 200,
		status: STATUS.ARCHIVED,
		category: CATEGORY.MERCH,
		created_at: new Date('2023-11-20T14:00:00Z'),
		updated_at: new Date('2024-01-10T10:10:00Z'),
		creators: mockCreators
	},
	{
		product_id: 'ad3da2ba-168a-4d3e-9744-6f9723609783',
		images: [
			{
				img_url: '',
				alt_desc: 'A pack of organic whole bean coffee'
			}
		],
		name: 'Organic Coffee Beans',
		desc: 'Premium organic coffee beans sourced from Colombia.',
		price: 25.99,
		quantity: 75,
		status: STATUS.READY,
		category: CATEGORY.CAFE,
		created_at: new Date('2024-02-10T09:00:00Z'),
		updated_at: new Date('2024-03-01T11:20:00Z'),
		creators: [mockCreators[0]]
	},
	{
		product_id: 'ac032632-f5f8-41e4-be9f-1154f88a0948',
		images: [
			{
				img_url: 'https://example.com/images/product5.jpg',
				alt_desc: 'A creative DIY candle-making kit'
			}
		],
		name: 'DIY Candle-Making Kit',
		desc: 'A fun and creative kit for making your own candles.',
		price: 30.0,
		quantity: 40,
		status: STATUS.READY,
		category: CATEGORY.WORKSHOP,
		created_at: new Date('2024-01-05T13:15:00Z'),
		updated_at: new Date('2024-02-25T15:00:00Z'),
		creators: [mockCreators[1]]
	}
];

export default mockProducts;
