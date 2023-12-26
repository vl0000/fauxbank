import { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.fauxbank',
  appName: 'fauxbank',
  webDir: 'build',
  server: {
    androidScheme: 'https'
  }
};

export default config;
