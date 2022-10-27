<template>
	<main></main>
</template>

<script>
export default {
	asyncData({ $axios, params, $cookies, redirect }) {
		return $axios
			.get(`/api/v1/open/${params.qrid}/`)
			.then((res) => {
				$cookies.set("userid", res.data.qrid, { path: "/", maxAge: 60 * 60 })
				redirect("/")
			})
			.catch(() => {
				if ($cookies.get("userid")) {
					$cookies.remove("userid")
				}
				redirect("/")
			})
	},
}
</script>
