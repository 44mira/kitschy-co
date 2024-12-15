<script lang="ts">
	let user = {
		photo: "https://github.com/shadcn.png",
		name: "Kitschy Co.",
		email: "kitschyco@gmail.com",
		contact: "123 456 7890",
		address: "Philippines",
	};

	// Temporary state for editing
	let form = { ...user };

	// Save changes by updating the user object
	const saveChanges = () => {
		user = { ...form }; // Update user with form values
		alert("Changes saved successfully!");
	};
</script>

<div class="bg-brand-purple-l flex items-center justify-center min-h-screen px-12">
	<div class="bg-white rounded-lg shadow-lg p-6 w-full sm:max-w-md md:max-w-lg lg:max-w-xl">
		<!-- Header -->
		<div class="flex items-center space-x-4 mb-6">
			<!-- svelte-ignore a11y_img_redundant_alt -->
			<img src={user.photo} alt="Profile Picture" class="w-16 h-16 rounded-full object-cover" />
			<div>
				<h1 class="text-xl md:text-2xl font-semibold">{user.name}</h1>
				<p class="text-gray-500 text-sm md:text-base">{user.email}</p>
			</div>
		</div>

		<!-- Personal Info Form -->
		<div class="space-y-4">
			<div>
				<label for="name" class="block text-sm font-medium text-gray-700">Name</label>
				<input
					type="text"
					id="name"
					bind:value={form.name}
					class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm md:text-base"
				/>
			</div>

			<div>
				<label for="email" class="block text-sm font-medium text-gray-700">Email</label>
				<input
					type="email"
					id="email"
					bind:value={form.email}
					class="mt-1 block w-full border-gray-300 rounded-md shadow-sm sm:text-sm md:text-base"
				/>
			</div>

			<div>
				<label for="contact" class="block text-sm font-medium text-gray-700">Mobile Number</label>
				<input
					type="text"
					id="contact"
					bind:value={form.contact}
					class="mt-1 block w-full border-gray-300 rounded-md shadow-sm sm:text-sm md:text-base"
				/>
			</div>

			<div>
				<label for="address" class="block text-sm font-medium text-gray-700">Location</label>
				<input
					type="text"
					id="address"
					bind:value={form.address}
					class="mt-1 block w-full border-gray-300 rounded-md shadow-sm sm:text-sm md:text-base"
				/>
			</div>
		</div>

		<!-- Save Button -->
		<div class="mt-6">
			<button
				on:click={saveChanges}
				class="w-full bg-brand-purple hover:bg-brand-purple-d text-white font-medium py-2 px-4 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
			>
				Save Changes
			</button>
		</div>
	</div>
</div>
