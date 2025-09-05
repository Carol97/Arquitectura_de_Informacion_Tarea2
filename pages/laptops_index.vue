<template>
  <div class="container">
    <HeaderView />
    <h3 style="margin-top: 15px">Listado de Laptops</h3>
    <p>Esta sección muestra todas las laptops disponibles.</p>
    <ul>
      <ContentList path="/laptops" v-slot="{ list }">
        <li v-for="item in list" :key="item._path">
          <NuxtLink :to="item._path">{{ item.title }}</NuxtLink>
        </li>
      </ContentList>
    </ul>
    <FooterView />
  </div>
</template>
