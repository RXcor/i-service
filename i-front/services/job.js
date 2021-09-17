export default class {
  constructor(app) {
    this.app = app;
  }
  getById(id) {
    return this.app.$axios.get(`jobs/${id}/`);
  }
  createJob(data) {
    return this.app.$axios.post('jobs/', data);
  }
}
