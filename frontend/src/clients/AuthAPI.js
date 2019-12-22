import axios from "axios"

class AuthAPI {
    static API_AUTH_PREFIX = "/auth"

    static get(path) {
        return axios.get(`${AuthAPI.API_AUTH_PREFIX}${path}`)
    }

    static post(path, data) {
        return axios.post(`${AuthAPI.API_AUTH_PREFIX}${path}`, data)
    }

    static put(path, data) {
        return axios.put(`${AuthAPI.API_AUTH_PREFIX}${path}`, data)
    }

    static delete(path) {
        return axios.delete(`${AuthAPI.API_AUTH_PREFIX}${path}`)
    }

    createUser(newUser) {
        return AuthAPI.post("/users/", newUser)
    }

    loginUser(userLogin) {
        return AuthAPI.post("/token/login/", userLogin)
    }
}

const authAPI = new AuthAPI()

export default authAPI
