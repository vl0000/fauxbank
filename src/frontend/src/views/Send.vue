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
              <ion-input v-model="transaction.payee" fill="outline" label="Account Number" label-placement="floating" placeholder="xxxxxxxxxx" type="number"></ion-input>
          </ion-col>
        </ion-row>
        <ion-row>
          <ion-col size="12">
          <ion-input v-model="transaction.amount" fill="outline" label="Amount" label-placement="floating" placeholder="00.00" type="number"></ion-input>
          </ion-col>
        </ion-row>

        <ion-row>
          <ion-col size="12">
          <ion-button id="send-button" @click="handleSend">Send</ion-button>
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
import { makeTransaction } from '@/maketransaction';
import router from '@/router';

let transaction = {
  payee: 0,
  amount: 0.0
}

async function handleSend() {
  let response = await makeTransaction(transaction)

  if (response.status == 200) {
    //make a success view
    router.back()
  }
}

</script>

<style scoped>
#send-button {
    width: 100%;
}
ion-router-outlet {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}
ion-grid {
  position: relative;
  top: 20%;
}
</style>