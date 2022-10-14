export const state = () => ({
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
})

export const mutations = {
	add(state, payload) {
		state.email = payload.email
		state.nickname = payload.nickname
		state.design = payload.design
		state.address = payload.address
		state.gender = payload.gender
		state.age = payload.age
		state.job = payload.job
		state.major_subject = payload.major_subject
		state.know_about = payload.know_about
		state.agree = payload.agree
	},
	remove(state) {
		state.email = ""
		state.nickname = ""
		state.design = ""
		state.address = null
		state.gender = null
		state.age = null
		state.job = null
		state.major_subject = null
		state.know_about = []
		state.agree = false
	},
}

export const getters = {
	get(state) {
		return {
			email: state.email,
			nickname: state.nickname,
			design: state.design,
			address: state.address,
			gender: state.gender,
			age: state.age,
			job: state.job,
			major_subject: state.major_subject,
			know_about: state.know_about,
			agree: state.agree,
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
