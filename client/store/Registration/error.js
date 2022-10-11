export const state = () => ({
	email: "",
	nickname: "",
	design: "",
	address: "",
	gender: "",
	age: "",
	job: "",
	major_subject: "",
	know_about: "",
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
	},
	remove(state) {
		state.email = ""
		state.nickname = ""
		state.design = ""
		state.address = ""
		state.gender = ""
		state.age = ""
		state.job = ""
		state.major_subject = ""
		state.know_about = ""
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
