<template>
	<article>
		<form @submit.prevent="submit">
			<fieldset>
				<section>
					<h3>お名前</h3>
					<label class="name-left">
						<p>姓</p>
						<p>
							<input v-model="formdata.last_name" type="text" placeholder="赤羽台" required @focus="removeError('last_name')" />
						</p>
					</label>
					<label class="name-right">
						<p>名</p>
						<p>
							<input v-model="formdata.first_name" type="text" placeholder="太郎" required @focus="removeError('first_name')" />
						</p>
					</label>
					<label class="name-left">
						<p>カナ(姓)</p>
						<p>
							<input v-model="formdata.ruby_last_name" type="text" placeholder="アカバネダイ" required @focus="removeError('ruby_last_name')" />
						</p>
					</label>
					<label class="name-right">
						<p>カナ(名)</p>
						<p>
							<input v-model="formdata.ruby_first_name" type="text" placeholder="タロウ" required @focus="removeError('ruby_first_name')" />
						</p>
					</label>
				</section>
			</fieldset>

			<fieldset>
				<section>
					<h3>ご連絡先</h3>
					<label>
						<p>メールアドレス</p>
						<p>
							<input v-model="formdata.email" type="email" placeholder="sample@example.com" required @focus="removeError('email')" @blur="checkEmail" />
						</p>
					</label>
					<p v-if="error.email" class="error">⚠{{ error.email }}</p>
					<ul class="notice">
						<li>事前登録完了時に登録完了のメールを送信いたします。</li>
						<li>感染症クラスター等発生時にご連絡用として使います。</li>
					</ul>
				</section>
			</fieldset>

			<fieldset>
				<section>
					<h3>カスタムINIADネームカード</h3>
					<p>INIAD生が普段着用しているINIADネームカードの大学祭特別仕様版を来場者の皆様にご着用してもらうことになりました！お渡しするネームカードにはニックネームと二次元コードが印刷されています。印刷されている二次元コードは複数の企画と連動しています。ニックネームのご入力とカードデザインの選択をお願いいたします。</p>
					<label>
						<p>ニックネーム</p>
						<p>
							<input v-model="formdata.nickname" type="text" placeholder="†いにゃー-BlueEyes-†" required @focus="removeError('nickname')" @blur="checkNickname" />
						</p>
					</label>
					<p v-if="error.nickname" class="error">⚠{{ error.nickname }}</p>
					<ul class="notice">
						<li>ネームカードに印刷されます。他人に見せることが可能なニックネームの入力をお願いいたします。</li>
						<li>16字以内でお願いいたします。</li>
					</ul>
				</section>

				<section>
					<p>デザイン</p>
					<ul class="namecard-design">
						<li v-for="(i, index) in list.namecard" :key="index" class="namecardbox">
							<label>
								<input v-model="formdata.design" :value="i.uuid" type="radio" required />
								<p>{{ i.name }}</p>
								<div class="namecard-sample">
									<img :src="i.img" :alt="i.name" />
								</div>
								<p>{{ i.text }}</p>
							</label>
						</li>
					</ul>
				</section>
			</fieldset>

			<fieldset>
				<section>
					<h3>アンケート</h3>
					<label>
						<p>お住まい(都道府県)</p>
						<select v-model="formdata.address" required>
							<option v-for="(i, index) in list.address" :key="index" :value="i.value">
								{{ i.display }}
							</option>
						</select>
					</label>
				</section>

				<section>
					<p>性別</p>
					<select v-model="formdata.gender" required>
						<option v-for="(i, index) in list.gender" :key="index" :value="i.value">
							{{ i.display }}
						</option>
					</select>
				</section>

				<section>
					<p>ご年代</p>
					<select v-model="formdata.age" required>
						<option v-for="(i, index) in list.age" :key="index" :value="i.value">
							{{ i.display }}
						</option>
					</select>
				</section>

				<section>
					<p>ご職業</p>
					<select v-model="formdata.job" required>
						<option v-for="(i, index) in list.job" :key="index" :value="i.value">
							{{ i.display }}
						</option>
					</select>
				</section>

				<section v-if="formdata.job == 4 || formdata.job == 5">
					<p>専攻/希望分野</p>
					<select v-model="formdata.major_subject">
						<option v-for="(i, index) in list.major_subject" :key="index" :value="i.value">
							{{ i.display }}
						</option>
					</select>
				</section>

				<section>
					<p>INIAD-FES・WELLB-FES・このポータルサイトはどこで知りましたか？</p>
					<p v-for="(i, index) in list.know_about" :key="index">
						<label> <input v-model="formdata.know_about" :value="i" type="checkbox" />{{ i }}</label>
					</p>
				</section>
			</fieldset>

			<fieldset>
				<section class="confirm">
					<h3>個人情報取り扱いについて(必ずご確認ください)</h3>
					<ol>
						<li>
							利用目的
							<ul>
								<li>大学祭「INIAD-FES」「WELLB-FES」を運営するため</li>
								<li>次年度以降の大学祭の参考のため</li>
								<li>感染症クラスター発生時にご連絡するため</li>
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
						<p>support@iniadfes.com</p>
					</div>
					<div class="center">
						<label class="center"><input v-model="formdata.agree" type="checkbox" @focus="removeError('agree')" />以上の内容を確認しました。</label>
					</div>
					<p v-if="error.agree" class="error">⚠{{ error.agree }}</p>
				</section>
			</fieldset>
			<div class="center">
				<button type="submit">入力内容を確認する</button>
			</div>
		</form>
	</article>
</template>

<script>
export default {
	name: "RegistrationForm",
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
			error: {
				last_name: "",
				first_name: "",
				ruby_last_name: "",
				ruby_first_name: "",
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
	created() {
		const getListdata = this.$store.getters["Registration/data/get"]
		this.list.age = getListdata.age
		this.list.job = getListdata.job
		this.list.major_subject = getListdata.major_subject
		this.list.gender = getListdata.gender
		this.list.address = getListdata.address
		this.list.know_about = getListdata.know_about
		this.list.namecard = getListdata.namecard

		const getFormdata = this.$store.getters["Registration/get"]
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
		this.formdata.agree = false

		const getErrordata = this.$store.getters["Registration/error/get"]
		this.error.last_name = getErrordata.last_name
		this.error.first_name = getErrordata.first_name
		this.error.ruby_last_name = getErrordata.ruby_last_name
		this.error.ruby_first_name = getErrordata.ruby_first_name
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
			const match = this.formdata.email.match(/^[A-Za-z0-9]{1}[A-Za-z0-9_.-]*@{1}[A-Za-z0-9_.-]+\.[A-Za-z0-9]+$/)
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
	width: 95%;
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
					background-color: #ccc;
					padding: 5px;
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
						border-bottom: 15px solid #ccc;
						border-left: 15px solid transparent;
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

	input[type="checkbox"] {
		margin-right: 0.5em;
	}

	.center {
		text-align: center;
	}

	@include mq(md) {
		width: 80%;
		padding: 1em;
	}
}
</style>
