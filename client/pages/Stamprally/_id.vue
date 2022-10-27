<template>
	<div>
		<div class="stamprally">
			<canvas ref="canvas"></canvas>
		</div>
		<div class="stamps">
			<table>
				<tbody>
					<tr>
						<th></th>
						<th>場所</th>
					</tr>
					<tr v-for="(stamp, index) in stamps" :key="index">
						<td>{{ stamp.serial }}</td>
						<td>{{ stamp.room.groupname }}</td>
					</tr>
				</tbody>
			</table>
		</div>
	</div>
</template>

<script>
export default {
	layout: "portal",
	middleware: "opened",
	asyncData({ $axios, params, redirect, $cookies }) {
		return $axios
			.get(`/api/v1/stampsheet/${params.id}/`)
			.then((res1) => {
				return $axios.get(`/api/v1/stamps/${params.id}/`).then((res2) => {
					return $axios.get(`/api/v1/stamprally/${$cookies.get("userid")}/${params.id}/`).then((res3) => {
						return {
							title: res1.data.title,
							sheet: res1.data.background,
							stamps: res2.data,
							got_stamp: res3.data.got_stamp,
						}
					})
				})
			})
			.catch(() => {
				redirect("/404")
			})
	},
	data() {
		return {
			canvas: null,
			context: null,
			imgs: [],
		}
	},
	mounted() {
		this.$nuxt.$emit("setTitle", this.title)
		this.canvas = this.$refs.canvas
		this.canvas.width = 1170
		this.canvas.height = 2532
		this.context = this.canvas.getContext("2d")
		let img = new Image()
		img.src = this.sheet
		this.context.drawImage(img, 0, 0, this.canvas.width, this.canvas.height)
		img = null
		for (let i = 0; i < this.stamps.length; i++) {
			for (const stamp of this.got_stamp) {
				if (this.stamps[i].serial === stamp.serial) {
					this.stamps[i].img = stamp.img
					let img = new Image()
					img.src = stamp.img
					this.context.drawImage(img, 0, 0, this.canvas.width, this.canvas.height)
					img = null
					break
				}
			}
		}
	},
}
</script>

<style lang="scss" scoped>
div.stamprally {
	canvas {
		width: 80%;
		height: 80%;
		margin: auto;
	}
}

div.stamps {
	table {
		margin: auto;
		margin-top: 2em;
		background-color: #ccc;
		width: 80%;
	}

	th,
	td {
		padding: 1em;
		margin: 0.5em;
		background-color: #eee;
		text-align: center;

		img {
			width: 20vw;
		}

		p {
			display: inline;
			margin: auto;
		}
	}
}
</style>
