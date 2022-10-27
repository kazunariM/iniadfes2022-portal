<template>
	<main>
		<h1>ネームカードをスキャン</h1>
		<ScanQRcodeComponent @func="open" />
		<p>スタンプラリーや巡った企画一覧が見られるように！</p>
	</main>
</template>

<script>
export default {
	layout: "portal",
	middleware: "scannamecard",
	mounted() {
		this.$nuxt.$emit("setTitle", "赤羽台祭ポータル")
	},
	methods: {
		open(url) {
			const qrid = url.match(/https:\/\/portal.iniadfes.com\/open\/([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/)
			if (qrid) {
				this.$router.push(`/open/${qrid[1]}/`)
			}
		},
	},
}
</script>
