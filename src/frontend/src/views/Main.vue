<template>
  <ion-page>
    <ion-content>
      <ion-button router-link="/send" router-direction="forward">Go</ion-button>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
  import {
    IonPage,
    IonContent,
    IonButton
    } from '@ionic/vue';
</script>

<style scoped>
</style>