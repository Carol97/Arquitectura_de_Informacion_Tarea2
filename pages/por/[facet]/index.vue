<script setup lang="ts">
const route = useRoute()
const facet = route.params.facet as string

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

const { data: valores } = await useAsyncData(`vals-${facet}`, async () => {
  const rows: any[] = await queryContent('/laptops').only([field]).find()
  const set = new Set(
    rows
      .map(r => String(r[field] ?? '').trim())
      .filter(Boolean)
  )
  return Array.from(set).sort((a, b) => a.localeCompare(b, 'es', { numeric: true }))
})
</script>

<template>
  <div class="container">
    <HeaderView />
    <h3 style="margin-top: 15px">Listar por {{ facet }}</h3>
    <p>Seleccione un valor para ver las laptops que coinciden.</p>

    <ul>
      <li v-for="v in valores" :key="v">
        <NuxtLink :to="`/por/${facet}/${encodeURIComponent(v)}`">{{ v }}</NuxtLink>
      </li>
    </ul>

    <FooterView />
  </div>
</template>