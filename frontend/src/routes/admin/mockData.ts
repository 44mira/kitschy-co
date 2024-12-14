import {type OrderSchema, ORDER_STATUS, PAYMENT_METHOD} from '@/api/schema';
import {mockCreators, mockProducts} from '@/routes/(user)/cafe/mockData';

const mockOrders : OrderSchema[] = [
    {
        order_id: 'b1d0c6e3-7b6c-4f5b-8b9c-6f6c1b0f7b5d',
        total: 65.98,
        items: [
            {
                quantity: 1,
                product: mockProducts[0]
            },
            {
                quantity: 2,
                product: mockProducts[1]
            }
        ],
        method: PAYMENT_METHOD.COD,
        status: ORDER_STATUS.DELIVERED,
        delivery_date: new Date('2024-03-15T14:30:00Z'),
        created_at: new Date('2024-03-10T11:00:00Z'),
        updated_at: new Date('2024-03-15T15:00:00Z'),
        user: '69a723cd-fc42-4522-b30b-eb7a2b20f23f'
    },
    {
        order_id: 'f3b2c1a4-8d6e-4f1a-9c8b-6f7c1a0f7b5d',
        total: 9.99,
        items: [
            {
                quantity: 1,
                product: mockProducts[2]
            }
        ],
        method: PAYMENT_METHOD.ONLINE,
        status: ORDER_STATUS.CANCELLED,
        delivery_date: new Date('2024-02-05T13:00:00Z'),
        created_at: new Date('2024-02-01T09:00:00Z'),
        updated_at: new Date('2024-02-05T15:30:00Z'),
        user: 'c9327099-1876-4710-b068-f6b706a814a0'
    },
    {
        order_id: 'd4e3f2c1-6b7c-5f4b-8b9c-6f6c1b0f7b5d',
        total: 45.0,
        items: [
            {
                quantity: 5,
                product: mockProducts[3]
            },
            {
                quantity: 1,
                product: mockProducts[4]
            },
            {
                quantity: 3,
                product: mockProducts[0]
            }
        ],
        method: PAYMENT_METHOD.COD,
        status: ORDER_STATUS.PENDING,
        delivery_date: new Date('2024-03-20T10:00:00Z'),
        created_at: new Date('2024-03-15T08:30:00Z'),
        updated_at: new Date('2024-03-15T09:45:00Z'),
        user: '69a723cd-fc42-4522-b30b-eb7a2b20f23f'
    }
];