<template>
	<main>
		<h1>INIAD-FES Portalサイト</h1>
		<section v-if="is_before">
			<div class="border-b-2 m-3 p-2 pb-5">
				<h1 class="text-md mb-1">【 INFORMATION 】</h1>
				<p class="text-sm leading-relaxed">こちらは赤羽台祭の来場者情報事前登録ページです。<br />赤羽台祭についての情報に関しましては、ページ下部のリンクよりホームページをご覧ください。</p>
			</div>
			<div class="m-3 p-5 text-center">
				<h2 class="text-xl mb-5">来場者情報事前登録はこちらから</h2>
				<button class="bg-pink-900 hover:bg-pink-700 text-white p-5 w-full shadow-xl rounded-lg text-xl" @click="moveRegistration">事前登録をする</button>
			</div>
		</section>
		<section v-if="!is_before">
			<section v-if="!is_qrid">
				<h2>ネームカードと連動させる</h2>
				<nuxt-link to="ScanNamecard">ネームカードの二次元コードを読み取る</nuxt-link>
			</section>
			<section v-if="is_qrid">
				<p>スタンプラリー</p>
			</section>
		</section>
	</main>
</template>

<script>
export default {
	layout: "portal",
	asyncData({ $axios, $cookies }) {
		if ($cookies.get("qrid")) {
			return $axios
				.get(`/api/v1/portaltop/${$cookies.get("qrid")}/`)
				.then((res) => {
					$cookies.set("visitor", res.data.nickname)
					return {
						is_qrid: true,
						visitor: res.data.nickname,
					}
				})
				.catch(() => {
					return {
						is_qrid: false,
					}
				})
		} else {
			return {
				is_qrid: false,
				is_before: true,
			}
		}
	},
	methods: {
		moveRegistration() {
			this.$router.replace("/Registration/")
		},
	},
}
</script>
