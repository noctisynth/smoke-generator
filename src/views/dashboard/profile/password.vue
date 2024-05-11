<script setup lang="ts">
import axios from '@/axios';
import { useTokenStore } from '@/stores/token';
import { useToast } from 'primevue/usetoast';
import { useRouter } from 'vue-router';
import { ref } from 'vue';

const toast = useToast();
const router = useRouter();
const tokenStore = useTokenStore();

const oldPassword = ref('');
const password = ref('');
const passwordConfirm = ref('');

function updatePassword() {
    if (!oldPassword.value) {
        toast.add({ severity: 'error', summary: '错误', detail: '请输入旧密码', life: 3000 });
        return;
    }
    if (!password.value) {
        toast.add({ severity: 'error', summary: '错误', detail: '请输入新密码', life: 3000 });
        return;
    }
    if (password.value !== passwordConfirm.value) {
        toast.add({ severity: 'error', summary: '错误', detail: '两次输入的密码不一致', life: 3000 });
        return;
    }
    axios.post('/account/update', { token: tokenStore.token, password: password.value }).then((res) => {
        if (res.data.status === 200) {
            toast.add({ severity: 'success', summary: '成功', detail: '密码修改成功', life: 3000 });
            tokenStore.removeToken();
            router.push('/login');
        }
        else
            toast.add({ severity: 'error', summary: '错误', detail: '密码修改失败', life: 3000 });
    }).catch(() => {
        toast.add({ severity: 'error', summary: '错误', detail: '密码修改失败', life: 3000 });
    });
}
</script>

<template>
    <div class="flex flex-col w-full h-full">
        <Announcement></Announcement>
        <Toast></Toast>
        <TopBar></TopBar>
        <div class="grid grid-cols-4 w-full p-1rem gap-4 h-full bg-#f8fafc dark:bg-dark-900">
            <SidePanel class="grid col-span-1"></SidePanel>
            <Card class="grid col-span-3">
                <template #title>
                    <h1 class="text-2xl font-bold m-0">修改密码</h1>
                </template>
                <template #content>
                    <div class="flex flex-col gap-4 m-3rem max-w-sm">
                        <InputText v-model="oldPassword" placeholder="请输入旧密码" type="password"></InputText>
                        <InputText v-model="password" placeholder="新密码" type="password"></InputText>
                        <InputText v-model="passwordConfirm" placeholder="密码确认" type="password"></InputText>
                        <div class="flex flex-row justify-end">
                            <Button @click="updatePassword" label="确认修改"></Button>
                        </div>
                    </div>
                </template>
            </Card>
        </div>
    </div>
</template>

<style scoped></style>