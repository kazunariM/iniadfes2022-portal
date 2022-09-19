<template>
	<article>
		<h1>スタッフメニュー</h1>
	</article>
</template>

<script>
export default {
	asyncData({ $axios, route, redirect }) {
		return $axios
			.get(`/api/v1/staff/check/`)
			.then((res) => {
				if (!res.data.is_authenticated) {
					redirect("/Staff/Signin")
				}
			})
			.catch(() => {
				redirect("/")
			})
	},
}
</script>

<style lang="scss" scoped></style>
