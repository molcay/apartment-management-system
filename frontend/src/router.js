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
import DetailedLandlord from './pages/landlords/Details'
import DetailedGuarantor from './pages/guarantors/Details'
import DetailedRoom from './pages/rooms/Details'
import DetailedTenant from './pages/tenants/Details'
import EditedLandlord from './pages/landlords/Edit'
import EditedGuarantor from './pages/guarantors/Edit'
import EditedRoom from './pages/rooms/Edit'
import EditedTenant from './pages/tenants/Edit'
import EditedAgreement from './pages/agreements/Edit'
import SignUp from './pages/accounts/SignUp'
import SearchResult from './pages/SearchResult'

import {tr_to_ascii} from "./helper"

const router = new VueRouter({
  mode: 'hash',
  routes: [
    {
      path: '/',
      component: Home,
    },
    {
      path: '/kaydol',
      component: SignUp,
    },
    {
      path: '/odalar',
      component: RoomList,
    },
    {
      path: '/odalar/ekle',
      component: CreateRoom,
    },
    {
      path: '/odalar/:id/detay',
      component: DetailedRoom,
    },
    {
      path: tr_to_ascii('/odalar/:id/düzenle'),
      component: EditedRoom,
    },
    {
      path: tr_to_ascii('/kiracılar'),
      component: TenantList,
    },
    {
      path: tr_to_ascii('/kiracılar/ekle'),
      component: CreateTenant,
    },
    {
      path: tr_to_ascii('/kiracılar/:id/detay'),
      component: DetailedTenant,
    },
    {
      path: tr_to_ascii('/kiracılar/:id/düzenle'),
      component: EditedTenant,
    },
    {
      path: '/arama',
      component: SearchResult,
    },
    {
      path: tr_to_ascii('/sözleşmeler'),
      component: AgreementList,
    },
    {
      path: tr_to_ascii('/sözleşmeler/ekle'),
      component: CreateAgreement,
    },
    {
      path: tr_to_ascii('/sözleşmeler/:id/detay'),
      component: DetailedAgreement,
    },
    {
      path: tr_to_ascii('/sözleşmeler/:id/düzenle'),
      component: EditedAgreement,
    },
    {
      path: '/kefiller',
      component: GuarantorList,
    },
    {
      path: '/kefiller/ekle',
      component: CreateGuarantor,
    },
    {
      path: '/kefiller/:id/detay',
      component: DetailedGuarantor,
    },
    {
      path: tr_to_ascii('/kefiller/:id/düzenle'),
      component: EditedGuarantor,
    },
    {
      path: tr_to_ascii('/mülk_sahipleri'),
      component: LandlordList,
    },
    {
      path: tr_to_ascii('/mülk_sahipleri/ekle'),
      component: CreateLandlord,
    },
    {
      path: tr_to_ascii('/mülk_sahipleri/:id/detay'),
      component: DetailedLandlord,
    },
    {
      path: tr_to_ascii('/mülk_sahipleri/:id/düzenle'),
      component: EditedLandlord,
    },
  ]
})

export default router
