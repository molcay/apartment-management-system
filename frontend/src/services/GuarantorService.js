import api from '../clients/API'

export default class GuarantorService {
  static async getAll() {
    return await api.getGuarantors()
  }

  static async getById() {
    return Promise.resolve(1) // TODO: implement this
  }
}