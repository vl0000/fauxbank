<template>
<ion-page>
  <ion-content>

    <ion-grid>

      <ion-row>
        <ion-col size="12">
          <ion-input v-model="email" fill="outline" label="Email" label-placement="floating" placeholder="johndoe@example.com" type="email"></ion-input>
        </ion-col>
      </ion-row>

      <ion-row>
        <ion-col size="12">
          <ion-input v-model="password" fill="outline" label="Password" label-placement="floating" placeholder="Your password" type="password"></ion-input>
        </ion-col>
      </ion-row>

      <ion-row>
        <ion-col size="6">
          <!-- This link is temporary !!!!!!!!!!!-->
          <ion-button router-link="/dashboard" fill="clear">Create an account</ion-button>
        </ion-col>
        <ion-col size="5">
          <ion-button @click="login">Login</ion-button>
        </ion-col>
      </ion-row>
      

    </ion-grid>

  </ion-content>
</ion-page>


</template>

<script setup lang="ts">
import { ref } from 'vue';
import {
  IonInput,
  IonGrid,
  IonRow,
  IonCol,
  IonButton,
  IonPage,
  IonContent,
} from '@ionic/vue';
import router from '@/router';

async function login() {
  const form = new FormData();
  //This is needed due to Oauth2
  form.append("username", email)
  form.append("password", password)

  let response = await fetch(
    "http://127.0.0.1:8000/api/accounts",
    {
      method: "POST",
      body: form
    }
    )
    .then(response => response.json())
    .then(
      response => {
        if (response.status == 200) {
          // STORE THE JWT KEY SOMEWHERE
          router.push("/dashboard")
        } 
      }
    )
    .catch(err => { console.error(err) })
}


let email: string;
let password: string;


</script>

<style scoped>

ion-col {
  display: flex;
  direction: column;
  align-items: center;
  justify-content: center;
}
ion-row {
  display: flex;
  align-items: center;
  justify-content: center;
}
ion-grid {
  height: 50%;
  width: 100%;
  position: relative;
  top: 30%;
}
</style>