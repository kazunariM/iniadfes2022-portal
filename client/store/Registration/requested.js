export const state = () => ({
	requested: false,
})

export const mutations = {
	change(state, payload) {
		state.requested = payload.requested
	},
}

export const getters = {
	get(state) {
		return {
			requested: state.requested,
		}
	},
}

export const actions = {
	changeAction({ commit, dispatch, state }, payload) {
		commit("change", payload)
	},
}
