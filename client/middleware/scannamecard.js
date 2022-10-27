export default function ({ route, redirect, $axios, store, $cookies }) {
	if ($cookies.get("userid")) {
		return $axios.get("/api/v1/state/").then((res) => {
			for (const key of Object.keys(res.data)) {
				if (res.data[key]) {
					if (key === "fes" || key === "finished") {
						return
					}
				}
			}
			redirect("/")
		})
	}
}
