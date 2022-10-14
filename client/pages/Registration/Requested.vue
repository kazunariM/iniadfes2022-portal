<template>
	<div>
		<p>入力していただいたメールアドレス宛に仮受付確認メールを送信いたしました。仮受付確認メールにメールアドレス確認用URLを添付いたしましたので必ず開くようお願いいたします。</p>
		<p>万が一メールが届いていない場合お手数ですが<a href="mailto:support@iniadfes.com">support@iniadfes.com</a>までご連絡ください。</p>
	</div>
</template>

<script>
export default {
	name: "Requested",
	layout: "portal",
	mounted() {
		this.$nuxt.$emit("setTitle", "来場者登録 仮受付完了")
	},
	created() {
		const getData = this.$store.getters["Registration/requested/get"]
		if (!getData.requested) {
			this.$router.replace("/")
		}
		this.$store.dispatch("Registration/requested/changeAction", { requested: false })
	},
}
</script>

<style lang="scss" scoped>
a {
	color: #352995;
	text-decoration: underline;
}
</style>
