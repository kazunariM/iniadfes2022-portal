<template>
	<RegistrationForm />
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
	mounted() {
		this.$nuxt.$emit("setTitle", "来場者登録")
	},
}
</script>
