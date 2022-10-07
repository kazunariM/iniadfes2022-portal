<template>
	<main>
		<h1>ネームカードお渡し</h1>
		<ScanQRcodeComponent :timeout="2000" @func="reception"></ScanQRcodeComponent>
		<p v-if="msg">{{ msg }}</p>
		<div v-if="step === 1">
			<img :src="namecard" alt="" />
		</div>
		<div v-if="step === 2">
			<p>{{ nickname }}</p>
			<p>{{ identifying }}</p>
			<p @click="completed">お渡し完了</p>
		</div>
	</main>
</template>

<script>
export default {
	asyncData({ $axios, redirect }) {
		return $axios
			.get("/api/v1/staff/pages/HandoverNamecard/")
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
			msg: "メール配信されている事前配信二次元コードを読んでください",
			step: 0,
			management_uuid: null,
			namecard: null,
			nickname: null,
			identifying: null,
		}
	},
	methods: {
		reset() {
			this.msg = "メール配信されている事前配信二次元コードを読んでください"
			this.step = 0
			this.management_uuid = null
			this.namecard = null
			this.nickname = null
			this.identifying = null
		},
		reception(qr) {
			if (this.step === 0) {
				this.$axios.get(`/api/v1/staff/reception/confirmvisitor/${qr}/`).then((res) => {
					this.management_uuid = qr
					this.msg = "該当するデザインのネームカードを1枚取り二次元コードを読み込んでください"
					this.namecard = res.data.design.img
					this.step = 1
				})
			} else if (this.step === 1) {
				const qrid = qr.match(/https:\/\/portal.iniadfes.com\/open\/([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/)
				this.$axios({
					method: "post",
					url: "api/v1/staff/reception/selectnamecard/",
					headers: {
						"Content-Type": "application/json",
						"X-CSRFToken": this.$cookies.get("csrftoken"),
					},
					data: {
						management_uuid: this.management_uuid,
						userid: qrid[1],
					},
				}).then((res) => {
					this.nickname = res.data.nickname
					this.identifying = res.data.identifying
					this.msg = "ニックネームを記入しお渡しし完了を押してください。"
					this.step = 2
				})
			}
		},
		completed() {
			if (this.step === 2) {
				this.$axios({
					method: "patch",
					url: `/api/v1/staff/reception/handover/${this.management_uuid}/`,
					headers: {
						"Content-Type": "application/json",
						"X-CSRFToken": this.$cookies.get("csrftoken"),
					},
					data: {
						is_handedover: true,
					},
				}).then(() => {
					this.msg = "完了"
					this.step = 3
					setTimeout(this.reset, 2000)
				})
			}
		},
	},
}
</script>

<style lang="scss" scoped>
img {
	width: 300px;
}
</style>
