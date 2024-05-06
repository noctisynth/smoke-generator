<script setup lang="ts">
import { onMounted, ref } from 'vue';

// 侧边栏内容
const items = ref([
    {
        label: '烟雾生成',
        icon: 'pi pi-chart-bar',
        items: [
            {
                label: '生成',
                icon: 'pi pi-chart-line',
            },
            {
                label: '历史',
                icon: 'pi pi-list',
            }
        ]
    },
    {
        label: '烟雾拼接',
        icon: 'pi pi-clone',
        items: [
            {
                label: '拼接',
                icon: 'pi pi-images',
            },
            {
                label: '历史',
                icon: 'pi pi-history',
            },
        ]
    },
    {
        label: '个人资料',
        icon: 'pi pi-user',
        items: [
            {
                label: '设置',
                icon: 'pi pi-cog',
            }
        ]
    }
]);

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
    <div class="flex flex-row w-full p-1rem gap-2rem h-full bg-#f8fafc">
        <PanelMenu :model="items" class="w-18rem">
            <template #item="{ item }">
                <a v-ripple class="flex items-center px-3 py-2 cursor-pointer">
                    <span :class="[item.icon, 'text-primary']" />
                    <span :class="['ml-2', { 'font-semibold': item.items }]">{{ item.label }}</span>
                </a>
            </template>
        </PanelMenu>
        <div class="w-full h-full"></div>
    </div>
</template>

<style scoped></style>