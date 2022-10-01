<template>
	<main>
		<h1>来場者登録 完了</h1>
		<p>来場者登録をしていただきありがとうございます。</p>
		<table>
			<tbody>
				<tr>
					<td>ニックネーム</td>
					<td>{{ nickname }}</td>
				</tr>
				<tr>
					<td>QRコード</td>
					<td v-if="qr"><img :src="qr" alt="受付用QRコード" /></td>
					<td v-else>読み込み中</td>
				</tr>
			</tbody>
		</table>
		<p>当日はこちらのQRコードを受付でご提示ください。</p>
		<p>QRコードはご登録されたメールアドレス宛に送信しております。</p>
	</main>
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
}
</script>

<style lang="scss" scoped></style>
