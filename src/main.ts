import "virtual:uno.css";
import "primeicons/primeicons.css";

import { createApp } from "vue";
import { createPinia } from "pinia";
import App from "./App.vue";
import router from "./router";
import PrimeVue from "primevue/config";
// @ts-ignore
import PrimeOne from "primevue/themes/primeone";
// @ts-ignore
import Aura from "primevue/themes/primeone/aura";
import Ripple from "primevue/ripple";
import ToastService from "primevue/toastservice";
import piniaPluginPersistedstate from "pinia-plugin-persistedstate";

import Button from "primevue/button";
import Stepper from "primevue/stepper";
import StepperPanel from "primevue/stepperpanel";
import IconField from "primevue/iconfield";
import InputIcon from "primevue/inputicon";
import Toast from "primevue/toast";

const pinia = createPinia();
pinia.use(piniaPluginPersistedstate);

const app = createApp(App);
app.use(PrimeVue, {
  ripple: true,
  theme: {
    base: PrimeOne,
    preset: Aura,
    options: {
      prefix: "p",
      darkModeSelector: "sstem",
      cssLayer: false,
    },
  },
});

app.directive("ripple", Ripple);
app.component("Toast", Toast);
app.component("Button", Button);
app.component("Stepper", Stepper);
app.component("StepperPanel", StepperPanel);
app.component("IconField", IconField);
app.component("InputIcon", InputIcon);

app.use(ToastService);

app.use(pinia);
app.use(router);

app.mount("#app");
