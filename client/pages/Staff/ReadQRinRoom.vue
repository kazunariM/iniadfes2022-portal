<template>
	<main>
		<h1>入退室リーダー</h1>
		<section v-if="!is_check">
			<h2>セットアップ</h2>
			<section v-if="send_placeid">
				<h3>場所IDを入力してください</h3>
				<p><input v-model="placeid" placeholder="1022021" required /><button @click="CheckPlaceid">送信</button></p>
			</section>
			<section v-if="!send_placeid">
				<h3>以下の内容に間違いがなく設置が完了したらOKを押してください</h3>
				<table>
					<tbody>
						<tr>
							<td>場所</td>
							<td>{{ groupname }}</td>
						</tr>
						<tr>
							<td>キャンパス</td>
							<td>{{ campus }}</td>
						</tr>
						<tr>
							<td>階</td>
							<td>{{ floor }}階</td>
						</tr>
					</tbody>
				</table>
				<p><button @click="Ready">OK</button></p>
			</section>
		</section>
		<section v-if="is_check">
			<ScanQRcodeComponent :timeout="timeout" @func="Register"></ScanQRcodeComponent>
			<Inya v-if="isOK">
				<p>{{ nickname }}</p>
				<p>{{ inorout }}</p>
			</Inya>
		</section>
	</main>
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
			is_check: false,
			placeid: "",
			send_placeid: true,
			groupname: "",
			campus: "",
			floor: "",
		}
	},
	methods: {
		CheckPlaceid() {
			this.$axios
				.get(`/api/v1/staff/existplaceid/${this.placeid}/`)
				.then((res) => {
					this.placeid = res.data.placeid
					this.groupname = res.data.room.groupname
					this.campus = res.data.room.campus ? "WELLB" : "INIAD"
					this.floor = res.data.room.floor
					this.$axios
						.get(`/api/v1/staff/readyroomqr_answer/${this.placeid}/`)
						.then(() => {
							this.send_placeid = false
						})
						.catch(() => {
							this.is_check = true
						})
				})
				.catch(() => {
					alert("場所IDが見つかりません")
				})
		},
		Ready() {
			this.$axios({
				method: "patch",
				url: `/api/v1/staff/readyroomqr_answer/${this.placeid}/`,
				headers: {
					"Content-Type": "application/json",
					"X-CSRFToken": this.$cookies.get("csrftoken"),
				},
				data: {
					ready: true,
				},
			}).then((res) => {
				if (res.data.ready) {
					this.is_check = true
				}
			})
		},
		Register(url) {
			const qrid = url.match(/https:\/\/portal.iniadfes.com\/open\/([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/)
			if (qrid) {
				this.$axios({
					method: "post",
					url: "/api/v1/staff/roomqr/",
					headers: {
						"Content-Type": "application/json",
						"X-CSRFToken": this.$cookies.get("csrftoken"),
					},
					data: {
						visitor: qrid[1],
						placeid: this.placeid,
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
