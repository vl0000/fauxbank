<template>
<ion-page>
  <ion-content>

    <ion-header>
      <ion-toolbar>
        <ion-button 
        slot="start"
        router-link="/dashboard"
        router-direction="back"
        fill="clear"
        shape="round">
          <ion-icon :icon="arrowBack"></ion-icon>
        </ion-button>
      </ion-toolbar>
    </ion-header>

    <ion-grid>
      <ion-row>
        <ion-col size="12">
        </ion-col>
      </ion-row>

      <ion-row>
          <ion-col size="12">
          <ion-input fill="outline" label="Ammount" label-placement="floating" placeholder="00.00" type="number"></ion-input>
          </ion-col>
      </ion-row>

      <ion-row>
          <ion-col size="12">
          <ion-button id="generate-qr">Generate a QR code</ion-button>
          </ion-col>
      </ion-row>
    </ion-grid>
  </ion-content>
</ion-page>


</template>

<script setup lang="ts">
  import {
  IonInput,
  IonGrid,
  IonRow,
  IonCol,
  IonButton,
  IonPage,
  IonContent,
  IonHeader,
  IonToolbar,
  IonIcon
  } from '@ionic/vue';
  import { arrowBack } from 'ionicons/icons';
</script>

<style scoped>
#generate-qr {
  width: 100%;
}
</style>