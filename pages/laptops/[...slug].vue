<template>
  <div class="container">
    <HeaderView />
    <ContentDoc v-slot="{ doc }">
      <h4 style="margin-top: 15px">{{ doc.title }}</h4>
      <ContentRenderer :value="doc" />
    </ContentDoc>
    <FooterView />
  </div>
</template>
