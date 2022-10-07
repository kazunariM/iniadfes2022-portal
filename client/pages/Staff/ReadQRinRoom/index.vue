<template>
	<main>
		<article>
			<h1>場所ID確認</h1>
			<section v-if="step === 1">
				<h2>場所IDを入力してください</h2>
				<p><input v-model="placeid" type="text" placeholder="1022021" required /><button @click="CheckPlaceid">確認</button></p>
			</section>
			<section v-if="step === 2">
				<h2>間違いがないか確認してください</h2>
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
				<p><button @click="Ready">OK</button></p>
			</section>
		</article>
	</main>
</template>

<script>
export default {
	asyncData({ $axios, redirect, params }) {
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
			placeid: null,
			campus: null,
			floor: null,
			groupname: null,
			step: 1,
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
							this.step = 2
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
					this.$router.replace(`${this.placeid}/`)
				}
			})
		},
	},
}
</script>
