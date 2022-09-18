<template>
	<article>
		<h1>来場者登録 完了</h1>
		<p>来場者登録をしていただきありがとうございます。</p>
		<table>
			<tr>
				<td>ニックネーム</td>
				<td>{{ nickname }}</td>
			</tr>
			<tr>
				<td>QRコード</td>
				<td><img :src="qr" alt="受付用QRコード" /></td>
			</tr>
		</table>
		<p>当日はこちらのQRコードを受付でご提示ください。</p>
		<p>QRコードはご登録されたメールアドレス宛に送信しております。</p>
	</article>
</template>

<script>
import QRCode from "qrcode"
export default {
	neme: "Complated",
	data() {
		return {
			nickname: "",
			id: "",
			qr: null,
		}
	},
	created() {
		this.$axios.get(`/api/v1/complete/${this.$route.query.id}/`).then((res) => {
			this.nickname = res.data.nickname
			this.id = res.data.management_uuid
			QRCode.toDataURL(this.id, { width: 400 }).then((code) => {
				this.qr = code
			})
		})
	},
}
</script>

<style lang="scss" scoped></style>
