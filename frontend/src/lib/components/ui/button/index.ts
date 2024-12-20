import { type VariantProps, tv } from 'tailwind-variants';
import type { Button as ButtonPrimitive } from 'bits-ui';
import Root from './button.svelte';

const buttonVariants = tv({
	base: 'ring-offset-background focus-visible:ring-ring inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50',
	variants: {
		variant: {
			default: 'bg-primary text-primary-foreground hover:bg-primary/90',
			destructive: 'bg-destructive text-destructive-foreground hover:bg-destructive/90',
			outline: 'border-input bg-background hover:bg-accent hover:text-accent-foreground border',
			secondary: 'bg-secondary text-secondary-foreground hover:bg-secondary/80',
			ghost: '',
			link: 'text-primary underline-offset-4 hover:underline',
			tab: 'bg-background rounded-xl rounded-b-none font-giphursSC text-lg',
			cafe: 'rounded-none bg-brand-base text-[#BF3A0E] font-giphursSC font-bold text-2xl drop-shadow-xl',
			big: 'font-gladiola bg-brand-purple hover:bg-brand-purple-m active:bg-brand-purple-d text-6xl',
			membership:
				'capitalize bg-[#696969] text-white font-giphursSC font-light text-2xl drop-shadow-xl'
		},
		size: {
			default: 'h-10 px-4 py-2',
			sm: 'h-9 rounded-md px-3',
			lg: 'h-11 rounded-md px-8',
			icon: 'h-10 w-10'
		}
	},
	defaultVariants: {
		variant: 'default',
		size: 'default'
	}
});

type Variant = VariantProps<typeof buttonVariants>['variant'];
type Size = VariantProps<typeof buttonVariants>['size'];

type Props = ButtonPrimitive.Props & {
	variant?: Variant;
	size?: Size;
};

type Events = ButtonPrimitive.Events;

export {
	Root,
	type Props,
	type Events,
	//
	Root as Button,
	type Props as ButtonProps,
	type Events as ButtonEvents,
	buttonVariants
};
