import api from '../clients/API'

export default class LandlordService {
  static async getAll() {
    return await api.getLandlords()
  }

  static async getById() {
    return Promise.resolve(1) // TODO: implement this
  }
}
