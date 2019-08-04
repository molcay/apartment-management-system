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
  }

  getGuarantor(id) {
    return API.get(`/guarantors/${id}/`)
      .then(response => response.data)
      .catch(error => error)
  }

  getLandlord(id) {
    return API.get(`/landlords/${id}/`)
      .then(response => response.data)
      .catch(error => error)
  }

  getRoom(id) {
    return API.get(`/rooms/${id}/`)
      .then(response => response.data)
      .catch(error => error)
  }

  getTenant(id) {
    return API.get(`/tenants/${id}/`)
      .then(response => response.data)
      .catch(error => error)
  }

  saveAgreement() {
    return API.post(``)
      .then(response => response.data)
      .catch(error => error)
  }

  saveGuarantor() {
    return API.post(``)
      .then(response => response.data)
      .catch(error => error)
  }

  saveLandlord(id, newLandlord) {
    return API.put(`/landlords/${id}/`, newLandlord)
      .then(response => response.data)
      .catch(error => error)
  }

  saveRoom() {
    return API.post(``)
      .then(response => response.data)
      .catch(error => error)
  }

  saveTenant() {
    return API.post(``)
      .then(response => response.data)
      .catch(error => error)
  }

  deleteAgreement() {
    return API.delete(``)
      .then(response => response.data)
      .catch(error => error)
  }

  deleteGuarantor() {
    return API.delete(``)
      .then(response => response.data)
      .catch(error => error)
  }

  deleteLandlord(id) {
    return API.delete(`/tenants/${id}/`)
      .then(response => response.data)
      .catch(error => error)
  }

  deleteRoom() {
    return API.delete(``)
      .then(response => response.data)
      .catch(error => error)
  }

  deleteTenant() {
    return API.delete(``)
      .then(response => response.data)
      .catch(error => error)
  }
}

const api = new API()

export default api
