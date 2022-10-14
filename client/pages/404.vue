<template>
	<div>
		<p>このページは存在しません</p>
		<nuxt-link to="/">トップページに戻る</nuxt-link>
	</div>
</template>

<script>
export default {
	layout: "portal",
	mounted() {
		this.$nuxt.$emit("setTitle", "NOT FOUND")
	},
}
</script>
