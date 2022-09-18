<template>
	<div>
		<HeaderView />
		<section>
			<nuxt-link to="Registration">事前登録をする</nuxt-link>
		</section>
		<section>
			<nuxt-link to="ScanNamecard">スタンプラリーを見る</nuxt-link>
		</section>
	</div>
</template>

<script>
export default {
	name: "IndexPage",
}
</script>
