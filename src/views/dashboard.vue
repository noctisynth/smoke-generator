<script setup lang="ts">
import { onMounted, ref } from 'vue';
import items from '@/scripts/items';

// 右上角菜单
const menu = ref();

// 公告内容
const announcement = ref<string>('');
const showAnnouncement = ref<boolean>(true);
async function fetchAnnouncement() {
    announcement.value = '公告内容';
}

onMounted(async () => {
    // 页面渲染完成后获取公告内容
    await fetchAnnouncement();
})
</script>

<template>
    <div :class="['fixed inset-x-0 bottom-0 p-4', (showAnnouncement ? '' : 'hidden')]">
        <div class="relative flex items-center justify-between rounded-lg bg-indigo-600 px-4 py-1 text-white shadow-lg">
            <p class="text-sm font-medium">
                {{ announcement }}
            </p>

            <Button @click="showAnnouncement = false" icon="pi pi-times text-coolGray hover:!text-white"
                class="hover:!bg-indigo-600 hover:!text-white" plain text>
            </Button>
        </div>
    </div>
    <div class="flex flex-col w-full h-full">
        <TopBar></TopBar>
        <div class="flex flex-row w-full p-1rem gap-4 h-full bg-#f8fafc">
            <SidePanel></SidePanel>
            <Card class="w-full h-full">
                <template #title>
                    <h1 class="text-2xl font-bold m-0">主页</h1>
                </template>
                <template #content>
                    <div class="flex flex-col gap-4">
                        <span class="text-lg font-bold">xxx 的账户</span>
                        <h2 class="text-sm font-bold m-0 text-coolGray-600">此处列出了一些功能快捷入口</h2>
                        <div class="grid grid-cols-2 gap-4">
                            <ColoredCard title="烟雾拼接" href="/dashboard/generate/" tag="拼接" class="w-full h-full">
                            </ColoredCard>
                            <ColoredCard title="烟雾生成" href="/dashboard/joint/" tag="生成" class="w-full h-full">
                            </ColoredCard>
                            <ColoredCard title="烟雾生成" href="/dashboard/joint/" tag="生成" class="w-full h-full">
                            </ColoredCard>
                        </div>
                    </div>
                </template>
            </Card>
        </div>
    </div>
</template>

<style scoped></style>