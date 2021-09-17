import Jobs from './job'

export default ({ app }, inject) => {
  inject('jobService', new Jobs(app));
}
