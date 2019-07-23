import VueRouter from 'vue-router'

import Home from './pages/home/Home'
import RoomList from './pages/rooms/List'
import TenantList from './pages/tenants/List'
import AgreementList from './pages/agreements/List'
import GuarantorList from './pages/guarantors/List'
import LandlordList from './pages/landlords/List'
import CreateRoom from './pages/rooms/Create'
import CreateLandlord from './pages/landlords/Create'
import CreateTenant from './pages/tenants/Create'
import CreateGuarantor from './pages/guarantors/Create'
import CreateAgreement from './pages/agreements/Create'
import DetailedAgreement from './pages/agreements/Details'

import {tr_to_ascii} from "./helper"

const router = new VueRouter({
  mode: 'hash',
  routes: [
    {
      path: '/',
      component: Home,
    },
    {
      path: '/odalar',
      component: RoomList,
    },
    {
      path: tr_to_ascii('/kiracılar'),
      component: TenantList,
    },
    {
      path: tr_to_ascii('/sözleşmeler'),
      component: AgreementList,
    },
    {
      path: '/kefiller',
      component: GuarantorList,
    },
    {
      path: tr_to_ascii('/mülk_sahipleri'),
      component: LandlordList,
    },
    {
      path: '/odalar/ekle',
      component: CreateRoom,
    },
    {
      path: tr_to_ascii('/mülk_sahipleri/ekle'),
      component: CreateLandlord,
    },
    {
      path: tr_to_ascii('/kiracılar/ekle'),
      component: CreateTenant,
    },
    {
      path: '/kefiller/ekle',
      component: CreateGuarantor,
    },
    {
      path: tr_to_ascii('/sözleşmeler/ekle'),
      component: CreateAgreement,
    },
    {
      path: tr_to_ascii('/sözleşmeler/:id/detay'),
      component: DetailedAgreement,
    },
  ]
})

export default router
