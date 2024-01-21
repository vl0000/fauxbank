<template>
<ion-page>
  <ion-content>

    <ion-grid>

      <ion-row>
        <!-- Balance section-->
        <ion-col>

          <ion-card>

          <ion-card-header>
            <ion-card-title>
              Balance
            </ion-card-title>
          </ion-card-header>
          
            <ion-card-content>
              R$ 250.00
            </ion-card-content>

          </ion-card>

        </ion-col>
      </ion-row>

      <ion-row>
        <!-- Card section-->
        <ion-col>
          <ion-card id="credit-card">
            <ion-card-content id="credit-card content">
              <div class="card-info">
                <span>**** **** **** 1234</span>
                <span>FLAG</span>
              </div>
              <div class="card-info">
                <span>Name | 000000</span>
                <span>12/28</span>
              </div>
            </ion-card-content>
          </ion-card>
        </ion-col>
      </ion-row>

      <ion-row>
        <!-- Buttons -->
        <ion-col class="button-container">
          <ion-button router-link="/send">
            Send 
            <ion-icon :icon="arrowUpOutline"></ion-icon>
          </ion-button>
        </ion-col>
        <ion-col class="button-container">
          <ion-button router-link="/receive" router-direction="forward">
            Receive 
            <ion-icon :icon="arrowDownOutline"></ion-icon>
          </ion-button>
        </ion-col>
      </ion-row>


      <ion-row>
        <!-- Transactions -->
        <ion-col>
          <ion-card>

            <ion-card-header>
              <ion-card-title>Latest Movements</ion-card-title>
            </ion-card-header>

            <ion-card-content>
              <ion-list>
                <ion-item>
                  <ion-label>
                    <h2>Movement</h2>
                    <p>Today</p>
                  </ion-label>
                  <small class="negative">R$ -12.57</small>
                </ion-item>
              </ion-list>
            </ion-card-content>

          </ion-card>

        </ion-col>
      </ion-row>

          <ion-fab>
            <ion-fab-button>
              <ion-icon :icon="qrCodeOutline"></ion-icon>
            </ion-fab-button>
          </ion-fab>
    </ion-grid>
  </ion-content>
</ion-page>
</template>

<script setup lang="ts">
import {
  IonGrid,
  IonRow,
  IonCol,
  IonCard,
  IonCardHeader,
  IonCardTitle,
  IonCardContent,
  IonList,
  IonItem,
  IonLabel,
  IonButton,
  IonIcon,
  IonFab,
  IonFabButton,
  IonPage,
  IonContent,

  } from '@ionic/vue';
  
  import {
    arrowUpOutline,
    arrowDownOutline,
    qrCodeOutline
  } from 'ionicons/icons'
</script>

<style scoped>
#credit-card {
  max-height: 160px;
}
.card-info {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  
  margin-top: 50px;
}
.negative {
  color: red;
}

.button-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}
ion-fab {
  right: 15px;
  bottom: 15px
}
</style>