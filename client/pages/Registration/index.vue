<template>
	<main>
		<section>
			<div class="bg-gray-200 rounded-md w-full p-1 px-2 mt-2">
				<h1 class="text-sm text-gray-800">来場者登録</h1>
			</div>
		</section>
		<RegistrationForm />
	</main>
</template>

<script>
import RegistrationForm from "~/components/Registration/RegistrationForm"
export default {
	components: { RegistrationForm },
	layout: "portal",
	fetch({ store, $axios }) {
		return $axios.get("/api/v1/namecards").then((res) => {
			store.dispatch("Registration/data/addAction", res.data)
		})
	},
}
</script>
