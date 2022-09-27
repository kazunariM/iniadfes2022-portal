<template>
	<article></article>
</template>

<script>
export default {
	asyncData({ $axios, redirect }) {
		return $axios
			.get("/api/v1/staff/pages/CampusQR/")
			.then((res) => {
				if (res.data.result === null) {
					redirect("/Staff/Signin/")
				} else if (!res.data.result) {
					redirect("/Staff/")
				}
			})
			.catch(() => {
				redirect("/")
			})
	},
}
</script>
