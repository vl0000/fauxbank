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
      <ion-row class="QR">
        <ion-col class="QR" size="12">
          <canvas id="canvas"></canvas>
        </ion-col>
      </ion-row>

      <ion-row>
          <ion-col size="12">
          <ion-input v-model="amount" fill="outline" label="Ammount" label-placement="floating" placeholder="00.00" type="number"></ion-input>
          </ion-col>
      </ion-row>

      <ion-row>
          <ion-col size="12">
          <ion-button @click="generate_code" id="generate-qr">Generate a QR code</ion-button>
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
  import { store } from '@/store';
  import * as QRCode from 'qrcode';


  let amount: Number;
  
  function generate_code() {
    let data = `{ "payee": ${store.account.number}, "amount": ${amount} }`

    let canvas = document.getElementById("canvas")

    let options = {
      scale: 10
    }
    QRCode.toCanvas(canvas, data, options, err => console.error(err))
  }

</script>

<style scoped>
#generate-qr {
  width: 100%;
}
.QR {
  height: 500px !important;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>