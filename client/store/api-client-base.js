export const state = () => ({
  users: [],
})

export const mutations = {
  add(state, data) {
    state.users = data
  },
}

export const actions = {
  async fetch({ commit, state }) {
    if (!state.users.length) {
      const res = await this.$axios.$get('/geo')
      commit('add', res.data)
    }
  },
}
