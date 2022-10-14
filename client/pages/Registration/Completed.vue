<template>
	<div>
		<p>来場者登録していただきありがとうございます。当日はこちらの二次元コードを受付でご提示ください。二次元コードはご登録されたメールアドレス宛に送信しております。</p>

		<div class="content">
			<section>
				<h2>ニックネーム</h2>
				<p>{{ nickname }}</p>
			</section>

			<section>
				<h2>二次元コード</h2>
				<p v-if="qr"><img :src="qr" alt="受付用二次元コード" /></p>
				<p v-else>読み込み中</p>
			</section>

			<div class="please">
				<p>来場者1名1名それぞれにネームカードを発行いたします。そのため複数人でご来場される場合は<span style="font-weight: bolder; font-size: 1.2em">ご来場される人数分の登録をお願いいたします</span>。メールアドレスは同じもので構いません。ぜひ皆様でそれぞれ楽しいニックネームをお付けください。</p>
			</div>
		</div>
	</div>
</template>

<script>
import QRCode from "qrcode"
export default {
	layout: "portal",
	neme: "Complated",
	asyncData({ $axios, route, redirect }) {
		return $axios
			.get(`/api/v1/complete/${route.query.id}/`)
			.then((res) => {
				return {
					nickname: res.data.nickname,
					id: res.data.management_uuid,
				}
			})
			.catch(() => {
				redirect("/")
			})
	},
	data() {
		return {
			qr: null,
		}
	},
	created() {
		QRCode.toDataURL(this.id, { width: 400 }).then((code) => {
			this.qr = code
		})
	},
	mounted() {
		this.$nuxt.$emit("setTitle", "来場者登録 完了")
	},
}
</script>

<style lang="scss" scoped>
div.content {
	background-color: #ccc;
	padding: 3%;
	border-radius: 7px;

	section {
		background-color: #eee;
		margin-bottom: 3%;
		padding: 1em;
		border-radius: 7px;
	}

	div.please {
		margin-bottom: 3%;
		width: 100%;
		padding: 1em;
		border-radius: 7px;
		color: white;
		background-color: rgb(217, 119, 6);
	}
}
</style>
