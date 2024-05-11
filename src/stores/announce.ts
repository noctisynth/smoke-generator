import { ref } from "vue";
import { defineStore } from "pinia";

export const useAnnounceStore = defineStore(
  "announce",
  () => {
    const closed = ref<boolean>(false);

    function close() {
      closed.value = true;
    }

    return { closed, close };
  },
  {
    persist: true,
  }
);
