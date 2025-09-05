<script setup lang="ts">
const route = useRoute()
const facet = route.params.facet as string
const valor = decodeURIComponent(route.params.valor as string)

const fieldMap: Record<string, string> = {
  marca: 'marca',
  sistema: 'sistema_operativo',
  pantalla: 'tamano_pantalla',
  procesador: 'procesador'
}
const field = fieldMap[facet]
if (!field) {
  throw createError({ statusCode: 404, statusMessage: 'Criterio no válido' })
}

const { data: equipos } = await useAsyncData(
  `equipos-${facet}-${valor}`,
  async () => await queryContent('/laptops')
    .where({ [field]: valor })
    .only(['_path','title','marca','modelo','sistema_operativo','procesador','ram_gb','tamano_pantalla','precio'])
    .find()
)
</script>

<template>
  <div class="container">
    <HeaderView />
    <h3 style="margin-top: 15px">
      Laptops | <span style="text-transform: capitalize;">{{ facet }}:</span> {{ valor }}
    </h3>

    <ul v-if="equipos?.length">
      <li v-for="e in equipos" :key="e._path">
        <NuxtLink :to="e._path">{{ e.title }}</NuxtLink>
        <small>
          — {{ e.marca }} | {{ e.sistema_operativo }} | {{ e.procesador }}
          <span v-if="e.tamano_pantalla"> | {{ e.tamano_pantalla }}"</span>
          <span v-if="e.ram_gb"> | {{ e.ram_gb }} GB</span>
          <span v-if="e.precio"> | ${{ e.precio }}</span>
        </small>
      </li>
    </ul>
    <p v-else>No hay resultados para este valor.</p>

    <FooterView />
  </div>
</template>
