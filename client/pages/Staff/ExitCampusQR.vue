<template>
	<main>
		<h1>赤羽台キャンパス 赤羽台祭 出口</h1>
		<div>
			<CampusQR mode="exit" @func="Register" />
			<Inya v-if="isOK">
				<p>{{ nickname }}</p>
				<p>退構</p>
			</Inya>
		</div>
		<p v-if="error" class="error">{{ error }}</p>
		<div>
			<img src="/akabanedaifes-pop.png" alt="" />
		</div>
	</main>
</template>

<script>
import CampusQR from "@/components/Staff/CampusQR"
import Inya from "~/components/Modal/Inya"
export default {
	components: {
		CampusQR,
		Inya,
	},
	asyncData({ $axios, redirect }) {
		return $axios
			.get("/api/v1/staff/pages/ExitCampusQR/")
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
			isOK: false,
			nickname: "",
			error: null,
		}
	},
	methods: {
		Register(url) {
			const qrid = url.match(/https:\/\/portal.iniadfes.com\/open\/([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/)
			if (qrid) {
				this.$axios({
					method: "post",
					url: "/api/v1/staff/campusqr/exit/",
					headers: {
						"Content-Type": "application/json",
						"X-CSRFToken": this.$cookies.get("csrftoken"),
					},
					data: {
						visitor: qrid[1],
					},
				})
					.then((res) => {
						this.isOK = true
						this.nickname = res.data.nickname
						setTimeout(this.CloseInya, 3000)
					})
					.catch((error) => {
						error = error.response.data.detail
						setTimeout(this.deleteError, 3000)
					})
			}
		},
		CloseInya() {
			this.nickname = ""
			this.isOK = false
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
		}
	}
}
</style>
