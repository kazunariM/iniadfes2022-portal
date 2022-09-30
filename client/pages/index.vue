<template>
	<article>
		<h1>INIAD-FES Portalサイト</h1>
		<section v-if="is_before">
			<h2>事前予約はこちらから</h2>
			<nuxt-link to="Registration">事前登録をする</nuxt-link>
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
	</article>
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
}
</script>
