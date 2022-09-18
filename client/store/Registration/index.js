export const state = () => ({
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
})

export const mutations = {
	add(state, payload) {
		state.last_name = payload.last_name
		state.first_name = payload.first_name
		state.ruby_last_name = payload.ruby_last_name
		state.ruby_first_name = payload.ruby_first_name
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
		state.last_name = ""
		state.first_name = ""
		state.ruby_last_name = ""
		state.ruby_first_name = ""
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
			last_name: state.last_name,
			first_name: state.first_name,
			ruby_last_name: state.ruby_last_name,
			ruby_first_name: state.ruby_first_name,
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
