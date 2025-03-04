<script setup lang="ts">
import axios from '@/axios';
import { useTokenStore } from '@/stores/token';
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
import { useToast } from 'primevue/usetoast';
import { useUserStore } from '@/stores/user';

const toast = useToast();
const router = useRouter();
const tokenStore = useTokenStore();
const loading = ref(true);

if (!tokenStore.isLoggedIn()) {
    router.push('/login');
}

const records = ref<{
    id: number,
    name: string,
    user: string,
    date: string,
    type: string,
    url: string,
    visible: boolean,
}[]>([]);
async function load(): Promise<boolean> {
    let status = true;
    await axios.post('/smoke/get_public', { type: '图片' }).then((res) => { records.value = res.data.records }).catch((err) => {
        toast.add({ severity: 'error', summary: '数据获取失败！', detail: err.message });
        status = false
    })
    return status
}

async function add(id: string | number) {
    await axios.post('/smoke/explore_add', { token: tokenStore.token, id: id, type: '图片' }).then(_ => {
        toast.add({ severity: 'success', summary: '数据添加成功！', detail: '数据已添加到您的历史记录中。', life: 3000 });
    }).catch((err) => {
        toast.add({ severity: 'error', summary: '数据添加失败！', detail: err.message, life: 3000 });
    })
}

onMounted(async () => {
    load().then((status) => {
        if (status)
            loading.value = false;
    })
});
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
                    <h1 class="text-2xl font-bold m-0">合成图</h1>
                </template>
                <template #content>
                    <div v-if="records.length > 0" class="grid lg:grid-cols-3 sm:grid-cols-1 md:grid-cols-2 gap-4">
                        <div v-for="record in records" :key="record.id" class="py-3 flex flex-col items-center">
                            <a class="max-w-full rounded-lg shadow-sm shadow-indigo-100 grid">
                                <Image :src="record.url" imageClass="max-w-full" class="h-56 w-full max-w-full object-cover" preview></Image>
                                <div class="p-2 mt-2">
                                    <div @click="router.push('/dashboard/explore/synthesis/' + record.id)"
                                        class="cursor-pointer flex p-2 flex-col items-start justify-center">
                                        <span class="text-sm text-gray-500">{{ record.date }}</span>
                                        <span class="font-medium">{{ record.name }}</span>
                                    </div>

                                    <div class="flex items-center gap-4 text-xs px-2 justify-between">
                                        <div class="sm:inline-flex sm:shrink-0 sm:items-center sm:gap-1 gap-2">
                                            <Avatar :img="record.url" class="w-7 h-7"></Avatar>
                                            <p class="text-wrap text-gray-600">Generated by {{ record.user }}</p>
                                        </div>

                                        <Button @click="add(record.id)" icon="pi pi-star" outlined></Button>
                                    </div>
                                </div>
                            </a>
                        </div>
                    </div>
                    <div v-else class="flex justify-center items-center h-full">
                        <p class="text-center text-gray-500">暂无数据</p>
                    </div>
                </template>
            </Card>
        </div>
    </div>
</template>

<style scoped></style>