import { ref } from "vue";
import router from "@/router";
import { useTokenStore } from "@/stores/token";
import axios from "@/axios";

// 侧边栏内容
export default ref([
  {
    label: "首页",
    icon: "pi pi-home",
    command: () => {
      router.push("/dashboard");
    },
  },
  {
    label: "探索更多",
    icon: "pi pi-compass",
    command: () => {
        router.push("/dashboard/explore");
    },
    items: [
      {
        label: "烟雾",
        icon: "pi pi-database",
        command: () => {
          router.push("/dashboard/explore/smoke");
        },
      },
      {
        label: "合成",
        icon: "pi pi-folder-open",
        command: () => {
          router.push("/dashboard/explore/synthesis");
        },
      },
    ],
  },
  {
    label: "烟雾生成",
    icon: "pi pi-chart-bar",
    items: [
      {
        label: "生成",
        icon: "pi pi-chart-line",
        command: () => {
          router.push("/dashboard/generate");
        },
      },
      {
        label: "历史",
        icon: "pi pi-list",
        command: () => {
          router.push("/dashboard/generate/history");
        },
      },
    ],
  },
  {
    label: "烟雾拼接",
    icon: "pi pi-clone",
    items: [
      {
        label: "拼接",
        icon: "pi pi-images",
        command: () => {
          router.push("/dashboard/joint");
        },
      },
      {
        label: "历史",
        icon: "pi pi-history",
        command: () => {
          router.push("/dashboard/joint/history");
        },
      },
    ],
  },
  {
    label: "账户管理",
    icon: "pi pi-user",
    items: [
      {
        label: "个人资料",
        icon: "pi pi-cog",
        command: () => {
          router.push("/dashboard/profile");
        },
      },
      {
        label: "修改密码",
        icon: "pi pi-lock",
        command: () => {
          router.push("/dashboard/profile/password");
        },
      },
      {
        label: "登出",
        icon: "pi pi-sign-out",
        command: () => {
          const tokenStore = useTokenStore();
          axios
            .post("/account/logout", { token: tokenStore.token })
            .then(() => {});
          tokenStore.removeToken();
          router.push("/login");
        },
      },
    ],
  },
  {
    label: "公告",
    icon: "pi pi-bell",
    command: () => {
      router.push("/dashboard/billboard");
    },
  },
]);
