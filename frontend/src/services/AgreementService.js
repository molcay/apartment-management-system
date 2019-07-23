import api from '../clients/API'

export default class AgreementService {
  static async getAll() {
    return await api.getAgreements()
  }

  static async getById(id) {
    return api.getAgreement(id)
  }
}
