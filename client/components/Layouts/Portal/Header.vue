<template>
	<header>
		<nuxt-link to="/">INIAD-FES</nuxt-link>
		<p v-if="isqr">{{ visitor }}</p>
	</header>
</template>

<script>
export default {
	data() {
		return {
			isqr: null,
			visitor: null,
		}
	},
	mounted() {
		this.isqr = !!this.$cookies.get("qrid")
		this.visitor = this.$cookies.get("visitor")
	},
}
</script>
