import { CATEGORY } from '@/api/schema';

export const icons = {
	add: 'mdi:add',
	delete: 'mdi:delete-forever-outline',
	save: 'mdi:content-save-outline',
	close: 'mdi:close',
	archive: 'mdi:archive-arrow-down-outline'
};

export const creators = [
	{ uuid: '69a723cd-fc42-4522-b30b-eb7a2b20f23f', name: 'admin1', color: '#ee1768' },
	{ uuid: 'c9327099-1876-4710-b068-f6b706a814a0', name: 'admin2', color: '#5eb5e3' },
	{ uuid: '550e8400-e29b-41d4-a716-446655440000', name: 'admin3', color: '#b0d253' }
];

export const categories = [
	{ value: CATEGORY.MERCH, label: 'Merchandise', color: '#4D1078' },
	{ value: CATEGORY.PRINT, label: "Misbeek's Printing", color: '#ffabff' },
	{ value: CATEGORY.CAFE, label: 'Cafe & Pastries', color: '#FB7A4F' },
	{ value: CATEGORY.MINIMART, label: 'Mini-mart', color: '#F9F871' },
	{ value: CATEGORY.WORKSHOP, label: 'Workshop', color: '#32beaf' }
];

export const darkTextCategories = [CATEGORY.PRINT, CATEGORY.MINIMART];
