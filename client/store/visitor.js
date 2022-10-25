export const state = () => ({
	userid: null,
	nickname: null,
})

export const mutations = {
	regUserid(state, payload) {
		state.userid = payload
	},

	regNickname(state, payload) {
		state.nickname = payload
	},
}

export const getters = {
	get(state) {
		return {
			userid: state.userid,
			nickname: state.nickname,
		}
	},
}

export const actions = {
	setBase({ commit }, payload) {
		commit("regUserid", payload.qrid)
		commit("regNickname", payload.nickname)
	},
}
