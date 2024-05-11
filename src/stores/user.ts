import { ref } from "vue";
import { defineStore } from "pinia";

export const useUserStore = defineStore(
  "user",
  () => {
    const phone = ref<string>("");
    const email = ref<string>("");
    const status = ref<string>("");
    const avatar = ref<string>("");
    const username = ref<string>("");

    function setUserInfo(data: any) {
      phone.value = data.phone;
      email.value = data.email;
      status.value = data.status;
      avatar.value = data.avatar;
      username.value = data.username;
    }

    return { phone, email, status, avatar, username, setUserInfo };
  },
  {
    persist: true,
  }
);
