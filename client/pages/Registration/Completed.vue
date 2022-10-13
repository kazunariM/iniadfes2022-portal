<template>
	<main>
		<article>
			<div class="bg-gray-200 rounded-md w-full p-1 px-2 mt-2">
				<h1 class="text-sm text-gray-800">来場者登録 完了</h1>
			</div>

			<p>来場者登録していただきありがとうございます。</p>

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
			</div>

			<p>当日はこちらの二次元コードを受付でご提示ください。二次元コードはご登録されたメールアドレス宛に送信しております。</p>
		</article>
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

<style lang="scss" scoped>
article {
	p {
		margin: 1em auto;
	}
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
	}
}
</style>
