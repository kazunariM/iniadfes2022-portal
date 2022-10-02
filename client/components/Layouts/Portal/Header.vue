<template>
	<header>
		<div class="group rounded-b-3xl shadow-xl bg-white px-4 py-2">
			<div class="flex justify-between">
				<div class="flex-none">
					<nuxt-link to="/"><img class="h-12" src="/fes-logo.png" alt="iniadfes-logo"></nuxt-link>
				</div>
				<div class="peer-flex-none flex items-center text-sm truncate ml-4">
					<p v-if="isqr">{{ visitor }} さん</p>
					<button v-if="!isqr" class="bg-pink-900 hover:bg-pink-700 rounded-full text-white p-1 px-3">ネームカードと連動させる</button>
				</div>
			</div>
		</div>
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
