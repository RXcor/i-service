import Raffle from './job'

export default ({ app }, inject) => {
  inject('jobService', new Job(app));
}
