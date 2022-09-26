export default function ({ route, redirect, $axios }) {
	return $axios
		.get("/api/v1/staff/check/")
		.then((res) => {
			if (!res.data.is_authenticated) {
				redirect("/Staff/Signin")
			}
		})
		.catch(() => {
			redirect("/")
		})
}
