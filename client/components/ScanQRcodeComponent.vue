<template>
	<section>
		<p v-if="NoPermission">カメラの利用を許可してください</p>
		<p v-if="Loading">カメラを読み込んでいます</p>
		<canvas ref="canvas"></canvas>
		<p>
			<button @click="ReloadCamera">カメラを再読み込みする</button>
			<button @click="SwitchCamera">カメラを切り替える</button>
		</p>
	</section>
</template>

<script>
import jsQR from "~/assets/js/jsQR.js"

export default {
	name: "ScanQRcodeComponent",
	props: {
		timeout: {
			type: Number,
			default: 3000,
		},
	},
	data() {
		return {
			NoPermission: true,
			Loading: false,
			canvas: null,
			context: null,
			video: null,
			stream: null,

			imageData: null,
			code: null,

			Out: false,

			QR_DATA: "",
		}
	},
	mounted() {
		this.canvas = this.$refs.canvas
		this.context = this.canvas.getContext("2d")
		this.video = document.createElement("video")
		this.StartCamera()
		setInterval(this.reload, 120000)
	},
	destroyed() {
		this.StopCamera()
	},
	methods: {
		drawLine(begin, end, color) {
			this.context.beginPath()
			this.context.moveTo(begin.x, begin.y)
			this.context.lineTo(end.x, end.y)
			this.context.lineWidth = 4
			this.context.strokeStyle = color
			this.context.stroke()
		},
		clear() {
			this.QR_DATA = ""
			this.getCameraTick()
		},
		getCameraTick() {
			setTimeout(() => {
				requestAnimationFrame(this.tick)
			}, 200)
		},
		tick() {
			this.NoPermission = false
			this.Loading = true
			if (this.video.readyState === this.video.HAVE_ENOUGH_DATA) {
				this.Loading = false

				this.canvas.height = this.video.videoHeight
				this.canvas.width = this.video.videoWidth
				this.context.drawImage(this.video, 0, 0, this.canvas.width, this.canvas.height)

				this.imageData = this.context.getImageData(0, 0, this.canvas.width, this.canvas.height)
				this.code = jsQR(this.imageData.data, this.imageData.width, this.imageData.height, {
					inversionAttempts: "dontInvert",
				})

				if (this.code) {
					this.drawLine(this.code.location.topLeftCorner, this.code.location.topRightCorner, "#FF3B58")
					this.drawLine(this.code.location.topRightCorner, this.code.location.bottomRightCorner, "#FF3B58")
					this.drawLine(this.code.location.bottomRightCorner, this.code.location.bottomLeftCorner, "#FF3B58")
					this.drawLine(this.code.location.bottomLeftCorner, this.code.location.topLeftCorner, "#FF3B58")
					this.QR_DATA = this.code.data
					if (this.code.data) {
						this.$emit("func", this.code.data)
						setTimeout(this.clear, this.timeout)
					} else {
						this.getCameraTick(this.tick)
					}
				} else {
					this.getCameraTick(this.tick)
				}
			} else {
				this.getCameraTick(this.tick)
			}
		},
		StartCamera() {
			navigator.mediaDevices
				.getUserMedia({ video: { facingMode: this.Out ? { exact: "environment" } : "user" } })
				.then((stream) => {
					this.stream = stream
					this.video.srcObject = this.stream
					this.video.setAttribute("playsinline", true)
					this.video.play()
					requestAnimationFrame(this.tick)
				})
				.catch(() => {
					this.Out = !this.Out
					this.StartCamera()
				})
		},
		StopCamera() {
			this.stream.getVideoTracks().forEach((track) => {
				track.stop()
			})
		},
		SwitchCamera() {
			this.StopCamera()
			this.Out = !this.Out
			this.StartCamera()
		},
		ReloadCamera() {
			this.StopCamera()
			this.StartCamera()
		},
		reload() {
			location.reload()
		},
	},
}
</script>

<style lang="scss" scoped>
section {
	p {
		text-align: center;
		display: flex;
		gap: 4em;
		align-items: center;
		justify-content: center;
	}

	canvas {
		width: 80%;
		margin: auto;
		transform: scale(-1, 1);
	}

	button {
		background-color: #831843;
		border-radius: 7px;
		padding: 2px;
		color: white;
	}
}
</style>
