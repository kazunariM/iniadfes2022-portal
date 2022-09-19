<template>
	<article>
		<form @submit.prevent="signin">
			<p v-if="error">{{ error }}</p>
			<input v-model="username" type="text" placeholder="ユーザー名" />
			<input v-model="password" type="password" placeholder="パスワード" />
			<button type="submit">送信</button>
		</form>
	</article>
</template>

<script>
export default {
	asyncData({ $axios, $cookies, route, redirect }) {
		return $axios
			.get(`/api/v1/staff/check/`)
			.then((res) => {
				if (res.data.is_authenticated) {
					redirect("/Staff/")
				} else {
					return $axios.get("/api/v1/initial/").then((res) => {
						return {
							csrftoken: $cookies.set("csrftoken", res.data.csrftoken, { path: "/", maxAge: 60 * 60 }),
						}
					})
				}
			})
			.catch(() => {
				redirect("/")
			})
	},
	data() {
		return {
			username: "",
			password: "",
			error: "",
		}
	},
	methods: {
		signin() {
			this.$axios({
				method: "post",
				url: "/api/v1/staff/login/",
				headers: {
					"Content-Type": "application/json",
					"X-CSRFToken": this.$cookies.get("csrftoken"),
				},
				data: {
					username: this.username,
					password: this.password,
				},
			})
				.then(() => {
					window.location.href = "/Staff"
				})
				.catch((err) => {
					this.error = err.response.detail[0]
				})
		},
	},
}
</script>

<style lang="scss" scoped></style>
