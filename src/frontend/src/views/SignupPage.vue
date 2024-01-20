<template>
    <ion-grid>
      <ion-row>
        <ion-col size="12">
          <ion-input fill="outline" label="Name" label-placement="floating" placeholder="John Doe" type="text"></ion-input>
        </ion-col>
      </ion-row>

      <ion-row>
        <ion-col size="12">
          <ion-input fill="outline" label="Email" label-placement="floating" placeholder="johndoe@example.com" type="email"></ion-input>
        </ion-col>
      </ion-row>
  
      <ion-row>
        <ion-col size="12">
          <ion-input fill="outline" label="Password" label-placement="floating" placeholder="Your password" type="password"></ion-input>
        </ion-col>
      </ion-row>

      <ion-row>
        <ion-col size="12">
          <ion-input fill="outline" label="Confirm Password" label-placement="floating" placeholder="Confirm your password" type="password"></ion-input>
        </ion-col>
      </ion-row>

      <ion-row>
        <ion-col size="6">
          <a>Or login</a>
        </ion-col>
        <ion-col size="5">
          <ion-button>Register</ion-button>
        </ion-col>
      </ion-row>
  
    </ion-grid>
</template>

<script setup lang="ts">
import {
  IonInput,
  IonGrid,
  IonRow,
  IonCol,
  IonButton
} from '@ionic/vue';
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