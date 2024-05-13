<script setup lang="ts">
import axios from '@/axios';
import { useTokenStore } from '@/stores/token';
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
import { useToast } from 'primevue/usetoast';
// @ts-ignore
import VueCropper from 'vue-cropperjs';
import "cropperjs/dist/cropper.css";

const toast = useToast();
const router = useRouter();
const tokenStore = useTokenStore();
const loading = ref(true);

const active = ref<number>(0);

if (!tokenStore.isLoggedIn()) {
    router.push('/login');
}

const smokes = ref<any[]>([]);
const selectedMask = ref(0);
async function load(): Promise<boolean> {
    // 加载类型及样式数据
    let status = true;
    await axios.post('/smoke/generate_history', { token: tokenStore.token }).then((res) => { smokes.value = res.data.records }).catch((err) => {
        toast.add({ severity: 'error', summary: '数据获取失败！', detail: err.message });
        status = false
    })
    return status
}
// 更新选择的烟雾类型
function maskChanged(value: any) {
    selectedMask.value = value;
}

// 图片裁剪实例
const cropper = ref<VueCropper | null>(null);
const uploadedImage = ref<File | null>(null);
const uploadedSrc = ref<string | ArrayBuffer | null>(null);

// 烟雾生成
const generatedSmoke = ref<string>('');
const inProgress = ref<boolean>(false);
async function jointSmoke() {
    if (!uploadedImage.value || !uploadedSrc.value) {
        toast.add({ severity: 'error', summary: '请先上传图片！', life: 3000 });
        return;
    }
    active.value = 2;
    inProgress.value = true;

    let cropData: { x: number, y: number, width: number, height: number } = cropper.value.getData();

    // 发送生成烟雾请求
    const formData = new FormData();
    formData.append('token', tokenStore.token);
    formData.append('input_pic', uploadedImage.value);
    formData.append('smoke_id', smokes.value[selectedMask.value].id);
    formData.append('pos1', "(" + cropData.x.toFixed(0).toString() + ", " + cropData.y.toFixed(0).toString() + ")");
    formData.append(
        'pos2',
        "(" + (cropData.x + cropData.width).toFixed(0).toString() + ", "
        + (cropData.y + cropData.height).toFixed(0).toString() + ")"
    );

    await new Promise((resolve) => setTimeout(resolve, 3000));
    axios.post('/smoke/joint', formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
    }).then((res) => {
        if (res.data.status === 200) {
            const obj = res.data.obj;
            generatedSmoke.value = obj.url;
            toast.add({ severity: 'success', summary: '烟雾合成成功！', detail: res.data.message, life: 3000 });
            router.push('/dashboard/explore/synthesis/' + obj.id);
        }
        else
            toast.add({ severity: 'error', summary: '烟雾合成失败！', detail: res.data.message, life: 3000 });
        inProgress.value = false;
    }).catch((err) => {
        toast.add({ severity: 'error', summary: '烟雾合成失败！', detail: err.message, life: 3000 });
    })
}

// 图片上传
function uploader(event: any) {
    const file: File = event.files[0];
    const reader = new FileReader();
    reader.onload = (event) => {
        if (event.target) {
            uploadedSrc.value = event.target.result;
            cropper.value.replace(uploadedSrc.value)
        }
    };
    uploadedImage.value = file;
    reader.readAsDataURL(file);
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
                    <h1 class="text-2xl font-bold m-0">烟雾拼接</h1>
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
                                    <h2 class="text-lg font-bold pl-10">选择烟雾</h2>
                                    <div class="flex justify-center items-center">
                                        <Carousel class="w-30rem" :page="selectedMask" @update:page="maskChanged"
                                            :value="smokes" :numVisible="1" :numScroll="1">
                                            <template #item="slotProps">
                                                <div class="b-1.5 b-solid b-coolGray b-rd m-2 p-3">
                                                    <div class="flex justify-center items-center">
                                                        <div class="relative mx-auto">
                                                            <Image class="w-20rem h-20rem" imageClass="rounded"
                                                                :src="slotProps.data.url" preview>
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
                                        <Button label="上传图片" icon="pi pi-arrow-right" iconPos="right"
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
                                    <h2 class="text-lg font-bold pl-10">上传并框选图片</h2>
                                    <div class="flex justify-center items-center">
                                        <div
                                            :class="['justify-center items-center flex-col gap-2rem', (uploadedSrc ? 'flex' : 'hidden')]">
                                            <VueCropper class="max-w-full w-30rem" :zoomable="false" :view-mode="1"
                                                :aspect-ratio="16 / 9" :src="uploadedSrc" ref="cropper">
                                            </VueCropper>
                                            <Button icon="pi pi-times" label="取消"
                                                @click="uploadedSrc = null; uploadedImage = null"></Button>
                                        </div>
                                        <FileUpload v-if="!uploadedImage" mode="basic" name="demo[]" url="/api/upload"
                                            accept="image/*" chooseLabel="上传图片" customUpload @uploader="uploader"
                                            auto />
                                    </div>
                                    <div class="flex pt-4 justify-between">
                                        <Button label="选择烟雾" icon="pi pi-arrow-left" severity="secondary"
                                            @click="active = 0"></Button>
                                        <Button label="合成图片" icon="pi pi-arrow-right" iconPos="right"
                                            @click="jointSmoke"></Button>
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

<style scoped>
:deep(.cropper-point.point-se) {
    border-radius: 50%;
    height: 5px;
    width: 5px;
}
</style>