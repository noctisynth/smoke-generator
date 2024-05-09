<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

// 右上角菜单
const menu = ref();

// 侧边栏内容
const items = ref([
    {
        label: '烟雾生成',
        icon: 'pi pi-chart-bar',
        items: [
            {
                label: '生成',
                icon: 'pi pi-chart-line',
                command: () => {
                    router.push('/dashboard/generate');
                }
            },
            {
                label: '历史',
                icon: 'pi pi-list',
                command: () => {
                    router.push('/dashboard/generate/history');
                }
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
                command: () => {
                    router.push('/dashboard/joint');
                }
            },
            {
                label: '历史',
                icon: 'pi pi-history',
                command: () => {
                    router.push('/dashboard/joint/history');
                }
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
                command: () => {
                    router.push('/dashboard/profile');
                }
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

const toggle = (event: any) => {
    menu.value.toggle(event);
};

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
        <Toolbar class="!border-rd-none">
            <template #start>
                <div class="pl-3">
                    <span class="text-lg font-bold">控制台</span>
                </div>
            </template>
            <template #end>
                <div class="inline-flex items-center gap-2">
                    <IconField iconPosition="left">
                        <InputIcon>
                            <i class="pi pi-search"></i>
                        </InputIcon>
                        <InputText placeholder="搜索" />
                    </IconField>
                    <Button type="button" severity="secondary" icon="pi pi-ellipsis-v" @click="toggle"
                        aria-haspopup="true" aria-controls="overlay_menu"></Button>
                    <Menu ref="menu" id="overlay_menu" :model="items" :popup="true"></Menu>
                </div>
            </template>
        </Toolbar>
        <div class="flex flex-row w-full p-1rem gap-4 h-full bg-#f8fafc">
            <PanelMenu :model="items" class="w-18rem">
                <template #item="{ item }">
                    <a v-ripple class="flex items-center px-3 py-2 cursor-pointer">
                        <span :class="[item.icon, 'text-primary']"></span>
                        <span :class="['ml-2', { 'font-semibold': item.items }]">{{ item.label }}</span>
                    </a>
                </template>
            </PanelMenu>
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