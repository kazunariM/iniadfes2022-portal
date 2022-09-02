<template>
    <section>
        <p class="error">{{ error }}</p>
        <client-only><qrcode-stream paused="paused" @decode="onDecode" @init="onInit" /></client-only>
    </section>
</template>

<script>

export default {
    name: "ScanQRcodeComponents",
    
    data() {
        return {
            NoPermission: true,
            Loading: false,
            canvas: null,
            context: null,
            video: null,

            imageData: null,
            code: null,

            paused: false,
            error: "",
        }
    },
    mounted() {    
    },
    methods: {
        async onInit (promise) {
            // show loading indicator
            try {
                await promise
                // successfully initialized
            } catch (error) {
                if (error.name === "NotAllowedError") {
                    this.error = "カメラの利用を許可してください"
                } else if (error.name === "NotFoundError") {
                    this.error = "カメラが見つかりません"
                } else if (error.name === "NotSupportedError") {
                    this.error = "ブラウザを変更してお試しください"
                } else if (error.name === "NotReadableError") {
                    this.error = "スキャンに失敗しました"
                } else if (error.name === "OverconstrainedError") {
                    this.error = "カメラが使用できません"
                } else {
                    this.error = "もう一度お試しください"
                }
            } finally {
                // hide loading indicator
            }
        },
        onDecode(content){
            this.paused = true
            alert(content)
        }
    },
}
</script>
