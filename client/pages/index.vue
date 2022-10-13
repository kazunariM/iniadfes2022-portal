<template>
	<main>
		<article>
			<div class="bg-gray-200 rounded-md w-full p-1 px-2 mt-2">
				<h1 class="text-sm text-gray-800">赤羽台祭ポータル</h1>
			</div>

			<section v-if="is_before">
				<div class="border-b-2 m-3 p-2 pb-5">
					<h2 class="text-md mb-1">【 INFORMATION 】</h2>
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
					<nuxt-link to="ScanNamecard">ネームカードのQRコードを読み取る</nuxt-link>
				</section>
				<section v-if="is_qrid">
					<p>スタンプラリー</p>
				</section>
			</section>
			<section class="border-t-2 p-5 m-3">
				<h3 class="text-xl text-center">赤羽台祭関連サイト</h3>
				<a href="https://akabanedai-fes.com">
					<button class="flex justify-between items-center bg-gray-50 border-2 shadow-xl hover:bg-gray-300 text-gray-900 p-2 mt-5 w-full rounded-lg text-xl">
						<img class="h-10 m-2 flex-none" src="/akabanedaifes-logo.png" alt="akabanedaifes-logo" />
						<p class="flex-1">赤羽台祭</p>
					</button>
				</a>
				<a href="https://iniadfes.com">
					<button class="flex justify-between items-center bg-gray-50 border-2 shadow-xl hover:bg-gray-300 text-gray-900 p-2 mt-5 w-full rounded-lg text-xl">
						<img class="h-10 m-2 flex-none" src="/fes-logo.png" alt="iniadfes-logo" />
						<p class="flex-1">INIAD-FES</p>
					</button>
				</a>
				<a href="https://wellbfes.com">
					<button class="flex justify-between items-center bg-gray-50 border-2 shadow-xl hover:bg-gray-300 text-gray-900 p-2 mt-5 w-full rounded-lg text-xl">
						<img class="h-10 m-2 flex-none rounded-full" src="/wellbfes-logo.png" alt="wellbfes-logo" />
						<p class="flex-1">WELLB-FES</p>
					</button>
				</a>
			</section>
		</article>
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
