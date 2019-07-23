import api from '../clients/API'

export default class TenantService {
  static async getAll() {
    const tenants = await api.getTenants()
    return tenants.map(tenant => {
      return {
        ...tenant,
        full_name: `${tenant.first_name} ${tenant.last_name}`,
      }
    })
  }

  static async getById() {
    return Promise.resolve(1) // TODO: implement this
  }
}
