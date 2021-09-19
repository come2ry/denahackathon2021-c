export const state = () => ({
  locus: [],
})

export const mutations = {
  add(state, data) {
    state.locus = data
  },
}

export const actions = {
  async fetch({ commit, state }) {
    if (!state.locus.length) {
      const res = await this.$axios.$get('/locus/1')
      commit('add', res.data)
    }
  },
}
