<template>
	<div>
		<p>このページは存在しないにゃー。開いてるページを確認してほしいにゃー。</p>
		<p>INIAD-FES当日はいっぱいご飯が食べたいにゃー・・・。</p>
		<p><img src="/tabetainya.png" alt="" /></p>
		<button class="bg-pink-900 hover:bg-pink-700 text-white py-2 px-8 shadow-xl rounded-md w-full" @click="moveTop">トップページに戻る</button>
	</div>
</template>

<script>
export default {
	layout: "portal",
	mounted() {
		this.$nuxt.$emit("setTitle", "NOT FOUND")
	},
	methods: {
		moveTop() {
			this.$router.push("/")
		},
	},
}
</script>
