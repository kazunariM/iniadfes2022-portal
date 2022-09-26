<template>
	<div>
		<HeaderView />
		<h2>来場者登録フォーム</h2>
		<RegistrationForm />
	</div>
</template>

<script>
import RegistrationForm from "~/components/Registration/RegistrationForm"
export default {
	components: { RegistrationForm },
	fetch({ store, $axios }) {
		return $axios.get("/api/v1/namecards").then((res) => {
			store.dispatch("Registration/data/addAction", res.data)
		})
	},
}
</script>
