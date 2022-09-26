<template>
	<article>
		<ScanQRcodeComponent :timeout="timeout" @func="Register"></ScanQRcodeComponent>
		<Inya v-if="isOK">
			<p>{{ nickname }}</p>
			<p>{{ inorout }}</p>
		</Inya>
	</article>
</template>

<script>
import Inya from "~/components/Modal/Inya"
export default {
	components: {
		Inya,
	},
	asyncData({ $axios, redirect }) {
		return $axios
			.get("/api/v1/staff/pages/ReadQRinRoom/")
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
			nickname: "",
			inorout: "",
			isOK: false,
			timeout: 3000,
		}
	},
	methods: {
		Register(url) {
			const qrid = url.match(/https:\/\/portal.iniadfes.com\/open\/([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/)
			if (qrid) {
				this.$axios({
					method: "post",
					url: `${this.$config.API_URL}/api/v1/staff/roomqr/`,
					headers: {
						"Content-Type": "application/json",
						"X-CSRFToken": this.$cookies.get("csrftoken"),
					},
					data: {
						visitor: qrid[1],
						placeid: 1022021,
					},
				})
					.then((res) => {
						this.nickname = res.data.nickname
						this.inorout = res.data.inorout ? "入室" : "退室"
						this.isOK = true
						setTimeout(this.CloseInya, this.timeout)
					})
					.catch((error) => {
						alert(JSON.stringify(error.response))
					})
			}
		},
		CloseInya() {
			this.nickname = ""
			this.inorout = ""
			this.isOK = false
		},
	},
}
</script>

<style lang="scss" scoped></style>
