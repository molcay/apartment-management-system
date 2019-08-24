import axios from "axios"

class API {
  static API_V1_PREFIX = '/api/v1'

  static get(path) {
    return axios.get(`${API.API_V1_PREFIX}${path}`)
  }

  static post(path, data) {
    return axios.post(`${API.API_V1_PREFIX}${path}`, data)
  }

  static put(path, data) {
    return axios.put(`${API.API_V1_PREFIX}${path}`,data)
  }

  static delete(path) {
    return axios.delete(`${API.API_V1_PREFIX}${path}`)
  }

  getAgreements() {
    return API.get('/agreements')
      .then(function (response) {
        return response.data
      })
      .catch(function (error) {
        return error
      })
      .finally(function () {
        // always executed
      })
  }

  getGuarantors() {
    return API.get('/guarantors')
      .then(function (response) {
        return response.data
      })
      .catch(function (error) {
        return error
      })
      .finally(function () {
        // always executed
      })
  }

  getLandlords() {
    return API.get('/landlords')
      .then(function (response) {
        return response.data
      })
      .catch(function (error) {
        return error
      })
      .finally(function () {
        // always executed
      })
  }

  getRooms() {
    return API.get('/rooms')
      .then(function (response) {
        return response.data
      })
      .catch(function (error) {
        return error
      })
      .finally(function () {
        // always executed
      })
  }

  getTenants() {
    return API.get('/tenants')
      .then(function (response) {
        return response.data
      })
      .catch(function (error) {
        return error
      })
      .finally(function () {
        // always executed
      })
  }

  getAgreement(id) {
    return API.get(`/agreements/${id}/`)
      .then(response => response.data)
      .catch(error => error)
      .finally()
  }

  getGuarantor(id) {
    return API.get(`/guarantors/${id}/`)
      .then(response => response.data)
      .catch(error => error)
      .finally()
  }

  getLandlord(id) {
    return API.get(`/landlords/${id}/`)
      .then(response => response.data)
      .catch(error => error)
      .finally()
  }

  getRoom(id) {
    return API.get(`/rooms/${id}/`)
      .then(response => response.data)
      .catch(error => error)
      .finally()
  }

  getTenant(id) {
    return API.get(`/tenants/${id}/`)
      .then(response => response.data)
      .catch(error => error)
      .finally()
  }

  saveAgreement() {
    return API.post(``)
      .then(response => response.data)
      .catch(error => error)
      .finally()
  }

  saveGuarantor(id, newGuarantor) {
    return API.put(`/guarantors/${id}/`, newGuarantor)
      .then(response => response.data)
      .catch(error => error)
      .finally()
  }

  saveLandlord(id, newLandlord) {
    return API.put(`/landlords/${id}/`, newLandlord)
      .then(response => response.data)
      .catch(error => error)
      .finally()
  }

  saveRoom(id, newRoom) {
    return API.put(`/rooms/${id}/`, newRoom)
  }

  saveTenant(id, newTenant) {
    return API.put(`/tenants/${id}/`, newTenant)
  }

  deleteAgreement() {
    return API.delete(``)
  }

  deleteGuarantor(id) {
    return API.delete(`/guarantors/${id}/`)
  }

  deleteLandlord(id) {
    return API.delete(`/landlords/${id}/`)
  }

  deleteRoom(id) {
    return API.delete(`/rooms/${id}/`)
  }

  deleteTenant(id) {
    return API.delete(`/tenants/${id}`)
  }
}

const api = new API()

export default api
