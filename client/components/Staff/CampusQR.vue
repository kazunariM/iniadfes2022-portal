<template>
	<article>
		<ScanQRcodeComponent @func="Register" />
	</article>
</template>

<script>
export default {
	props: {
		mode: {
			type: String,
			default: "Enter",
		},
	},
	methods: {
		Register(qrid) {
			this.$emit("func", qrid)
		},
	},
}
</script>
