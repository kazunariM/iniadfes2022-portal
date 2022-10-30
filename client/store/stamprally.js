export const state = () => ({
	title: null,
	background: null,
	stamps: {
		0: {
			name: null,
			stamp: null,
		},
		1: {
			name: null,
			stamp: null,
		},
		2: {
			name: null,
			stamp: null,
		},
		3: {
			name: null,
			stamp: null,
		},
		4: {
			name: null,
			stamp: null,
		},
		5: {
			name: null,
			stamp: null,
		},
		6: {
			name: null,
			stamp: null,
		},
		7: {
			name: null,
			stamp: null,
		},
		8: {
			name: null,
			stamp: null,
		},
	},
})

export const mutations = {
	setBackground(state, payload) {
		state.title = payload.title
		state.background = payload.background
	},

	setItem(state, payload) {
		state.stamps[payload[0]].name = payload[1]
	},

	setImg(state, payload) {
		state.stamps[payload[0]].stamp = payload[1]
	},
}

export const getters = {
	get(state) {
		return {
			data: state,
		}
	},
}

export const actions = {
	setBack({ commit, dispatch, state }, payload) {
		commit("setBackground", payload)
	},
	setStamps({ commit, dispatch, state }, payload) {
		commit("setItem", payload)
	},
}
