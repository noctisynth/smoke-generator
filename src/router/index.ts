import {
  createRouter,
  createWebHashHistory,
  type RouteRecordRaw,
} from "vue-router";

// 动态导入views目录下的所有vue文件
const views = import.meta.glob([
  "../views/**/*.vue",
  "../views/**/index.vue",
  "../views/**/\\[*\\].vue",
]);

// 路由配置
const routes: RouteRecordRaw[] = Object.entries(views).map(
  ([filePath, component]) => {
    // 处理路由路径
    let path = filePath.replace(/^\.\.\/views\//, "");
    path = path.replace(/^(.*)\/?index\.vue$/, "$1");
    path = path.replace(/\[(\w+)\]\.vue$/, ":$1");
    path = path.replace(/\.vue$/, "");
    path = "/" + path;

    return {
      path,
      name: filePath.replace(/^\.\.\/views\//, ""),
      component,
    } satisfies RouteRecordRaw;
  }
);

// 打印路由配置
console.table(routes);

// 创建路由实例
const router = createRouter({
  history: createWebHashHistory(import.meta.env.BASE_URL),
  routes: [...routes],
});

// 导出路由实例
export default router;
