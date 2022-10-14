<template>
	<article>
		<h3>入力内容をご確認ください</h3>
		<form @submit.prevent="submit">
			<section>
				<h4><img src="https://icongr.am/fontawesome/pencil.svg?size=16&color=currentColor" />ニックネーム</h4>
				<p>{{ formdata.nickname }}</p>
			</section>

			<section>
				<h4><img src="https://icongr.am/fontawesome/pencil.svg?size=16&color=currentColor" />ネームカードデザイン</h4>
				<p><img :src="get_namecard()" /></p>
			</section>

			<section>
				<h4><img src="https://icongr.am/fontawesome/pencil.svg?size=16&color=currentColor" />メールアドレス</h4>
				<p>{{ formdata.email }}</p>
			</section>

			<section v-if="formdata.address">
				<h4><img src="https://icongr.am/fontawesome/pencil.svg?size=16&color=currentColor" />お住まい</h4>
				<p>{{ get_from_arr("address") }}</p>
			</section>

			<section v-if="formdata.gender">
				<h4><img src="https://icongr.am/fontawesome/pencil.svg?size=16&color=currentColor" />性別</h4>
				<p>{{ get_from_arr("gender") }}</p>
			</section>

			<section v-if="formdata.age">
				<h4><img src="https://icongr.am/fontawesome/pencil.svg?size=16&color=currentColor" />ご年代</h4>
				<p>{{ get_from_arr("age") }}</p>
			</section>

			<section v-if="formdata.job">
				<h4><img src="https://icongr.am/fontawesome/pencil.svg?size=16&color=currentColor" />ご職業</h4>
				<p>{{ get_from_arr("job") }}</p>
			</section>

			<section v-if="formdata.major_subject">
				<h4><img src="https://icongr.am/fontawesome/pencil.svg?size=16&color=currentColor" />専攻/希望分野</h4>
				<p>{{ get_from_arr("major_subject") }}</p>
			</section>

			<section v-if="formdata.know_about.length">
				<h4><img src="https://icongr.am/fontawesome/pencil.svg?size=16&color=currentColor" />INIAD-FES・WELLB-FESはどこで知りましたか？</h4>
				<p>{{ get_know_about() }}</p>
			</section>

			<section>
				<h4><img src="https://icongr.am/feather/bell.svg?size=16&color=53122b" />メール受信設定確認のお願い<img src="https://icongr.am/feather/bell.svg?size=16&color=53122b" /></h4>
				<span>ドメイン設定を利用されている方は「@iniadfes.com」からのメールを受信できる設定をお願いいたします。</span>
			</section>

			<div class="btns">
				<span class="bg-blue-900 hover:bg-blue-700 text-white py-1 px-4 shadow-xl rounded-md text-center" @click="back()"><img src="https://icongr.am/entypo/back.svg?size=16&color=ffffff" />修正する</span>
				<button type="submit" class="bg-pink-900 hover:bg-pink-700 text-white py-1 px-4 shadow-xl rounded-md">この内容で登録する</button>
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
			error: {
				email: "",
				nickname: "",
				design: "",
				address: "",
				gender: "",
				age: "",
				job: "",
				major_subject: "",
				know_about: "",
				agree: "",
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
		if (!this.$cookies.get("csrftoken")) {
			this.$axios.get("/api/v1/initial/").then((res) => {
				this.$cookies.set("csrftoken", res.data.csrftoken, { path: "/", maxAge: 60 * 60 })
			})
		}
		const getFormdata = this.$store.getters["Registration/get"]
		if (!getFormdata.agree) {
			this.$router.replace("/Registration/")
		}
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
					"X-CSRFToken": this.$cookies.get("csrftoken"),
				},
				data: this.formdata,
			})
				.then((res) => {
					this.$store.dispatch("Registration/requested/changeAction", { requested: true })
					this.$router.replace("/Registration/Requested/")
				})
				.catch((error) => {
					const errData = error.response.data.detail
					this.error.email = "email" in errData ? errData.email[0] : ""
					this.error.nickname = "nickname" in errData ? errData.nickname[0] : ""
					this.error.design = "design" in errData ? errData.design[0] : ""
					this.error.address = "address" in errData ? errData.address[0] : ""
					this.error.gender = "gender" in errData ? errData.gender[0] : ""
					this.error.age = "age" in errData ? errData.age[0] : ""
					this.error.job = "job" in errData ? errData.job[0] : ""
					this.error.major_subject = "major_subject" in errData ? errData.major_subject[0] : ""
					this.error.know_about = "know_about" in errData ? errData.know_about[0] : ""
					this.$store.dispatch("Registration/error/changeAction", this.error)
					this.$router.replace("/Registration/")
				})
		},
	},
}
</script>

<style lang="scss" scoped>
form {
	background-color: #ccc;
	padding: 3%;
	border-radius: 7px;

	section {
		background-color: #eee;
		margin-bottom: 3%;
		padding: 1em;
		border-radius: 7px;

		h4 {
			margin-bottom: 0.5em;

			img {
				vertical-align: baseline;
				display: inline;
				margin-right: 0.5em;
				margin-left: 0.5em;
			}
		}

		p {
			background-color: white;
			padding: 0.5em;
			border-radius: 7px;

			img {
				width: 300px;
			}
		}
	}

	div.btns {
		justify-content: center;
		align-items: center;

		display: flex;
		flex-direction: column;
		gap: 16px;

		img {
			display: inline;
			margin-right: 0.5em;
		}

		span,
		button {
			width: 100%;
		}

		@include mq(md) {
			display: flex;
			flex-direction: row;
		}
	}
}
</style>
