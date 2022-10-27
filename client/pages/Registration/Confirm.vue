<template>
	<ConfirmComponent />
</template>

<script>
import ConfirmComponent from "~/components/Registration/ConfirmComponent"
export default {
	components: { ConfirmComponent },
	layout: "portal",
	middleware: "registration",
	mounted() {
		this.$nuxt.$emit("setTitle", "来場者登録")
	},
}
</script>
