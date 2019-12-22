<template>
  <div id="app">
    <nav class="navbar is-info is-large">
      <div class="navbar-brand">
        <a
          class="navbar-item"
          href="/"
        >
          <img
            src="logo.png"
            alt="__APART_ADI__"
          >
        </a>
        <div
          class="navbar-burger burger"
          data-target="navbarExampleTransparentExample"
        >
          <span />
          <span />
          <span />
        </div>
      </div>
      <div class="navbar-end">
        <div class="navbar-item">
          <div class="field has-addons">
            <div class="control">
              <input
                v-model="searchQuery"
                class="input"
                type="text"
                placeholder="Oda, Kiracı, Kefil Bul"
                required
              >
            </div>
            <div class="control">
              <button
                class="button is-link"
                @click="search()"
              >
                <span class="icon is-small"><i class="fa fa-search" /></span>
              </button>
            </div>
          </div>
        </div>
        <div class="navbar-item">
          <router-link to="/kaydol">
            <span class="fas fa-user" /> Sign Up
          </router-link>
        </div>
        <div class="navbar-item">
          <router-link to="/giris">
            <span class="fas fa-sign-in-alt" /> Login
          </router-link>
        </div>
      </div>
    </nav>
    <section class="section">
      <div class="container">
        <Tabs :routes="tabRoutes" />
        <div class="columns">
          <div class="column">
            <router-view />
            {{ $route.path }}
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
  import * as bulmaToast from 'bulma-toast'
  //import api from "./clients/API"

  import Tabs from './components/Tabs'
  import {tr_to_ascii} from './helper'

  const tabRoutes = [
    {
      text: 'Odalar',
      path: '/yonetim/odalar',
      icon: 'fas fa-bed',
    },
    {
      text: 'Kiracılar',
      path: tr_to_ascii('/yonetim/kiracılar'),
      icon: 'fas fa-user-alt',
    },
    {
      text: 'Sözleşmeler',
      path: tr_to_ascii('/yonetim/sözleşmeler'),
      icon: 'fas fa-handshake',
    },
    {
      text: 'Kefiller',
      path: '/yonetim/kefiller',
      icon: 'fas fa-users',
    },
    {
      text: 'Mülk Sahipleri',
      path: tr_to_ascii('/yonetim/mülk_sahipleri'),
      icon: 'fas fa-building',
    },    {
      text: 'Arızalar',
      path: tr_to_ascii('/arızalar'),
      icon: 'fas fa-wrench',
    },
  ]

  export default {
    name: 'App',
    components: {
      Tabs,
    },
    data() {
      return {
        searchQuery: '',
        tabRoutes: tabRoutes,
      }
    },
    methods: {
      async search() {
        if (this.searchQuery && this.searchQuery.length > 2) {
          bulmaToast.toast({
            message: `'${this.searchQuery}' aranıyor...`,
            type: 'is-success',
            animate: {
              in: 'fadeIn',
              out: 'fadeOut',
            },
            duration: 2000,
            position: "top-center",
            closeOnClick: true,
          })
          //`/arama?search=${this.searchQuery}`
          this.$router.push({path : '/arama', query : {search:`${this.searchQuery}`}})

        } else {
          bulmaToast.toast({
            message: `Aramak için en az 3 harf girmeniz gerekmektedir`,
            type: 'is-danger',
            position: "top-right",
            duration: 2500,
            dismissible: true,
          })
        }
      }
    }
  }
</script>

<style>
  .navbar-item img {
      max-height: 3rem !important;
  }
</style>