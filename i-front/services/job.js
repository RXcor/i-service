export default class {
  constructor(app) {
    this.app = app;
  }

  create(data) {
    return this.app.$axios.post('jobs/', data);
  }
}
