<template>
	<main>
		<table>
			<tbody>
				<tr>
					<th>デザイン</th>
					<th>ニックネーム</th>
					<th>二次元コード下の数字</th>
					<th>二次元コード</th>
					<th>印刷完了</th>
				</tr>
				<tr v-for="(visitor, index) in visitors" :key="index">
					<td>{{ visitor.design.name }}</td>
					<td>{{ visitor.nickname }}</td>
					<td>{{ visitor.identifying }}</td>
					<td>{{ visitor.userid }}</td>
					<td>
						<span v-if="!visitor.printed" @click="printed(visitor.userid, visitor)">印刷した</span>
						<span v-else>済</span>
					</td>
				</tr>
			</tbody>
		</table>
	</main>
</template>

<script>
export default {
	asyncData({ $axios, redirect }) {
		return $axios
			.get("/api/v1/staff/pages/AllocationQRID/")
			.then((res) => {
				if (res.data.result === null) {
					redirect("/Staff/Signin/")
				} else if (!res.data.result) {
					redirect("/Staff/")
				} else {
					return $axios.get("/api/v1/staff/get_prereg/not_printing/").then((res) => {
						for (const item of res.data) {
							item.printed = false
						}
						return {
							visitors: res.data,
						}
					})
				}
			})
			.catch(() => {
				redirect("/")
			})
	},
	methods: {
		printed(userid, visitor) {
			this.$axios({
				method: "patch",
				url: `/api/v1/staff/printed/${userid}/`,
				headers: {
					"Content-Type": "application/json",
					"X-CSRFToken": this.$cookies.get("csrftoken"),
				},
				data: {
					is_printed: true,
				},
			}).then((res) => {
				visitor.printed = res.data.is_printed
			})
		},
	},
}
</script>
