import pinkFlower from '$lib/assets/users/pink_flower.png';
import greenButterfly from '$lib/assets/users/green_butterfly.png';
import blueStar from '$lib/assets/users/blue_star.png';

export type HeaderCard = {
	bgColor: string;
	bgIcon: string;
	headerColor: string;
	headerContent: string;
	bgContent: string;
};

const HeaderCardContents: HeaderCard[] = [
	{
		bgColor: '#fc81ae',
		bgIcon: pinkFlower,
		headerColor: '#EF216D',
		headerContent: 'who we are',
		bgContent: `
Welcome to kitschy co. 🌟, where charm meets convenience in the most delightful way! Step into
our vibrant haven 🏡, where every corner is filled with delicious aromas from our café ☕️ and
bakery 🥐, a treasure trove of unique finds in our mini mart 🛍️, and an array of quirky, fun
merchandise ✨ that adds a touch of whimsy to your day.
`
	},
	{
		bgColor: '#abd6f7',
		bgIcon: blueStar,
		headerColor: '#5EB5E3',
		headerContent: 'our mission',
		bgContent: `
At kitschy co. ✨, our mission is to be the ultimate destination where vibrant
community 🌈 and unique charm 🌟 converge. We strive to provide a delightful
experience through our café ☕️ and pastries 🥐, curated mini mart 🛍️, and wide-ranging
merchandise 🎀.
`
	},
	{
		bgColor: '#d7f77e',
		bgIcon: greenButterfly,
		headerColor: '#B0D253',
		headerContent: 'our vision',
		bgContent: `
At kitschy co. 🌟, our goal is to create a unique experience and a welcoming
environment 🏡 that will entice our customers' to return time and time again. We aim
to be a beloved local hub 💝 that combines exceptional drinks ☕️ and pastries 🥮,
whimsical merchandise 🎪, and a warm atmosphere 🌈.
`
	}
];

export default HeaderCardContents;
