<template>
	<main>
		<section>
			<div class="bg-gray-200 rounded-md w-full p-1 px-2 mt-2">
				<h1 class="text-sm text-gray-800">来場者登録 完了</h1>
			</div>
		</section>
		<p>来場者登録をしていただきありがとうございます。</p>
		<table>
			<tbody>
				<tr>
					<td>ニックネーム</td>
					<td>{{ nickname }}</td>
				</tr>
				<tr>
					<td>二次元コード</td>
					<td v-if="qr"><img :src="qr" alt="受付用二次元コード" /></td>
					<td v-else>読み込み中</td>
				</tr>
			</tbody>
		</table>
		<p>当日はこちらの二次元コードを受付でご提示ください。</p>
		<p>二次元コードはご登録されたメールアドレス宛に送信しております。</p>
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
