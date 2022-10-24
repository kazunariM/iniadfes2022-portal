<template>
	<main>
		<article>
			<h1>人数確認</h1>
			<p>{{ nowdate }} 時点</p>
			<section>
				<h2>キャンパスの総人数</h2>
				<table>
					<tbody>
						<tr>
							<th>現在の人数</th>
							<th>総参加者</th>
							<th>延べ総参加者</th>
						</tr>
						<tr>
							<td>{{ campus.count }}</td>
							<td>{{ campus.unique_count }}</td>
							<td>{{ campus.total_count }}</td>
						</tr>
					</tbody>
				</table>
			</section>
			<section>
				<h2>各ブースの人数</h2>
				<table>
					<tbody>
						<tr>
							<th>キャンパス</th>
							<th>フロア</th>
							<th>教室</th>
							<th>団体名</th>
							<th>現在の人数</th>
							<th>総参加者</th>
							<th>延べ総参加者</th>
						</tr>
						<tr v-for="(room, index) in rooms" :key="index">
							<td>{{ room.campus ? "WELLB" : "INIAD" }}</td>
							<td>{{ room.floor }}</td>
							<td>{{ room.room_number }}</td>
							<td>{{ room.groupname }}</td>
							<td>{{ room.count }}</td>
							<td>{{ room.unique_count }}</td>
							<td>{{ room.total_count }}</td>
						</tr>
					</tbody>
				</table>
			</section>
		</article>
	</main>
</template>

<script>
export default {
	asyncData({ $axios, redirect }) {
		return $axios
			.get("/api/v1/staff/pages/Watching/")
			.then((res) => {
				if (res.data.result === null) {
					redirect("/Staff/Signin/")
				} else if (!res.data.result) {
					redirect("/Staff/")
				} else {
					const date = new Date()
					return $axios.get("/api/v1/staff/watching/campus").then((res1) => {
						return $axios.get("/api/v1/staff/watching/room/").then((res2) => {
							return {
								campus: res1.data,
								rooms: res2.data,
								nowdate: `${date.getFullYear()}/${date.getMonth() + 1}/${date.getDate()} ${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}`,
							}
						})
					})
				}
			})
			.catch(() => {
				redirect("/")
			})
	},
	mounted() {
		setInterval(this.getPeople, 10000)
	},
	methods: {
		getPeople() {
			const date = new Date()
			this.$axios.get("/api/v1/staff/watching/campus").then((res) => {
				this.campus = res.data
			})
			this.$axios.get("/api/v1/staff/watching/room/").then((res) => {
				this.rooms = res.data
			})
			this.nowdate = `${date.getFullYear()}/${date.getMonth() + 1}/${date.getDate()} ${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}`
		},
	},
}
</script>

<style lang="scss" scoped>
table {
	margin: 1em;

	tbody {
		background-color: #eee;

		tr {
			text-align: center;
			th,
			td {
				padding: 0.5em;
			}

			th {
				border-bottom: solid 1px black;
			}
		}
	}
}
</style>
