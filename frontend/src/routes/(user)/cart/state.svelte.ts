import mockProducts from './mockData';
import { type CartItemSchema } from '@/api/schema';

export const cart: CartItemSchema[] = $state(mockProducts);
