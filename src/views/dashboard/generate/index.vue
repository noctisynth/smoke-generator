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
const userStore = useUserStore();
const loading = ref(true);

const active = ref<number>(0);

if (!tokenStore.isLoggedIn()) {
    router.push('/login');
}

const masks = ref();
const styles = ref();
async function load(): Promise<boolean> {
    let status = true;
    masks.value = await axios.get('/smoke/masks').then((res) => { return res.data }).catch((err) => {
        toast.add({ severity: 'error', summary: '数据获取失败！', detail: err.message });
        status = false
    })
    styles.value = await axios.get('/smoke/styles').then((res) => { return res.data }).catch((err) => {
        toast.add({ severity: 'error', summary: '数据获取失败！', detail: err.message });
        status = false
    })
    return status
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
                    <h1 class="text-2xl font-bold m-0">烟雾生成</h1>
                </template>
                <template #content>
                    <Stepper class="w-full h-full" v-model:activeStep="active" linear v-if="!loading">
                        <StepperPanel>
                            <template #header="{ index, clickCallback }">
                                <button class="bg-transparent border-none inline-flex flex-col gap-2"
                                    @click="clickCallback">
                                    <span
                                        :class="['b-rd b-solid w-3rem h-3rem inline-flex items-center justify-center', { 'b-blueGray': index > active, 'bg-emerald !b-none': index <= active }]">
                                        <i class="pi pi-star"></i>
                                    </span>
                                </button>
                            </template>
                            <template #content>
                                <Carousel :value="masks" :numVisible="1" :numScroll="1">
                                    <template #item="slotProps">
                                        <div class="border-1 b-solid b-rd m-2 p-3">
                                            <Image :src="slotProps.data" preview></Image>
                                        </div>
                                    </template>
                                </Carousel>
                            </template>
                        </StepperPanel>
                        <StepperPanel>
                            <template #header="{ index, clickCallback }">
                                <button class="bg-transparent border-none inline-flex flex-col gap-2"
                                    @click="clickCallback">
                                    <span
                                        :class="['b-rd b-solid w-3rem h-3rem inline-flex items-center justify-center', { 'b-blueGray': index > active, 'bg-emerald !b-none': index <= active }]">
                                        <i class="pi pi-star"></i>
                                    </span>
                                </button>
                            </template>
                            <template #content>
                                <div class="flex flex-col gap-2 mx-auto" style="min-height: 16rem; max-width: 24rem">
                                    <div class="text-center mt-3 mb-3 text-xl font-semibold">账户创建成功！
                                    </div>
                                    <div class="text-center">
                                        <img alt="logo"
                                            src="https://primefaces.org/cdn/primevue/images/stepper/content.svg" />
                                    </div>
                                </div>
                                <div class="flex pt-4 justify-end">
                                    <Button label="登录" icon="pi pi-sign-in" iconPos="right"
                                        @click="$router.push('/login')"></Button>
                                </div>
                            </template>
                        </StepperPanel>
                    </Stepper>
                    <div class="flex justify-center items-center h-full" v-else>
                        <ProgressSpinner />
                    </div>
                </template>
            </Card>
        </div>
    </div>
</template>

<style scoped></style>