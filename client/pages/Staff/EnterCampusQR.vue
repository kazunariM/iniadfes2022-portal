<template>
	<main>
		<CampusQR mode="enter" @func="Register" />
	</main>
</template>

<script>
import CampusQR from "@/components/Staff/CampusQR"
export default {
	components: {
		CampusQR,
	},
	asyncData({ $axios, redirect }) {
		return $axios
			.get("/api/v1/staff/pages/EnterCampusQR/")
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
	methods: {
		Register(url) {
			const qrid = url.match(/https:\/\/portal.iniadfes.com\/open\/([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/)
			this.$axios({
				method: "post",
				url: "/api/v1/staff/campusqr/Enter/",
				headers: {
					"Content-Type": "application/json",
					"X-CSRFToken": this.$cookies.get("csrftoken"),
				},
				data: {
					visitor: qrid[1],
				},
			}).then((res) => {
				alert(res.data.inorout)
			})
		},
	},
}
</script>
