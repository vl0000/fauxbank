import { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'ionic.fauxbank',
  appName: 'fauxbank',
  webDir: 'dist',
  server: {
    androidScheme: 'https'
  }
};

export default config;
