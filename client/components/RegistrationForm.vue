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
					<p>INIAD生が普段着用しているINIADネームカードの大学祭特別仕様版を来場者の皆様にご着用してもらうことになりました！お渡しするネームカードにはニックネームとQRコードが印刷されています。印刷されているQRコードは複数の企画と連動しています。ニックネームのご入力とカードデザインの選択をお願いいたします。</p>
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
								<input v-model="formdata.namecard" :value="i.id" type="radio" required />
								<p>{{ i.name }}</p>
								<div class="namecard-sample">
									<img :src="i.img" :alt="i.name" />
								</div>
								<p>{{ i.description }}</p>
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
						<p><input v-model="formdata.address" type="text" placeholder="東京都北区" required @focus="removeError('address')" /></p>
					</label>
					<label class="zip-left">
						<p>郵便番号から検索場合はこちら</p>
						<p><input v-model="zip" type="text" placeholder="1150053" @focus="removeError('zip')" @input="findaddress" /></p>
					</label>
					<p v-if="error.zip" class="error">⚠{{ error.zip }}</p>
				</section>

				<section style="clear: both">
					<p>ご年代</p>
					<select v-model="formdata.age" required>
						<option value="0">10歳未満</option>
						<option value="1">10代</option>
						<option value="2">20代</option>
						<option value="3">30代</option>
						<option value="4">40代</option>
						<option value="5">50代</option>
						<option value="6">60代</option>
						<option value="7">70代</option>
						<option value="8">80歳以上</option>
					</select>
				</section>

				<section>
					<p>ご職業</p>
					<select v-model="formdata.job" required>
						<option v-for="(i, index) in list.job" :key="index" :value="i">
							{{ i }}
						</option>
					</select>
				</section>

				<section>
					<p>入場予定日</p>
					<p v-for="(i, index) in list.admission_date" :key="index">
						<label> <input v-model="formdata.admission_date" :value="i.data" type="checkbox" />{{ i.display }}</label>
					</p>
					<ul>
						<li>現段階のご予定で構いません。ご指定していない日付も入場可能です。</li>
					</ul>
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
								<li>第三者提供は一切致しません</li>
							</ul>
						</li>
					</ol>
					<p>ご不明点等ございましたら以下の連絡先にご連絡ください。</p>
					<div class="contact">
						<p>〒115-0053</p>
						<p>東京都北区赤羽台東京都北区赤羽台1丁目7-11</p>
						<p>support@iniadfes.com</p>
					</div>
					<div class="center">
						<label class="center"><input v-model="formdata.agree" type="checkbox" />以上の内容を確認しました。</label>
					</div>
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
				nemacard: "",
				address: "",
				age: "2",
				job: "大学生",
				know_about: [],
				admission_date: [],
				agree: false,
			},
			error: {
				last_name: "",
				first_name: "",
				ruby_last_name: "",
				ruby_first_name: "",
				email: "",
				nickname: "",
				nemacard: "",
				zip: "",
				address: "",
				age: "",
				job: "",
				know_about: "",
				admission_date: "",
				agree: "",
			},
			zip: "",
			list: {
				namecard: [],
				job: ["未就学児", "小学生", "中学生", "高校生", "大学生", "大学関係者", "会社員", "教職員", "自営業", "その他"],
				know_about: ["東洋大学ホームページ", "駅広告", "地域の施設での広告", "学校に配布されたチラシ", "YouTube広告", "Twitter広告", "友人・知人より", "その他"],
				admission_date: [
					{
						data: "2022-10-29",
						display: "2022/10/29(土)",
					},
					{
						data: "2022-10-30",
						display: "2022/10/30(日)",
					},
				],
			},
		}
	},
	methods: {
		submit() {},
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
		findaddress() {
			if (this.zip.length === 7) {
				this.$axios.get(`https://zipcloud.ibsnet.co.jp/api/search?zipcode=${this.zip}`).then((res) => {
					if (res.data.results) {
						this.formdata.address = `${res.data.results[0].address1}${res.data.results[0].address2}`
						this.error.zip = ""
					} else {
						this.error.zip = "郵便番号が見つかりませんでした"
					}
				})
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

				&.zip-left {
					width: 40%;
					float: left;
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
