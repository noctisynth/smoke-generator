import { ref } from "vue";
import router from "@/router";

// 侧边栏内容
export default ref([
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
    label: "个人资料",
    icon: "pi pi-user",
    items: [
      {
        label: "设置",
        icon: "pi pi-cog",
        command: () => {
          router.push("/dashboard/profile");
        },
      },
    ],
  },
]);
