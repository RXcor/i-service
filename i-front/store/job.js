export const state = () => {
  return {
    job: {
      id: null,
      data: null,
      result: null,
      is_completed: null,
      progress: null,
      type_of: null
    }
  }
};

export const mutations = {
  updateInstance (state, instanceData) {
    Object.assign(state.raffle, instance)
  },
  setData (state, data) {
    state.job.data = data;
  },
  setTypeOf (state, type) {
    state.job.type_of = type;
  }
};
export const actions = {
  // async getRaffle (state, id) {
  //   const resp = await this.app.$usersService.getById(id);
  //   state.commit('setUser', resp.data);
  // }
};
