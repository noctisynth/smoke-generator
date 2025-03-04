<script setup lang="ts">
import axios from '@/axios';
import { useTokenStore } from '@/stores/token';
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useToast } from 'primevue/usetoast';
import { useUserStore } from '@/stores/user';

const toast = useToast();
const router = useRouter();
const tokenStore = useTokenStore();
const userStore = useUserStore();

if (!tokenStore.isLoggedIn()) {
    router.push('/login');
}

onMounted(() => {
    axios.post('/account/profile', { token: tokenStore.token }).then((res) => {
        if (res.data.status === 403) {
            toast.add({ severity: 'error', summary: '错误', detail: '登录已过期，请重新登录！', life: 3000 });
            router.push('/login');
            tokenStore.removeToken();
        }
        userStore.setUserInfo(res.data);
    }).catch(() => {
        toast.add({ severity: 'error', summary: '错误', detail: '服务器错误！', life: 3000 });
    })
})
</script>

<template>
    <div class="flex flex-col w-full h-full">
        <Announcement></Announcement>
        <Toast></Toast>
        <TopBar></TopBar>
        <div class="grid md:grid-cols-4 lg:grid-cols-5 w-full p-1rem gap-4 h-full bg-#f8fafc dark:bg-dark-900">
            <SidePanel class="grid col-span-1"></SidePanel>
            <Card class="grid md:col-span-3 lg:md:col-span-4">
                <template #title>
                    <h1 class="text-2xl font-bold m-0">主页</h1>
                </template>
                <template #content>
                    <div class="flex flex-col gap-4">
                        <span class="text-lg font-bold">{{ userStore.username }} 的账户</span>
                        <h2 class="text-sm font-bold m-0 text-coolGray-600">此处列出了一些功能快捷入口</h2>
                        <div class="grid grid-cols-2 gap-4">
                            <ColoredCard title="烟雾生成" href="/dashboard/generate/" tag="生成" class="w-full h-full">
                            </ColoredCard>
                            <ColoredCard title="烟雾拼接" href="/dashboard/joint/" tag="拼接" class="w-full h-full">
                            </ColoredCard>
                            <ColoredCard title="烟雾生成历史" href="/dashboard/generate/history/" tag="生成"
                                class="w-full h-full">
                            </ColoredCard>
                            <ColoredCard title="烟雾拼接历史" href="/dashboard/joint/history/" tag="拼接" class="w-full h-full">
                            </ColoredCard>
                        </div>
                    </div>
                </template>
            </Card>
        </div>
    </div>
</template>

<style scoped></style>