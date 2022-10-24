<template>
	<main>
		<h1>ネームカードをスキャン</h1>
		<ScanQRcodeComponent @func="debug" />
		<article>
			<h2></h2>
			<p></p>
		</article>
	</main>
</template>

<script>
export default {
	methods: {
		debug(data) {
			alert(data)
		},
	},
}
</script>
