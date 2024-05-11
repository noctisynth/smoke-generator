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

const active = ref<number>(0);

if (!tokenStore.isLoggedIn()) {
    router.push('/login');
}

const masks = ref<string[]>([]);
const styles = ref<string[]>([]);
const selectedMask = ref(0);
const selectedStyle = ref(0);
async function load(): Promise<boolean> {
    // 加载类型及样式数据
    let status = true;
    await axios.get('/smoke/masks').then((res) => { masks.value = res.data.masks }).catch((err) => {
        toast.add({ severity: 'error', summary: '数据获取失败！', detail: err.message });
        status = false
    })
    await axios.get('/smoke/styles').then((res) => { styles.value = res.data.styles }).catch((err) => {
        toast.add({ severity: 'error', summary: '数据获取失败！', detail: err.message });
        status = false
    })
    return status
}
// 更新选择的烟雾类型
function maskChanged(value: any) {
    selectedMask.value = value;
}
// 更新选择的烟雾样式
function styleChanged(value: any) {
    selectedStyle.value = value;
}

// 烟雾生成
const generatedSmoke = ref<string>('');
const inProgress = ref<boolean>(false);
async function generateSmoke() {
    active.value = 2;
    inProgress.value = true;

    // 发送生成烟雾请求
    await new Promise((resolve) => setTimeout(resolve, 3000));
    console.log({
        token: tokenStore.token,
        mask: masks.value[selectedMask.value].split('/').pop(),
        style: styles.value[selectedStyle.value].split('/').pop()
    })
    axios.post('/smoke/generate', {
        token: tokenStore.token,
        mask_pic: masks.value[selectedMask.value].split('/').pop(),
        style_pic: styles.value[selectedStyle.value].split('/').pop()
    }).then((res) => {
        if (res.data.status === 200) {
            const obj = res.data.obj;
            generatedSmoke.value = obj.url;
            toast.add({ severity: 'success', summary: '烟雾生成成功！', detail: res.data.message, life: 3000 });
        }
        else
            toast.add({ severity: 'error', summary: '烟雾生成失败！', detail: res.data.message, life: 3000 });
        inProgress.value = false;
    }).catch((err) => {
        toast.add({ severity: 'error', summary: '烟雾生成失败！', detail: err.message, life: 3000 });
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
                                        <i class="pi pi-tag"></i>
                                    </span>
                                </button>
                            </template>
                            <template #content>
                                <div class="flex flex-col gap-2 mx-auto">
                                    <h2 class="text-lg font-bold pl-10">选择烟雾类型</h2>
                                    <div class="flex justify-center items-center">
                                        <Carousel class="w-30rem" :page="selectedMask" @update:page="maskChanged"
                                            :value="masks" :numVisible="1" :numScroll="1">
                                            <template #item="slotProps">
                                                <div class="b-1.5 b-solid b-coolGray b-rd m-2 p-3">
                                                    <div class="flex justify-center items-center">
                                                        <div class="relative mx-auto">
                                                            <Image class="w-20rem h-20rem" imageClass="rounded"
                                                                :src="slotProps.data" preview>
                                                            </Image>
                                                            <Tag value="MASK" severity="INFO"
                                                                class="absolute top-3 left-3" />
                                                        </div>

                                                    </div>
                                                </div>
                                            </template>
                                        </Carousel>
                                    </div>
                                    <div class="flex pt-4 justify-end">
                                        <Button label="选择样式" icon="pi pi-arrow-right" iconPos="right"
                                            @click="active = 1"></Button>
                                    </div>
                                </div>
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
                                <div class="flex flex-col gap-2 mx-auto">
                                    <h2 class="text-lg font-bold pl-10">选择烟雾样式</h2>
                                    <div class="flex justify-center items-center">
                                        <Carousel class="w-30rem" @update:page="styleChanged" :value="styles"
                                            :numVisible="1" :numScroll="1">
                                            <template #item="slotProps">
                                                <div class="b-1.5 b-solid b-coolGray b-rd m-2 p-3">
                                                    <div class="flex justify-center items-center">
                                                        <div class="relative mx-auto">
                                                            <Image class="w-20rem h-20rem" imageClass="rounded"
                                                                :src="slotProps.data" preview>
                                                            </Image>
                                                            <Tag value="STYLE" severity="danger"
                                                                class="absolute top-3 left-3" />
                                                        </div>

                                                    </div>
                                                </div>
                                            </template>
                                        </Carousel>
                                    </div>
                                    <div class="flex pt-4 justify-between">
                                        <Button label="选择类型" icon="pi pi-arrow-left" severity="secondary"
                                            @click="active = 0"></Button>
                                        <Button label="生成烟雾" icon="pi pi-arrow-right" iconPos="right"
                                            @click="generateSmoke"></Button>
                                    </div>
                                </div>
                            </template>
                        </StepperPanel>
                        <StepperPanel>
                            <template #header="{ index, clickCallback }">
                                <button class="bg-transparent border-none inline-flex flex-col gap-2"
                                    @click="clickCallback">
                                    <span
                                        :class="['b-rd b-solid w-3rem h-3rem inline-flex items-center justify-center', { 'b-blueGray': index > active, 'bg-emerald !b-none': index <= active }]">
                                        <i :class="(inProgress ? 'pi pi-spin pi-spinner' : 'pi pi-check')"></i>
                                    </span>
                                </button>
                            </template>
                            <template #content>
                                <div class="flex flex-col gap-2 mx-auto">
                                    <h2 class="text-lg font-bold pl-10">生成烟雾</h2>
                                    <div v-if="!inProgress" class="flex justify-center items-center">
                                        <Image class="w-30rem h-30rem rounded" imageClass="rounded"
                                            :src="generatedSmoke" preview></Image>
                                    </div>
                                    <div v-else>
                                        <div class="flex justify-center items-center">
                                            <ProgressSpinner></ProgressSpinner>
                                        </div>
                                    </div>
                                    <div class="flex pt-4 justify-start">
                                        <Button label="选择样式" icon="pi pi-arrow-left" severity="secondary"
                                            @click="active = 1"></Button>
                                    </div>
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