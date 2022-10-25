export const state = () => ({
	now: null,
})

export const mutations = {
	set(state, payload) {
		state.now = payload
	},
}

export const getters = {
	get(state) {
		return {
			now: state.now,
		}
	},
}

export const actions = {
	setAction({ commit, dispatch, state }, payload) {
		commit("set", payload)
	},
}
