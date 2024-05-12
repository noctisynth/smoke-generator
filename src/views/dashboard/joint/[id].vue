<script setup lang="ts">
import { onMounted, ref } from 'vue';
import axios from '@/axios';
import { useTokenStore } from '@/stores/token';
import { useRouter } from 'vue-router';
import { useUserStore } from '@/stores/user';
import { useToast } from 'primevue/usetoast';

const toast = useToast();
const router = useRouter();
const id = router.currentRoute.value.params.id;
const tokenStore = useTokenStore();
const userStore = useUserStore();

const smoke = ref<{
    id: number;
    name: string;
    user: string;
    type: string;
    date: string;
    url: string;
} | null>(null);

function download() {
    var a = document.createElement("a");
    a.href = "";
    a.download = "."
    a.style.display = "none";
    document.body.appendChild(a);
    a.click();
    a.remove();
}

onMounted(async () => {
    axios.post('/smoke/get', { token: tokenStore.token, id: id }).then(res => {
        if (res.data.status === 200) {
            smoke.value = res.data.record;
        } else if (res.data.status === 403) {
            router.push('/dashboard/error/403');
        } else {
            router.push('/dashboard/error/404');
        }
    }).catch(err => {
        console.log(err);
        toast.add({ severity: 'error', summary: '获取数据失败', detail: err.message });
    });
});
</script>

<template>
    <div class="flex flex-col w-full h-full">
        <Announcement></Announcement>
        <Toast></Toast>
        <TopBar></TopBar>

        <div class="flex flex-col w-full sm:h-30rem md:h-35rem justify-center items-center bg-#f9f9f9 dark:bg-#222">
            <Image :src="userStore.avatar" alt="avatar" class="w-20rem h-20rem max-h-full max-w-full rounded" preview>
            </Image>
        </div>
        <Card>
            <template #header>
                <div class="flex justify-between items-center p-2rem mx-6rem">
                    <div class="flex flex-row items-center gap-2">
                        <Avatar :src="userStore.avatar" size="xlarge" class="mr-2"></Avatar>
                        <div class="flex flex-col">
                            <h2 class="text-xl font-bold mb-0">名称</h2>
                            <p class="text-sm text-gray-500">xxx</p>
                        </div>
                    </div>
                    <Button icon="pi pi-download" label="下载" @click="download"></Button>
                </div>
            </template>
        </Card>
    </div>
</template>

<style scoped></style>
