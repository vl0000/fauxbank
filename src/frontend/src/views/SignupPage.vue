<template>
  <ion-page>
    <ion-content>
      <ion-grid>
        <ion-row>
          <ion-col size="12">
            <ion-input v-model="info.name" fill="outline" label="Name" label-placement="floating" placeholder="John Doe" type="text"></ion-input>
          </ion-col>
        </ion-row>

        <ion-row>
          <ion-col size="12">
            <ion-input v-model="info.email" fill="outline" label="Email" label-placement="floating" placeholder="johndoe@example.com" type="email"></ion-input>
          </ion-col>
        </ion-row>
    
        <ion-row>
          <ion-col size="12">
            <ion-input v-model="info.password" fill="outline" label="Password" label-placement="floating" placeholder="Your password" type="password"></ion-input>
          </ion-col>
        </ion-row>

        <ion-row>
          <ion-col size="12">
            <ion-input fill="outline" label="Confirm Password" label-placement="floating" placeholder="Confirm your password" type="password"></ion-input>
          </ion-col>
        </ion-row>

        <ion-row>
          <ion-col size="6">
            <ion-button fill="clear" router-link="/login" >Or login</ion-button>
          </ion-col>
          <ion-col size="5">
            <ion-button>Register</ion-button>
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
  IonContent
} from '@ionic/vue';
import { store } from '@/store';
import router from '@/router';

let info = {
  name: "",
  email: "",
  password: ""

}

async function handleSignup() {
  let form = new FormData()

  Object.entries(info)
    .forEach(([key, value]) => {
      form.append(key, value)
    })

  let response = await fetch(
    store.api + "/api/account/signup",
    {
      method: "POST",
      body: form
    }
    )
    .then(response => response.json())
    .then(
      response => {
        if (response.access_token) {
          store.jwt = "Bearer " + response.access_token
          router.push("/dashboard")
        } 
      }
    )
    .catch(err => { console.error(err) })
}

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
  top: 20%;
}
</style>