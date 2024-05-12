<script setup lang="ts">
import { ref } from 'vue';
import axios from '@/axios';
import { useTokenStore } from '@/stores/token';
import { useRouter } from 'vue-router';
import { useUserStore } from '@/stores/user';
// @ts-ignore 忽略 vue-img-cutter 类型错误
import ImgCutter from 'vue-img-cutter';
import { useToast } from 'primevue/usetoast';

const toast = useToast();
const router = useRouter();
const tokenStore = useTokenStore();
const userStore = useUserStore();

if (!tokenStore.isLoggedIn()) {
    // 如果未登录，跳转到登录页面
    router.push('/login');
}

const isEditing = ref(false);
const newAvatar = ref<File | null>(null);
const typeOptions = ['个人', '企业'];

// 剪切并暂存头像
function updateAvatar(value: { index: null; fileName: string; file: File; blob: Blob, dataURL: string }) {
    newAvatar.value = value.file;
}

// 提交修改
function saveChanges() {
    const data = new FormData();
    data.append('token', tokenStore.token)
    data.append('username', userStore.username);
    data.append('email', userStore.email);
    data.append('phone', userStore.phone);
    data.append('status', userStore.status);
    if (newAvatar.value)
        data.append('avatar', newAvatar.value);
    axios.post('/account/update', data).then(res => {
        toast.add({ severity: 'success', summary: '更新成功', detail: '个人资料已更新成功！', life: 3000 });
        userStore.setUserInfo(res.data);
    }).catch(() => {
        toast.add({ severity: 'error', summary: '更新失败', detail: '服务器错误。', life: 3000 });
    }).finally(() => {
        isEditing.value = false;
    });
}
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
                    <div class="flex flex-row items-center justify-between gap-2">
                        <h1 class="text-2xl font-bold m-0">个人资料</h1>
                        <Button v-if="!isEditing" @click="isEditing = true" icon="pi pi-pencil"
                            severity="secondary"></Button>
                        <Button v-else @click="saveChanges" icon="pi pi-check"></Button>
                    </div>
                </template>
                <template #content>
                    <div v-if="!isEditing" class="flex flex-col gap-2rem m-2rem">
                        <div class="flex flex-row items-center gap-2rem">
                            <span class="text-sm font-bold">用户头像:</span>
                            <Avatar :image="userStore.avatar" size="xlarge" shape="circle"></Avatar>
                        </div>
                        <div class="flex flex-row items-center gap-2rem">
                            <span class="text-sm font-bold">用户名:</span>
                            <h2 class="text-sm font-medium m-0">
                                {{ userStore.username }}
                            </h2>
                        </div>
                        <div class="flex flex-row items-center gap-2rem">
                            <span class="text-sm font-bold">邮箱:</span>
                            <p class="text-sm font-medium m-0">
                                {{ userStore.email }}
                            </p>
                        </div>
                        <div class="flex flex-row items-center gap-2rem">
                            <span class="text-sm font-bold">账户类型:</span>
                            <p class="text-sm font-medium m-0">
                                {{ userStore.status }}
                            </p>
                        </div>
                        <div class="flex flex-row items-center gap-2rem">
                            <span class="text-sm font-bold">联系方式:</span>
                            <p class="text-sm font-medium m-0">
                                {{ userStore.phone }}
                            </p>
                        </div>
                    </div>
                    <div v-else class="flex flex-col gap-2rem m-2rem">
                        <div class="flex flex-row items-center gap-2rem">
                            <span class="text-sm font-bold">用户头像:</span>
                            <ImgCutter :tool="false" :toolBoxOverflow="false" @cutDown="updateAvatar">
                                <template #open>
                                    <div class="group w-5rem h-5rem inline-flex items-center justify-center
                                                    hover:bg-coolGray-400 bg-coolGray-200 cursor-pointer b-rd-full">
                                        <i v-if="!userStore.avatar" class="pi pi-user"></i>
                                        <img v-else :src="userStore.avatar" alt="avatar"
                                            class="w-full h-full object-cover b-rd">
                                    </div>
                                </template>
                            </ImgCutter>
                        </div>
                        <div class="flex flex-row items-center gap-2rem">
                            <span class="text-sm font-bold">用户名:</span>
                            <h2 class="text-sm font-medium m-0">
                                {{ userStore.username }}
                            </h2>
                        </div>
                        <div class="flex flex-row items-center gap-2rem">
                            <span class="text-sm font-bold">邮箱:</span>
                            <IconField>
                                <InputIcon>
                                    <i class="pi pi-envelope"></i>
                                </InputIcon>
                                <InputText id="email" v-model="userStore.email" type="text" placeholder="邮箱" />
                            </IconField>
                        </div>
                        <div class="flex flex-row items-center gap-2rem">
                            <span class="text-sm font-bold">账户类型:</span>
                            <Dropdown v-model="userStore.status" :options="typeOptions" placeholder="用户类型">
                            </Dropdown>
                        </div>
                        <div class="flex flex-row items-center gap-2rem">
                            <span class="text-sm font-bold">联系方式:</span>
                            <IconField>
                                <InputIcon>
                                    <i class="pi pi-user"></i>
                                </InputIcon>
                                <InputText id="phone" v-model="userStore.phone" type="text" placeholder="联系方式" />
                            </IconField>
                        </div>
                    </div>
                </template>
            </Card>
        </div>
    </div>
</template>

<style scoped>
:deep(.btn-xs) {
    display: none;
}

:deep(.copyright) {
    display: none !important;
}
</style>