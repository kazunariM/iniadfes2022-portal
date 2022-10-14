<template>
	<header>
		<div class="group rounded-b-3xl shadow-lg bg-white px-4 py-2">
			<div class="flex justify-between">
				<div class="flex-none">
					<nuxt-link to="/"><img class="h-12" src="/fes-logo.png" alt="iniadfes-logo" /></nuxt-link>
				</div>
				<div class="peer-flex-none flex items-center text-sm truncate ml-4">
					<p v-if="isqr && fes">{{ visitor }} さん</p>
					<button v-if="!isqr && fes" class="bg-pink-900 hover:bg-pink-700 rounded-full text-white p-1 px-3">ネームカードと連動させる</button>
				</div>
			</div>
		</div>
		<div class="bg-gray-200 rounded-md p-1 px-2 grow mx-3 mt-5 md:mx-auto md:w-2/3 xl:w-1/2">
			<h1 class="text-sm">{{ title }}</h1>
		</div>
	</header>
</template>

<script>
export default {
	props: {
		title: {
			type: String,
			default: null,
		},
	},
	data() {
		return {
			isqr: null,
			visitor: null,
			fes: false,
		}
	},
	mounted() {
		this.isqr = !!this.$cookies.get("qrid")
		this.visitor = this.$cookies.get("visitor")
	},
}
</script>

<style lang="scss"></style>
