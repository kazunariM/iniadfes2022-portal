<template>
	<div>
		<HeaderView />
		<section v-if="!is_qrid">
			<nuxt-link to="Registration">事前登録をする</nuxt-link>
		</section>
		<section v-if="is_qrid">
			<p>{{ visitor.nickname }} さん</p>
			<nuxt-link to="ScanNamecard">スタンプラリーを見る</nuxt-link>
		</section>
	</div>
</template>

<script>
export default {
	name: "IndexPage",
	asyncData({ $axios, $cookies }) {
		if ($cookies.get("qrid")) {
			return $axios
				.get(`/api/v1/portaltop/${$cookies.get("qrid")}/`)
				.then((res) => {
					return {
						is_qrid: true,
						visitor: res.data,
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
			}
		}
	},
}
</script>
