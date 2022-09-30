<template>
	<div>
		<Header />
		<nuxt />
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
}
</script>
