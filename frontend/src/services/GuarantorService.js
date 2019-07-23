import api from '../clients/API'

export default class GuarantorService {
  static async getAll() {
    const guarantors = await api.getGuarantors()
    return guarantors.map(guarantor => {
      return {
        ...guarantor,
        full_name: `${guarantor.first_name} ${guarantor.last_name}`,
      }
    })
  }

  static async getById() {
    return Promise.resolve(1) // TODO: implement this
  }
}
