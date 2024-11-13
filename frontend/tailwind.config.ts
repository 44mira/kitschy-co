import { fontFamily } from "tailwindcss/defaultTheme";
import type { Config } from 'tailwindcss';

const config = {
	darkMode: ["class"],
	content: ["./src/**/*.{html,js,svelte,ts}"],
	safelist: ["dark"],
	theme: {
		container: {
			center: true,
			padding: "2rem",
			screens: {
				"2xl": "1400px"
			}
		},
		extend: {
			colors: {
				border: "hsl(var(--border) / <alpha-value>)",
				input: "hsl(var(--input) / <alpha-value>)",
				ring: "hsl(var(--ring) / <alpha-value>)",
				background: "hsl(var(--background) / <alpha-value>)",
				foreground: "hsl(var(--foreground) / <alpha-value>)",
				primary: {
					DEFAULT: "hsl(var(--primary) / <alpha-value>)",
					foreground: "hsl(var(--primary-foreground) / <alpha-value>)"
				},
				secondary: {
					DEFAULT: "hsl(var(--secondary) / <alpha-value>)",
					foreground: "hsl(var(--secondary-foreground) / <alpha-value>)"
				},
				destructive: {
					DEFAULT: "hsl(var(--destructive) / <alpha-value>)",
					foreground: "hsl(var(--destructive-foreground) / <alpha-value>)"
				},
				muted: {
					DEFAULT: "hsl(var(--muted) / <alpha-value>)",
					foreground: "hsl(var(--muted-foreground) / <alpha-value>)"
				},
				accent: {
					DEFAULT: "hsl(var(--accent) / <alpha-value>)",
					foreground: "hsl(var(--accent-foreground) / <alpha-value>)"
				},
				popover: {
					DEFAULT: "hsl(var(--popover) / <alpha-value>)",
					foreground: "hsl(var(--popover-foreground) / <alpha-value>)"
				},
				card: {
					DEFAULT: "hsl(var(--card) / <alpha-value>)",
					foreground: "hsl(var(--card-foreground) / <alpha-value>)"
				},
				admin: {
					pink: '#EE1768',
					blue: '#5EB5E3',
					green: '#B0D253',
				},

				admin_background: {
					overview: '#FFD9E7',
                    product_list: '#D3F0FF',
					order_tracker: '#F6FFDE',
				},
				
				brand: {
					purple: {
						DEFAULT: '#804B7A',
						d: '#663C62',
						m: '#A883A7',
						l: '#C8B5D5'
					},
				base: '#FFFADE',
				},
                
                admin_item: {
					creators: {
						admin2: '#804B7A',
						admin3: '#B0D253',
					},
					button: {
						cancel_stroke: '#9F9F9F',
                        delete_stroke: '#FF1D1D',
						blue_fill: '#99D8FA',
						blue_stroke: '#126A99',
					},	
				base: '#FFF5FE',
				overlay_bg: '#FFFFFF',
				},
                
                success_toast: {
                    success_fill: '#F6FFDE', 
					success_stroke: '#1A6C0E',
				},

                category_methods: {
					mart_yellow: '#F9F871',
					pastries_yellow: '#FB7A4F',
                    printing_pink: 'F1ABFF', 
				},

				status: {
					delivered: '#008000',
					shipped: '#F9F871',
					cancelled: '#FF1D1D'	
				}
			},
			borderRadius: {
				lg: "var(--radius)",
				md: "calc(var(--radius) - 2px)",
				sm: "calc(var(--radius) - 4px)"
			},
			fontFamily: {
				sans: [...fontFamily.sans]
			}
		}
	},
} satisfies Config;

export default config;
