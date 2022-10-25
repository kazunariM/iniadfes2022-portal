export default function ({ route, redirect, $axios, store, $cookies }) {
	$axios.get("/api/v1/state/").then((res) => {
		for (const key of Object.keys(res.data)) {
			if (res.data[key]) {
				store.dispatch("switching/setAction", key)
			}
		}
	})

	if ($cookies.get("userid")) {
		$axios
			.get(`/api/v1/open/${$cookies.get("userid")}/`)
			.then((res) => {
				store.dispatch("visitor/setBase", res.data)
			})
			.catch(() => {
				$cookies.remove("userid")
			})
	}
}
