<template>
	<div class="flex flex-col h-screen">
		<Header />
		<nuxt class="flex-grow m-3 md:mx-auto md:w-2/3 xl:w-1/2" />
		<Footer class="bottom-0" />
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
