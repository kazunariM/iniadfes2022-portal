<template>
	<main>
		<article>
			<div class="bg-gray-200 rounded-md w-full p-1 px-2 mt-2">
				<h1 class="text-sm text-gray-800">来場者登録 仮登録完了</h1>
			</div>
			<p>入力していただいたメールアドレス宛に確認URLを載せたメールを送信いたしました。ご確認ください。</p>
			<p>万が一メールが届いていない場合お手数ですが<a href="mailto:support@iniadfes.com">support@iniadfes.com</a>までご連絡ください。</p>
		</article>
	</main>
</template>

<script>
export default {
	name: "Requested",
	layout: "portal",
	// created() {
	// 	const getData = this.$store.getters["Registration/requested/get"]
	// 	if (!getData.requested) {
	// 		this.$router.replace("/")
	// 	}
	// 	this.$store.dispatch("Registration/requested/changeAction", { requested: false })
	// },
}
</script>

<style lang="scss" scoped>
a {
	color: #352995;
	text-decoration: underline;
}
</style>
