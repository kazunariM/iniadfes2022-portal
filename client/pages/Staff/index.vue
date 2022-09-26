<template>
	<article>
		<h1>スタッフメニュー</h1>
		<ul v-if="pages">
			<li v-for="(page, index) in pages" :key="index" @click="move(page.page)">{{ page.func }}</li>
		</ul>
		<p v-if="!pages.length">割り当てられた権限がありません。</p>
	</article>
</template>

<script>
export default {
	middleware: "staff",
	asyncData({ $axios, $cookies, route, redirect }) {
		return $axios.get("/api/v1/staff/menu").then((res) => {
			return {
				pages: res.data,
			}
		})
	},
	methods: {
		move(url) {
			window.location.href = `/Staff/${url}/`
		},
	},
}
</script>

<style lang="scss" scoped>
li {
	cursor: pointer;
}
</style>
