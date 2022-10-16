<template>
	<form @submit.prevent="submit">
		<fieldset>
			<section>
				<h3>カスタムINIADネームカード</h3>
				<p>
					赤羽台祭では、感染症対策とINIAD生の生活を体験することを目的とした企画として、普段INIAD生が構内で着用しているネームカードを全員にご着用いただきます。ご着用いただくカードについては、大学祭特別仕様のデザインを複数種類ご用意致しましたので、お好きなものをお選びください。また、事前登録をいただいた方にのみ、特別にご登録いただいたニックネームを印刷したネームカードをご用意いたしますので、ご来場をお考えの方はぜひこのままご登録をお進めください。
				</p>
				<label>
					<p>ニックネーム<span class="required">(必須)</span></p>
					<p>
						<input v-model="formdata.nickname" type="text" placeholder="†いにゃー-BlueEyes-†" required @focus="removeError('nickname')" @blur="checkNickname" />
					</p>
				</label>
				<p v-if="error.nickname" class="error"><img src="https://icongr.am/feather/alert-triangle.svg?size=18&color=ffffff" alt="" />{{ error.nickname }}</p>
				<ul class="notice">
					<li>ネームカードに印刷されるニックネームです。また、緊急時のご連絡の際にも使用させていただく場合がございます。公序良俗に反さない範囲でのご登録をお願い申し上げます。</li>
					<li>16字以内でお願いいたします。</li>
				</ul>
			</section>

			<section>
				<p>デザイン<span class="required">(必須)</span></p>
				<ul class="namecard-design">
					<li v-for="(i, index) in list.namecard" :key="index" class="namecardbox">
						<label :class="formdata.design == i.uuid ? 'selected' : 'no'">
							<p><input v-model="formdata.design" :value="i.uuid" type="radio" required @focus="removeError('design')" />{{ i.name }}</p>
							<div class="namecard-sample">
								<img :src="i.img" :alt="i.name" />
							</div>
							<p>{{ i.text }}</p>
						</label>
					</li>
				</ul>
				<p v-if="error.design" class="error"><img src="https://icongr.am/feather/alert-triangle.svg?size=18&color=ffffff" alt="" />{{ error.design }}</p>
				<ul class="notice">
					<li>当日ご着用いただくネームカードのデザインです。お好きなものをお選びください。</li>
				</ul>
			</section>
		</fieldset>

		<fieldset>
			<section>
				<h3>ご連絡先</h3>
				<label>
					<p>メールアドレス<span class="required">(必須)</span></p>
					<p>
						<input v-model="formdata.email" type="email" placeholder="sample@example.com" required @focus="removeError('email')" @blur="checkEmail" />
					</p>
				</label>
				<p v-if="error.email" class="error"><img src="https://icongr.am/feather/alert-triangle.svg?size=18&color=ffffff" alt="" />{{ error.email }}</p>
				<ul class="notice">
					<li>事前登録完了時に登録完了のメールを送信いたします。</li>
					<li>緊急事態発生時等のご連絡用として使用いたします。</li>
				</ul>
			</section>
		</fieldset>

		<div class="please">
			<p>来場者1名1名それぞれにネームカードを発行いたします。そのため複数人でご来場される場合は<span style="font-weight: bolder; font-size: 1.2em">ご来場される人数分の登録をお願いいたします</span>。メールアドレスは同じもので構いません。ぜひ皆様でそれぞれ楽しいニックネームをお付けください。</p>
		</div>

		<fieldset>
			<section>
				<h3>アンケート</h3>
				<p>来年度以降のINIAD-FESのクオリティ向上のため、よろしければアンケートにご協力ください。</p>
				<section>
					<h4>お住まい(都道府県)</h4>
					<select v-model="formdata.address" @focus="removeError('address')">
						<option v-for="(i, index) in list.address" :key="index" :value="i.value">
							{{ i.display }}
						</option>
					</select>
					<p v-if="error.address" class="error"><img src="https://icongr.am/feather/alert-triangle.svg?size=18&color=ffffff" alt="" />{{ error.address }}</p>
				</section>

				<section>
					<h4>性別</h4>
					<select v-model="formdata.gender" @focus="removeError('gender')">
						<option v-for="(i, index) in list.gender" :key="index" :value="i.value">
							{{ i.display }}
						</option>
					</select>
					<p v-if="error.gender" class="error"><img src="https://icongr.am/feather/alert-triangle.svg?size=18&color=ffffff" alt="" />{{ error.gender }}</p>
				</section>

				<section>
					<h4>ご年代</h4>
					<select v-model="formdata.age" @focus="removeError('age')">
						<option v-for="(i, index) in list.age" :key="index" :value="i.value">
							{{ i.display }}
						</option>
					</select>
					<p v-if="error.age" class="error"><img src="https://icongr.am/feather/alert-triangle.svg?size=18&color=ffffff" alt="" />{{ error.age }}</p>
				</section>

				<section>
					<h4>ご職業</h4>
					<select v-model="formdata.job" @focus="removeError('job')">
						<option v-for="(i, index) in list.job" :key="index" :value="i.value">
							{{ i.display }}
						</option>
					</select>
					<p v-if="error.job" class="error"><img src="https://icongr.am/feather/alert-triangle.svg?size=18&color=ffffff" alt="" />{{ error.job }}</p>
				</section>

				<section v-if="formdata.job == 4 || formdata.job == 5">
					<h4>専攻/希望分野</h4>
					<select v-model="formdata.major_subject" @focus="removeError('major_subject')">
						<option v-for="(i, index) in list.major_subject" :key="index" :value="i.value">
							{{ i.display }}
						</option>
					</select>
					<p v-if="error.major_subject" class="error"><img src="https://icongr.am/feather/alert-triangle.svg?size=18&color=ffffff" alt="" />{{ error.major_subject }}</p>
				</section>

				<section>
					<h4>INIAD-FES・WELLB-FESはどこで知りましたか？</h4>
					<p v-for="(i, index) in list.know_about" :key="index" @focus="removeError('know_about')">
						<label><input v-model="formdata.know_about" :value="i" type="checkbox" @focus="removeError('know_about')" />{{ i }}</label>
					</p>
					<p v-if="error.know_about" class="error"><img src="https://icongr.am/feather/alert-triangle.svg?size=18&color=ffffff" alt="" />{{ error.know_about }}</p>
				</section>
			</section>
		</fieldset>

		<fieldset>
			<section class="confirm">
				<h3>個人情報取り扱いについて(必ずご確認ください)</h3>
				<ol>
					<li>
						利用目的
						<ul>
							<li>「第6回INIAD-FES」ならびに「WELLB-FES2022」の運営のため</li>
							<li>来年度以降の大学祭の参考のため</li>
							<li>緊急時のご連絡に使用するため</li>
							<li>上記以外に個人情報は一切使用しません</li>
						</ul>
					</li>
					<li>
						第三者提供
						<ul>
							<li>第三者提供は一切いたしません</li>
						</ul>
					</li>
				</ol>
				<p>ご不明点等ございましたら以下の連絡先にご連絡ください。</p>
				<div class="contact">
					<p>〒115-8650</p>
					<p>東京都北区赤羽台1丁目7-11 INIAD HUB-1</p>
					<p>第6回INIAD-FES実行委員会 対外部渉外課</p>
					<p><a href="mailto:support@iniadfes.com">support@iniadfes.com</a></p>
				</div>
				<div class="center">
					<label class="center"><input v-model="formdata.agree" type="checkbox" @focus="removeError('agree')" />以上の内容を確認しました。</label>
				</div>
				<p v-if="error.agree" class="error"><img src="https://icongr.am/feather/alert-triangle.svg?size=18&color=ffffff" alt="" />{{ error.agree }}</p>
			</section>
		</fieldset>
		<div class="center">
			<button type="submit" class="bg-pink-900 hover:bg-pink-700 text-white py-2 px-8 shadow-xl rounded-md w-full">入力内容を確認する</button>
		</div>
	</form>
</template>

<script>
export default {
	name: "RegistrationForm",
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
			confirm: false,
		}
	},
	mounted() {
		const getListdata = this.$store.getters["Registration/data/get"]
		this.list.age = getListdata.age
		this.list.job = getListdata.job
		this.list.major_subject = getListdata.major_subject
		this.list.gender = getListdata.gender
		this.list.address = getListdata.address
		this.list.know_about = getListdata.know_about
		this.list.namecard = getListdata.namecard

		const getFormdata = this.$store.getters["Registration/get"]
		this.formdata.email = getFormdata.email
		this.formdata.nickname = getFormdata.nickname
		this.formdata.design = getFormdata.design
		this.formdata.address = getFormdata.address
		this.formdata.gender = getFormdata.gender
		this.formdata.age = getFormdata.age
		this.formdata.job = getFormdata.job
		this.formdata.major_subject = getFormdata.major_subject
		this.formdata.know_about = getFormdata.know_about
		this.formdata.agree = false

		const getErrordata = this.$store.getters["Registration/error/get"]
		this.error.email = getErrordata.email
		this.error.nickname = getErrordata.nickname
		this.error.design = getErrordata.design
		this.error.address = getErrordata.address
		this.error.gender = getErrordata.gender
		this.error.age = getErrordata.age
		this.error.job = getErrordata.job
		this.error.major_subject = getErrordata.major_subject
		this.error.know_about = getErrordata.know_about
		this.$store.dispatch("Registration/error/removeAction")
	},
	methods: {
		submit() {
			if (!this.formdata.agree) {
				this.error.agree = "内容を確認してください"
				return
			}
			for (const key in this.error) {
				if (this.error[key]) {
					return
				}
			}
			this.$store.dispatch("Registration/addAction", this.formdata)
			this.$router.replace("/Registration/Confirm/")
		},
		removeError(el) {
			this.error[el] = ""
		},
		checkEmail() {
			const match = this.formdata.email.match(/^[a-zA-Z0-9_+-]+(\.[a-zA-Z0-9_+-]+)*@([a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]*\.)+[a-zA-Z]{2,}$/)
			if (!match) {
				this.error.email = "正しいメールアドレスを入力してください"
			}
		},
		checkNickname() {
			if (this.formdata.nickname.length > 16) {
				this.error.nickname = "16字以内で入力してください"
				this.formdata.nickname = this.formdata.nickname.slice(0, 16)
			}
		},
	},
}
</script>

<style lang="scss" scoped>
form {
	margin: 1em auto;
	padding: 3%;
	background-color: #ccc;
	border-radius: 7px;

	fieldset {
		margin-bottom: 3%;
		width: 100%;
		background-color: #eee;
		padding: 1em;
		border-radius: 7px;

		section {
			h3 {
				border-left: solid 3px black;
				padding-left: 0.5em;
			}

			label {
				&.name-left {
					float: left;
					width: 45%;
					margin-right: 5%;
				}

				&.name-right {
					float: left;
					width: 45%;
					margin-left: 5%;
				}

				p {
					padding-top: 0.5em;
					padding-bottom: 0.5em;
				}

				input[type="text"],
				input[type="email"] {
					width: 100%;
					border-radius: 5px;
					padding: 4px;
				}
			}

			p {
				&.error {
					position: absolute;
					background-color: #831843;
					color: white;
					font-weight: bold;
					border-radius: 5px;
					padding: 0.5em;
					left: 50%;
					transform: translate(-50%, 5%);
					-webkit-transform: translate(-50%, 5%);

					&::before {
						content: "";
						position: absolute;
						left: 50%;
						transform: translate(-50%, -120%);
						-webkit-transform: translate(-50%, -120%);
						display: block;
						width: 0;
						height: 0;
						border-right: 15px solid transparent;
						border-bottom: 15px solid #831843;
						border-left: 15px solid transparent;
					}

					img {
						display: inline;
						margin-right: 0.5em;
						vertical-align: sub;
					}
				}
			}

			select {
				border-radius: 5px;
				margin: 1em 0;
				padding: 4px;
			}

			ul {
				li {
					label {
						img {
							width: 100%;
							height: auto;
						}
					}

					p {
						white-space: normal;
					}

					&.namecardbox {
						padding: 0.5em;
						display: inline-block;
						vertical-align: top;
						width: 66%;

						@include mq(md) {
							width: 40%;
						}

						@include mq(lg) {
							width: 30%;
						}
					}
				}

				&.notice {
					list-style-type: disc;
					margin-left: 1em;
				}

				&.namecard-design {
					overflow-x: scroll;
					white-space: nowrap;
					max-width: 70vw;
					margin-left: auto;
					margin-right: auto;

					&::-webkit-scrollbar {
						height: 0.5em;

						@include mq(md) {
							height: 0.8em;
						}
					}

					&::-webkit-scrollbar-thumb {
						background: #d2b48c;
						border-radius: 7px;
					}

					&::-webkit-scrollbar-track {
						background: #f5deb3;
						border-radius: 7px;
					}

					li {
						label {
							cursor: pointer;

							p {
								input {
									margin-right: 0.5em;
									accent-color: #831843;
								}
							}

							&.selected {
								color: #831843;
								font-weight: bold;

								img {
									border: solid 4px #831843;
								}
							}
						}
					}

					@include mq(md) {
						max-width: 78vw;
					}
				}
			}

			&.confirm {
				ol {
					list-style-type: decimal;
					margin: 3%;

					li {
						ul {
							list-style-type: disc;
							margin-left: 1em;
						}
					}
				}

				.contact {
					margin: 3%;
					padding: 3%;
					border: solid 1px black;

					@include mq(md) {
						margin: 1em;
						padding: 1em;
					}

					@include mq(md) {
						margin: 1em;
					}
				}
			}
		}

		@include mq(md) {
			margin-bottom: 1em;
		}
	}

	div.please {
		margin-bottom: 3%;
		width: 100%;
		padding: 1em;
		border-radius: 7px;
		color: white;
		background-color: rgb(217, 119, 6);
	}

	input[type="checkbox"] {
		margin-right: 0.5em;
	}

	span.required {
		color: #831843;
		font-weight: bold;
		margin-left: 0.5em;
	}

	.center {
		text-align: center;
	}

	@include mq(md) {
		padding: 1em;
	}
}
</style>
