import api from '../clients/API'

export default class RoomService {
  static async getAll() {
    const rooms = await api.getRooms()
    return rooms.map((room) => {
      return {
        ...room,
        name: `${room.building_number}/${room.home_number}-${room.room_number}`,
      }
    })
  }

  static async getById() {
    return Promise.resolve(1) // TODO: implement this
  }
}
