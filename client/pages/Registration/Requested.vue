<template>
	<article>
		<h1>来場者登録 仮登録完了</h1>
		<p>入力していただいたメールアドレス宛に確認URLを載せたメールを送信いたしました。ご確認ください。</p>
		<p>万が一メールが届いていない場合お手数ですが<a href="mailto:support@iniadfes.com">support@iniadfes.com</a>までご連絡ください。</p>
	</article>
</template>

<script>
export default {
	name: "Requested",
	created() {
		const getData = this.$store.getters["Registration/requested/get"]
		if (!getData.requested) {
			this.$router.replace("/")
		}
		this.$store.dispatch("Registration/requested/changeAction", { requested: false })
	},
}
</script>

<style lang="scss" scoped></style>
