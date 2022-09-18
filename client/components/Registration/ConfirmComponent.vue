<template>
	<article>
		<h3>入力内容をご確認ください</h3>
		<form @submit.prevent="submit">
			<table>
				<tr>
					<td>お名前</td>
					<td>{{ formdata.last_name }} {{ formdata.first_name }}</td>
				</tr>
				<tr>
					<td>フリガナ</td>
					<td>{{ formdata.ruby_last_name }} {{ formdata.ruby_first_name }}</td>
				</tr>
				<tr>
					<td>メールアドレス</td>
					<td>{{ formdata.email }}</td>
				</tr>
				<tr>
					<td>ニックネーム</td>
					<td>{{ formdata.nickname }}</td>
				</tr>
				<tr>
					<td>ネームカード</td>
					<td><img :src="get_namecard()" /></td>
				</tr>
				<tr>
					<td>お住まい</td>
					<td>{{ get_from_arr("address") }}</td>
				</tr>
				<tr>
					<td>性別</td>
					<td>{{ get_from_arr("gender") }}</td>
				</tr>
				<tr>
					<td>ご年代</td>
					<td>{{ get_from_arr("age") }}</td>
				</tr>
				<tr>
					<td>ご職業</td>
					<td>{{ get_from_arr("job") }}</td>
				</tr>
				<tr>
					<td>専攻/希望分野</td>
					<td>{{ get_from_arr("major_subject") }}</td>
				</tr>
				<tr>
					<td>INIAD-FES・WELLB-FES・このポータルサイトはどこで知りましたか？</td>
					<td>{{ get_know_about() }}</td>
				</tr>
			</table>
			<div>
				<p @click="back()">修正する</p>
				<button type="submit">この内容で登録する</button>
			</div>
		</form>
	</article>
</template>

<script>
export default {
	name: "ConfirmComponent",
	data() {
		return {
			formdata: {
				last_name: "",
				first_name: "",
				ruby_last_name: "",
				ruby_first_name: "",
				email: "",
				nickname: "",
				design: "",
				address: null,
				gender: null,
				age: null,
				job: null,
				major_subject: null,
				know_about: [],
				agree: false,
			},
			list: {
				namecard: [],
				age: [],
				job: [],
				major_subject: [],
				gender: [],
				address: [],
				know_about: [],
			},
		}
	},
	created() {
		const getFormdata = this.$store.getters["Registration/get"]
		if (!getFormdata.agree) {
			this.$router.replace("/Registration/")
		}
		this.formdata.last_name = getFormdata.last_name
		this.formdata.first_name = getFormdata.first_name
		this.formdata.ruby_last_name = getFormdata.ruby_last_name
		this.formdata.ruby_first_name = getFormdata.ruby_first_name
		this.formdata.email = getFormdata.email
		this.formdata.nickname = getFormdata.nickname
		this.formdata.design = getFormdata.design
		this.formdata.address = getFormdata.address
		this.formdata.gender = getFormdata.gender
		this.formdata.age = getFormdata.age
		this.formdata.job = getFormdata.job
		this.formdata.major_subject = getFormdata.major_subject
		this.formdata.know_about = getFormdata.know_about
		this.formdata.agree = getFormdata.agree

		const getListdata = this.$store.getters["Registration/data/get"]
		this.list.age = getListdata.age
		this.list.job = getListdata.job
		this.list.major_subject = getListdata.major_subject
		this.list.gender = getListdata.gender
		this.list.address = getListdata.address
		this.list.know_about = getListdata.know_about
		this.list.namecard = getListdata.namecard
	},
	methods: {
		get_from_arr(el) {
			const arr = this.list[el].filter((lst) => lst.value === this.formdata[el])
			if (arr.length) {
				return arr[0].display
			}
		},
		get_namecard() {
			const arr = this.list.namecard.filter((lst) => lst.uuid === this.formdata.design)
			if (arr.length) {
				return arr[0].img
			}
		},
		get_know_about() {
			return this.formdata.know_about.join(", ")
		},
		back() {
			this.$router.replace("/Registration/")
		},
		submit() {
			this.$axios({
				method: "post",
				url: "/api/v1/registration/",
				headers: {
					"Content-Type": "application/json",
					// "X-CSRFToken": csrftoken,
				},
				data: this.formdata,
			})
		},
	},
}
</script>

<style lang="scss" scoped>
table {
	img {
		width: 300px;
	}
}
</style>
