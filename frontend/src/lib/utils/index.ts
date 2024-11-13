export const toImageUrl = (processedImagePath: string) =>
	`url('${processedImagePath.slice(1).replaceAll('\\', '/')}')`;
