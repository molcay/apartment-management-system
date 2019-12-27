import VueRouter from 'vue-router'

import Home from './pages/home/Home'
import IssueList from './pages/issues/List'
import RoomList from './pages/rooms/List'
import TenantList from './pages/tenants/List'
import AgreementList from './pages/agreements/List'
import GuarantorList from './pages/guarantors/List'
import LandlordList from './pages/landlords/List'
import CouponList from './pages/coupons/List'
import CreateRoom from './pages/rooms/Create'
import CreateLandlord from './pages/landlords/Create'
import CreateTenant from './pages/tenants/Create'
import CreateGuarantor from './pages/guarantors/Create'
import CreateAgreement from './pages/agreements/Create'
import CreateCoupon from './pages/coupons/Create'
import DetailedAgreement from './pages/agreements/Details'
import DetailedLandlord from './pages/landlords/Details'
import DetailedGuarantor from './pages/guarantors/Details'
import DetailedRoom from './pages/rooms/Details'
import DetailedTenant from './pages/tenants/Details'
import DetailedCoupon from './pages/coupons/Details'
import DetailedIssue from './pages/issues/Details'
import EditedLandlord from './pages/landlords/Edit'
import EditedGuarantor from './pages/guarantors/Edit'
import EditedRoom from './pages/rooms/Edit'
import EditedTenant from './pages/tenants/Edit'
import EditedAgreement from './pages/agreements/Edit'
import EditedCoupon from './pages/coupons/Edit'
import EditedIssue from './pages/issues/Edit'
import SignUp from './pages/accounts/SignUp'
import Login from './pages/accounts/Login'
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
      path: '/giris',
      component: Login,
    },
    {
      path: tr_to_ascii('/yonetim/arızalar'),
      component: IssueList,
    },
    {
      path: tr_to_ascii('/yonetim/arızalar/:id/detay'),
      component: DetailedIssue,
    },
    {
      path: tr_to_ascii('/yonetim/arızalar/:id/düzenle'),
      component: EditedIssue,
    },
    {
      path: '/yonetim/odalar',
      component: RoomList,
    },
    {
      path: '/yonetim/odalar/ekle',
      component: CreateRoom,
    },
    {
      path: '/yonetim/odalar/:id/detay',
      component: DetailedRoom,
    },
    {
      path: tr_to_ascii('/yonetim/odalar/:id/düzenle'),
      component: EditedRoom,
    },
    {
      path: tr_to_ascii('/yonetim/kiracılar'),
      component: TenantList,
    },
    {
      path: tr_to_ascii('/yonetim/kiracılar/ekle'),
      component: CreateTenant,
    },
    {
      path: tr_to_ascii('/yonetim/kiracılar/:id/detay'),
      component: DetailedTenant,
    },
    {
      path: tr_to_ascii('/yonetim/kiracılar/:id/düzenle'),
      component: EditedTenant,
    },
    {
      path: '/yonetim/arama',
      component: SearchResult,
    },
    {
      path: tr_to_ascii('/yonetim/sözleşmeler'),
      component: AgreementList,
    },
    {
      path: tr_to_ascii('/yonetim/sözleşmeler/ekle'),
      component: CreateAgreement,
    },
    {
      path: tr_to_ascii('/yonetim/sözleşmeler/:id/detay'),
      component: DetailedAgreement,
    },
    {
      path: tr_to_ascii('/yonetim/sözleşmeler/:id/düzenle'),
      component: EditedAgreement,
    },
    {
      path: '/yonetim/kefiller',
      component: GuarantorList,
    },
    {
      path: '/yonetim/kefiller/ekle',
      component: CreateGuarantor,
    },
    {
      path: '/yonetim/kefiller/:id/detay',
      component: DetailedGuarantor,
    },
    {
      path: tr_to_ascii('/yonetim/kefiller/:id/düzenle'),
      component: EditedGuarantor,
    },
    {
      path: tr_to_ascii('/yonetim/mülk_sahipleri'),
      component: LandlordList,
    },
    {
      path: tr_to_ascii('/yonetim/mülk_sahipleri/ekle'),
      component: CreateLandlord,
    },
    {
      path: tr_to_ascii('/yonetim/mülk_sahipleri/:id/detay'),
      component: DetailedLandlord,
    },
    {
      path: tr_to_ascii('/yonetim/mülk_sahipleri/:id/düzenle'),
      component: EditedLandlord,
    },
    {
      path: tr_to_ascii('/yonetim/kuponlar'),
      component: CouponList,
    },
    {
      path: tr_to_ascii('/yonetim/kuponlar/ekle'),
      component: CreateCoupon,
    },
    {
      path: tr_to_ascii('/yonetim/kuponlar/:id/detay'),
      component: DetailedCoupon,
    },
    {
      path: tr_to_ascii('/yonetim/kuponlar/:id/düzenle'),
      component: EditedCoupon,
    },
  ]
})

export default router
