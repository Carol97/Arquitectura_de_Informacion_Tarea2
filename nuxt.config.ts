// nuxt.config.ts
export default defineNuxtConfig({
  modules: ['@nuxt/content'],
  app: {
    head: {
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { hid: 'description', name: 'description', content: 'Catálogo de Laptops' }
      ],
       link: [
        { rel: 'stylesheet', href: 'https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.min.css' },
        { rel: 'stylesheet', href: 'https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css' }
      ]
    }
  },
   nitro: { preset: 'static', prerender: { crawlLinks: true } },
  routeRules: { '/**': { prerender: true } }
})
