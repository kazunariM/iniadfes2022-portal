<template>
	<main>
		<h1>入退室リーダー</h1>
		<div>
			<p class="count">現在の人数： {{ count }}</p>
		</div>
		<div>
			<ScanQRcodeComponent :timeout="timeout" @func="Register"></ScanQRcodeComponent>
			<Inya v-if="isOK">
				<p>{{ nickname }}</p>
				<p>{{ inorout }}</p>
			</Inya>
		</div>
		<p v-if="error" class="error">{{ error }}</p>
		<div>
			<img :src="img" alt="" />
		</div>
	</main>
</template>

<script>
import Inya from "~/components/Modal/Inya"
export default {
	components: {
		Inya,
	},
	asyncData({ $axios, redirect, params }) {
		return $axios
			.get("/api/v1/staff/pages/ReadQRinRoom/")
			.then((res) => {
				if (res.data.result === null) {
					redirect("/Staff/Signin/")
				} else if (!res.data.result) {
					redirect("/Staff/")
				} else {
					return $axios
						.get(`/api/v1/staff/existplaceid/${params.placeid}/`)
						.then((res) => {
							return {
								placeid: res.data.placeid,
								groupname: res.data.room.groupname,
								campus: res.data.room.campus ? "WELLB" : "INIAD",
								floor: res.data.room.floor,
							}
						})
						.catch(() => {
							redirect("/Staff/")
						})
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
			img: null,
			count: null,
			error: null,
		}
	},
	mounted() {
		this.getCount()
	},
	methods: {
		Register(url) {
			const qrid = url.match(/https:\/\/portal.iniadfes.com\/open\/([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/)
			if (qrid) {
				this.$axios({
					method: "post",
					url: `/api/v1/staff/roomqr/`,
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
						this.error = error.response.data.detail
						setTimeout(this.deleteError, this.timeout)
					})
			}
		},
		CloseInya() {
			this.nickname = ""
			this.inorout = ""
			this.isOK = false
			this.getCount()
		},
		getCount() {
			this.$axios.get(`/api/v1/staff/room/${this.placeid}/`).then((res) => {
				this.img = res.data.pop
				this.count = res.data.count
			})
		},
		deleteError() {
			this.error = null
		},
	},
}
</script>

<style lang="scss" scoped>
div {
	text-align: center;

	p {
		&.count {
			display: inline-block;
			font-size: 2em;
		}

		&.error {
			position: absolute;
			background-color: #831843;
			color: white;
			font-weight: bold;
			border-radius: 5px;
			padding: 0.5em;
			left: 50%;
			transform: translate(-50%, 5%);
			-webkit-transform: translate(-50%, 5%);
			font-size: 1.5em;

			&::before {
				content: "";
				position: absolute;
				left: 50%;
				transform: translate(-50%, -120%);
				-webkit-transform: translate(-50%, -120%);
				display: block;
				width: 0;
				height: 0;
				border-right: 15px solid transparent;
				border-bottom: 15px solid #831843;
				border-left: 15px solid transparent;
			}
		}
	}

	div {
		img {
			width: 80%;
			margin-left: auto;
			margin-right: auto;
			aspect-ratio: 4/3;
			background-color: black;
			border: solid 1px black;
		}
	}
}
</style>
