<template>
	<div class="flex flex-col min-h-screen">
		<Header :title="title" />
		<main class="flex-grow m-3 md:mx-auto md:w-2/3 xl:w-1/2">
			<nuxt />
		</main>
		<Footer />
	</div>
</template>

<script>
import Header from "@/components/Layouts/Portal/Header"
import Footer from "@/components/Layouts/Portal/Footer"
export default {
	components: {
		Header,
		Footer,
	},
	data() {
		return {
			title: null,
		}
	},
	created() {
		this.$nuxt.$on("setTitle", this.setTitle)
	},
	methods: {
		setTitle(title) {
			this.title = title
		},
	},
}
</script>
