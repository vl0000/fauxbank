<template>
  <ion-page class="transparent">
    <ion-content class="transparent">
      <div id="camera"></div>
      <ion-button fill="outline" size="large" id="scan-button" @click="handleScan">Scan</ion-button>
    </ion-content>
  </ion-page>

</template>

<script setup lang="ts">
  import {
  IonButton,
  IonPage,
  IonContent,
  } from '@ionic/vue';
  import { onMounted } from 'vue';
  import { CameraPreview } from '@capacitor-community/camera-preview';
  import { useBackButton } from '@ionic/vue';
  import QrScanner from "qr-scanner";
  import { makeTransaction } from "@/maketransaction";
  import router from '@/router';
  
  async function scan() {
    // Get take the picture
    let data = await CameraPreview.capture({quality: 100})
    .then(result => "data:image/jpeg;base64," + result.value)
    .catch(err => console.log(err))
    
    // Convert to BLOB
    let image = await fetch(data)
    .then(data => data.blob())
    .then(data => createImageBitmap(data))
    .catch(err => console.log(err))

    // Scans the image for a QR code
    let result = await QrScanner.scanImage(image)
    .catch(err => console.log(error))

    //The function to create a transaction goes HERE!!!
    return JSON.parse(result)

  }

  async function handleScan() {
    let data = await scan()
    let response = await makeTransaction(data)
    
    if (response == "success") {
      CameraPreview.stop()
      // Add a success view later
      router.replace({ path: "/dashboard" })
    }
  }

  onMounted(
    () => {
      CameraPreview.start({parent: "camera", toBack: true})

    }
  )
  
  // Stop the camera whenever the back button is pressed.
  // If this is not done, it causes all sorts of badness. DO NOT TOUCH
  useBackButton(0, () => {
    CameraPreview.stop()
    router.replace({ path: "/dashboard" })
  })

</script>

<style scoped>
  #scan-button {
    position: absolute;
    transform: translate(-50%,0%);
    bottom: 40px;
    left: 50%;
    z-index: 1000;

  }
  .transparent {
    background-color: transparent;
  }

</style>