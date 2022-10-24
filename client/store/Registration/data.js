export const state = () => ({
	age: [
		{ value: 0, display: "10歳未満" },
		{ value: 1, display: "10代" },
		{ value: 2, display: "20代" },
		{ value: 3, display: "30代" },
		{ value: 4, display: "40代" },
		{ value: 5, display: "50代" },
		{ value: 6, display: "60代" },
		{ value: 7, display: "70代" },
		{ value: 8, display: "80歳以上" },
	],
	job: [
		{ value: 1, display: "未就学児" },
		{ value: 2, display: "小学生" },
		{ value: 3, display: "中学生" },
		{ value: 4, display: "高校生" },
		{ value: 5, display: "大学生" },
		{ value: 6, display: "その他の学生" },
		{ value: 7, display: "会社員" },
		{ value: 8, display: "教職員" },
		{ value: 9, display: "自営業" },
		{ value: 10, display: "その他" },
	],
	major_subject: [
		{ value: 1, display: "情報系" },
		{ value: 2, display: "理系" },
		{ value: 3, display: "文系" },
		{ value: 4, display: "その他" },
	],
	gender: [
		{ value: 1, display: "男性" },
		{ value: 2, display: "女性" },
		{ value: 3, display: "その他" },
		{ value: 4, display: "指定しない" },
	],
	address: [
		{ value: 1, display: "東京都（北区）" },
		{ value: 2, display: "東京都（23区）" },
		{ value: 3, display: "東京都（市部）" },
		{ value: 4, display: "埼玉県（川口）" },
		{ value: 5, display: "埼玉県" },
		{ value: 6, display: "神奈川県" },
		{ value: 7, display: "茨城県" },
		{ value: 8, display: "栃木県" },
		{ value: 9, display: "群馬県" },
		{ value: 10, display: "千葉県" },
		{ value: 11, display: "北海道" },
		{ value: 12, display: "青森県" },
		{ value: 13, display: "岩手県" },
		{ value: 14, display: "宮城県" },
		{ value: 15, display: "秋田県" },
		{ value: 16, display: "山形県" },
		{ value: 17, display: "福島県" },
		{ value: 18, display: "新潟県" },
		{ value: 19, display: "富山県" },
		{ value: 20, display: "石川県" },
		{ value: 21, display: "福井県" },
		{ value: 22, display: "山梨県" },
		{ value: 23, display: "長野県" },
		{ value: 24, display: "岐阜県" },
		{ value: 25, display: "静岡県" },
		{ value: 26, display: "愛知県" },
		{ value: 27, display: "三重県" },
		{ value: 28, display: "滋賀県" },
		{ value: 29, display: "京都府" },
		{ value: 30, display: "大阪府" },
		{ value: 31, display: "兵庫県" },
		{ value: 32, display: "奈良県" },
		{ value: 33, display: "和歌山県" },
		{ value: 34, display: "鳥取県" },
		{ value: 35, display: "島根県" },
		{ value: 36, display: "岡山県" },
		{ value: 37, display: "広島県" },
		{ value: 38, display: "山口県" },
		{ value: 39, display: "徳島県" },
		{ value: 40, display: "香川県" },
		{ value: 41, display: "愛媛県" },
		{ value: 42, display: "高知県" },
		{ value: 43, display: "福岡県" },
		{ value: 44, display: "佐賀県" },
		{ value: 45, display: "長崎県" },
		{ value: 46, display: "熊本県" },
		{ value: 47, display: "大分県" },
		{ value: 48, display: "宮崎県" },
		{ value: 49, display: "鹿児島県" },
		{ value: 50, display: "沖縄県" },
	],
	know_about: ["東洋大学ホームページ", "駅広告", "地域の施設での広告", "学校に配布されたチラシ", "テレビ", "Twitter広告", "友人・知人より", "その他"],
	namecard: [],
})

export const mutations = {
	add(state, payload) {
		state.namecard = payload
	},
	remove(state) {
		state.namecard = []
	},
}

export const getters = {
	get(state) {
		return {
			age: state.age,
			job: state.job,
			major_subject: state.major_subject,
			gender: state.gender,
			address: state.address,
			know_about: state.know_about,
			namecard: state.namecard,
		}
	},
}

export const actions = {
	addAction({ commit, dispatch, state }, payload) {
		commit("remove")
		commit("add", payload)
	},
	removeAction({ commit, dispatch, state }, payload) {
		commit("remove")
	},
}
