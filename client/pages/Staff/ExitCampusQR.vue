<template>
	<main>
		<CampusQR mode="exit" @func="Register" />
		<Inya v-if="isOK">
			<p>{{ nickname }}</p>
			<p>退構</p>
		</Inya>
	</main>
</template>

<script>
import CampusQR from "@/components/Staff/CampusQR"
import Inya from "~/components/Modal/Inya"
export default {
	components: {
		CampusQR,
		Inya,
	},
	asyncData({ $axios, redirect }) {
		return $axios
			.get("/api/v1/staff/pages/ExitCampusQR/")
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
	data() {
		return {
			isOK: false,
			nickname: "",
		}
	},
	methods: {
		Register(url) {
			const qrid = url.match(/https:\/\/portal.iniadfes.com\/open\/([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/)
			this.$axios({
				method: "post",
				url: "/api/v1/staff/campusqr/Exit/",
				headers: {
					"Content-Type": "application/json",
					"X-CSRFToken": this.$cookies.get("csrftoken"),
				},
				data: {
					visitor: qrid[1],
				},
			})
				.then((res) => {
					this.isOK = true
					this.nickname = res.data.nickname
					setTimeout(this.CloseInya, 3000)
				})
				.catch((error) => {
					alert(error.response.data.detail)
				})
		},
		CloseInya() {
			this.nickname = ""
			this.isOK = false
		},
	},
}
</script>
