<template>
    <section>
        <p v-if="NoPermission">カメラの利用を許可してください</p>
        <p v-if="Loading">カメラを読み込んでいます</p>
        <canvas ref="canvas"></canvas>
        <p>{{ QR_DATA }}</p>
    </section>
</template>

<script>
import jsQR from '~/static/jsQR.js'

export default {
    name: "ScanQRcodeComponent",
    data() {
        return {
            NoPermission: true,
            Loading: false,
            canvas: null,
            context: null,
            video: null,

            imageData: null,
            code: null,

            QR_DATA: "",
        }
    },
    mounted() {    
        this.canvas = this.$refs.canvas;
        this.context = this.canvas.getContext("2d")
        this.video = document.createElement("video")
        this.StartCamera()
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
            requestAnimationFrame(this.tick)
        },
        tick() {
            this.NoPermission = false
            this.Loading = true
            if (this.video.readyState === this.video.HAVE_ENOUGH_DATA) {
                this.Loading = false

                this.canvas.height = this.video.videoHeight
                this.canvas.width = this.video.videoWidth
                this.context.drawImage(this.video, 0, 0, this.canvas.width, this.canvas.height)

                this.imageData = this.context.getImageData(0, 0, this.canvas.width, this.canvas.height);
                this.code = jsQR(this.imageData.data, this.imageData.width, this.imageData.height, {
                    inversionAttempts: "dontInvert",
                })

                if (this.code) {
                    this.drawLine(this.code.location.topLeftCorner, this.code.location.topRightCorner, "#FF3B58")
                    this.drawLine(this.code.location.topRightCorner, this.code.location.bottomRightCorner, "#FF3B58")
                    this.drawLine(this.code.location.bottomRightCorner, this.code.location.bottomLeftCorner, "#FF3B58")
                    this.drawLine(this.code.location.bottomLeftCorner, this.code.location.topLeftCorner, "#FF3B58")
                    this.QR_DATA = this.code.data
                    setTimeout(this.clear, 3000)
                } else {
                    requestAnimationFrame(this.tick)
                }
            } else {
                requestAnimationFrame(this.tick)
            }
        },
        StartCamera() {
            navigator.mediaDevices.getUserMedia({ video: { facingMode: "environment" } })
                .then((stream) => {
                    this.video.srcObject = stream
                    this.video.setAttribute("playsinline", true)
                    this.video.play()
                    requestAnimationFrame(this.tick)
                });
        },
    },
}
</script>
