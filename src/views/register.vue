<script setup lang="ts">
import { ref } from 'vue';
import { useToast } from 'primevue/usetoast';
// @ts-ignore 忽略 vue-img-cutter 类型错误
import ImgCutter from 'vue-img-cutter';

const toast = useToast();

// 正在活跃的注册窗口
const active = ref(0);

// 注册参数
const username = ref('');
const email = ref('');
const password = ref('');
const confirmPassword = ref('');

// 用户资料
const phone = ref('');
const type = ref('');
const avatar = ref<Blob | null>(null);
const avatarUrl = ref('');
const typeOptions = ['企业', '个人']

// 人机验证
const verified = ref(false);
const inCheckProgress = ref(false);
async function toggleVerified() {
    inCheckProgress.value = true;
    await new Promise((resolve) => setTimeout(resolve, 2000));
    inCheckProgress.value = false;
    verified.value = !verified.value;
}

// 验证账户信息
async function validate() {
    if (!username.value) {
        toast.add({ severity: 'error', summary: '错误', detail: '请输入用户名！', life: 3000 });
        return;
    }
    if (!email.value) {
        toast.add({ severity: 'error', summary: '错误', detail: '请输入邮箱！', life: 3000 });
        return;
    }
    if (!password.value) {
        toast.add({ severity: 'error', summary: '错误', detail: '请输入密码！', life: 3000 });
        return;
    }
    if (password.value !== confirmPassword.value) {
        toast.add({ severity: 'error', summary: '错误', detail: '两次输入的密码不一致！', life: 3000 });
        return;
    }
    if (!verified.value) {
        toast.add({ severity: 'error', summary: '错误', detail: '请先完成人机验证！', life: 3000 });
        return;
    }

    // 信息正确，切换到用户资料页面
    active.value = 1;
}

// 剪切并上传头像
function cutDown(value: { index: null; fileName: string; file: File; blob: Blob, dataURL: string }) {
    avatarUrl.value = value.dataURL;
}

// 注册
const inProgress = ref(false);
async function register() {
    if (!phone.value) {
        toast.add({ severity: 'error', summary: '错误', detail: '请输入手机号！', life: 3000 });
        return;
    }
    if (!type.value) {
        toast.add({ severity: 'error', summary: '错误', detail: '请选择用户类型！', life: 3000 });
        return;
    }
    if (!avatarUrl.value) {
        toast.add({ severity: 'error', summary: '错误', detail: '请上传头像！', life: 3000 });
        return;
    }

    // 注册
    inProgress.value = true;
    await new Promise((resolve) => setTimeout(resolve, 2000));
    inProgress.value = false;

    // 注册成功，切换到成功页面
    active.value = 2;
}
</script>

<template>
    <section class="bg-#f8fafc">
        <Toast class="w-20rem max-w-90%"></Toast>
        <div class="lg:grid lg:min-h-screen lg:grid-cols-12">
            <section class="relative flex h-32 items-end bg-gray-900 lg:col-span-5 lg:h-full xl:col-span-6">
                <img alt=""
                    src="https://images.unsplash.com/photo-1617195737496-bc30194e3a19?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80"
                    class="absolute inset-0 h-full w-full object-cover opacity-80" />

                <div class="hidden lg:relative lg:block lg:p-12">
                    <a class="block text-white" href="#">
                        <span class="sr-only">注册</span>
                        <svg class="h-8 sm:h-10" viewBox="0 0 28 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path
                                d="M0.41 10.3847C1.14777 7.4194 2.85643 4.7861 5.2639 2.90424C7.6714 1.02234 10.6393 0 13.695 0C16.7507 0 19.7186 1.02234 22.1261 2.90424C24.5336 4.7861 26.2422 7.4194 26.98 10.3847H25.78C23.7557 10.3549 21.7729 10.9599 20.11 12.1147C20.014 12.1842 19.9138 12.2477 19.81 12.3047H19.67C19.5662 12.2477 19.466 12.1842 19.37 12.1147C17.6924 10.9866 15.7166 10.3841 13.695 10.3841C11.6734 10.3841 9.6976 10.9866 8.02 12.1147C7.924 12.1842 7.8238 12.2477 7.72 12.3047H7.58C7.4762 12.2477 7.376 12.1842 7.28 12.1147C5.6171 10.9599 3.6343 10.3549 1.61 10.3847H0.41ZM23.62 16.6547C24.236 16.175 24.9995 15.924 25.78 15.9447H27.39V12.7347H25.78C24.4052 12.7181 23.0619 13.146 21.95 13.9547C21.3243 14.416 20.5674 14.6649 19.79 14.6649C19.0126 14.6649 18.2557 14.416 17.63 13.9547C16.4899 13.1611 15.1341 12.7356 13.745 12.7356C12.3559 12.7356 11.0001 13.1611 9.86 13.9547C9.2343 14.416 8.4774 14.6649 7.7 14.6649C6.9226 14.6649 6.1657 14.416 5.54 13.9547C4.4144 13.1356 3.0518 12.7072 1.66 12.7347H0V15.9447H1.61C2.39051 15.924 3.154 16.175 3.77 16.6547C4.908 17.4489 6.2623 17.8747 7.65 17.8747C9.0377 17.8747 10.392 17.4489 11.53 16.6547C12.1468 16.1765 12.9097 15.9257 13.69 15.9447C14.4708 15.9223 15.2348 16.1735 15.85 16.6547C16.9901 17.4484 18.3459 17.8738 19.735 17.8738C21.1241 17.8738 22.4799 17.4484 23.62 16.6547ZM23.62 22.3947C24.236 21.915 24.9995 21.664 25.78 21.6847H27.39V18.4747H25.78C24.4052 18.4581 23.0619 18.886 21.95 19.6947C21.3243 20.156 20.5674 20.4049 19.79 20.4049C19.0126 20.4049 18.2557 20.156 17.63 19.6947C16.4899 18.9011 15.1341 18.4757 13.745 18.4757C12.3559 18.4757 11.0001 18.9011 9.86 19.6947C9.2343 20.156 8.4774 20.4049 7.7 20.4049C6.9226 20.4049 6.1657 20.156 5.54 19.6947C4.4144 18.8757 3.0518 18.4472 1.66 18.4747H0V21.6847H1.61C2.39051 21.664 3.154 21.915 3.77 22.3947C4.908 23.1889 6.2623 23.6147 7.65 23.6147C9.0377 23.6147 10.392 23.1889 11.53 22.3947C12.1468 21.9165 12.9097 21.6657 13.69 21.6847C14.4708 21.6623 15.2348 21.9135 15.85 22.3947C16.9901 23.1884 18.3459 23.6138 19.735 23.6138C21.1241 23.6138 22.4799 23.1884 23.62 22.3947Z"
                                fill="currentColor" />
                        </svg>
                    </a>

                    <h2 class="mt-6 text-2xl font-bold text-white sm:text-3xl md:text-4xl">
                        欢迎注册烟雾生成系统 🦑
                    </h2>

                    <p class="mt-4 leading-relaxed text-white/90">
                        烟雾生成系统是一个基于机器学习的智能烟雾生成系统，可以帮助你快速生成符合你的风格的烟雾。
                    </p>
                </div>
            </section>

            <main
                class="flex items-center justify-center px-8 py-8 sm:px-12 lg:col-span-7 lg:px-16 lg:py-12 xl:col-span-6">
                <div class="max-w-xl lg:max-w-3xl">
                    <div class="relative -mt-16 block lg:hidden">
                        <a class="inline-flex size-16 items-center justify-center rounded-full bg-white text-blue-600 sm:size-20"
                            href="#">
                            <span class="sr-only">注册</span>
                            <svg class="h-8 sm:h-10" viewBox="0 0 28 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path
                                    d="M0.41 10.3847C1.14777 7.4194 2.85643 4.7861 5.2639 2.90424C7.6714 1.02234 10.6393 0 13.695 0C16.7507 0 19.7186 1.02234 22.1261 2.90424C24.5336 4.7861 26.2422 7.4194 26.98 10.3847H25.78C23.7557 10.3549 21.7729 10.9599 20.11 12.1147C20.014 12.1842 19.9138 12.2477 19.81 12.3047H19.67C19.5662 12.2477 19.466 12.1842 19.37 12.1147C17.6924 10.9866 15.7166 10.3841 13.695 10.3841C11.6734 10.3841 9.6976 10.9866 8.02 12.1147C7.924 12.1842 7.8238 12.2477 7.72 12.3047H7.58C7.4762 12.2477 7.376 12.1842 7.28 12.1147C5.6171 10.9599 3.6343 10.3549 1.61 10.3847H0.41ZM23.62 16.6547C24.236 16.175 24.9995 15.924 25.78 15.9447H27.39V12.7347H25.78C24.4052 12.7181 23.0619 13.146 21.95 13.9547C21.3243 14.416 20.5674 14.6649 19.79 14.6649C19.0126 14.6649 18.2557 14.416 17.63 13.9547C16.4899 13.1611 15.1341 12.7356 13.745 12.7356C12.3559 12.7356 11.0001 13.1611 9.86 13.9547C9.2343 14.416 8.4774 14.6649 7.7 14.6649C6.9226 14.6649 6.1657 14.416 5.54 13.9547C4.4144 13.1356 3.0518 12.7072 1.66 12.7347H0V15.9447H1.61C2.39051 15.924 3.154 16.175 3.77 16.6547C4.908 17.4489 6.2623 17.8747 7.65 17.8747C9.0377 17.8747 10.392 17.4489 11.53 16.6547C12.1468 16.1765 12.9097 15.9257 13.69 15.9447C14.4708 15.9223 15.2348 16.1735 15.85 16.6547C16.9901 17.4484 18.3459 17.8738 19.735 17.8738C21.1241 17.8738 22.4799 17.4484 23.62 16.6547ZM23.62 22.3947C24.236 21.915 24.9995 21.664 25.78 21.6847H27.39V18.4747H25.78C24.4052 18.4581 23.0619 18.886 21.95 19.6947C21.3243 20.156 20.5674 20.4049 19.79 20.4049C19.0126 20.4049 18.2557 20.156 17.63 19.6947C16.4899 18.9011 15.1341 18.4757 13.745 18.4757C12.3559 18.4757 11.0001 18.9011 9.86 19.6947C9.2343 20.156 8.4774 20.4049 7.7 20.4049C6.9226 20.4049 6.1657 20.156 5.54 19.6947C4.4144 18.8757 3.0518 18.4472 1.66 18.4747H0V21.6847H1.61C2.39051 21.664 3.154 21.915 3.77 22.3947C4.908 23.1889 6.2623 23.6147 7.65 23.6147C9.0377 23.6147 10.392 23.1889 11.53 22.3947C12.1468 21.9165 12.9097 21.6657 13.69 21.6847C14.4708 21.6623 15.2348 21.9135 15.85 22.3947C16.9901 23.1884 18.3459 23.6138 19.735 23.6138C21.1241 23.6138 22.4799 23.1884 23.62 22.3947Z"
                                    fill="currentColor" />
                            </svg>
                        </a>

                        <h1 class="mt-2 text-2xl font-bold text-gray-900 sm:text-3xl md:text-4xl">
                            欢迎注册烟雾生成系统 🦑
                        </h1>

                        <p class="mt-4 leading-relaxed text-gray-500">
                            烟雾生成系统是一个基于机器学习的智能烟雾生成系统，可以帮助你快速生成符合你的风格的烟雾。
                        </p>
                    </div>

                    <Card class="w-600px max-w-full">
                        <template #content>
                            <Stepper v-model:activeStep="active" linear>
                                <StepperPanel>
                                    <template #header="{ index, clickCallback }">
                                        <button class="bg-transparent border-none inline-flex flex-col gap-2"
                                            @click="clickCallback">
                                            <span
                                                :class="['b-rd b-solid w-3rem h-3rem inline-flex items-center justify-center', { 'b-blueGray': index >= active, 'bg-emerald !b-none': index < active }]">
                                                <i class="pi pi-user"></i>
                                            </span>
                                        </button>
                                    </template>
                                    <template #content>
                                        <div class="flex flex-col gap-4 mx-auto"
                                            style="min-height: 16rem; max-width: 20rem">
                                            <div class="text-center mt-3 mb-3 text-xl font-semibold">创建账户</div>
                                            <div class="field p-fluid">
                                                <IconField>
                                                    <InputIcon>
                                                        <i class="pi pi-user"></i>
                                                    </InputIcon>
                                                    <InputText id="username" v-model="username" type="text"
                                                        placeholder="用户名" />
                                                </IconField>
                                            </div>
                                            <div class="field p-fluid">
                                                <IconField>
                                                    <InputIcon>
                                                        <i class="pi pi-envelope"></i>
                                                    </InputIcon>
                                                    <InputText id="email" v-model="email" type="email"
                                                        placeholder="邮箱" />
                                                </IconField>
                                            </div>
                                            <div class="field p-fluid">
                                                <Password v-model="password" toggleMask placeholder="密码" />
                                            </div>
                                            <div class="field p-fluid">
                                                <Password v-model="confirmPassword" toggleMask placeholder="确认密码" />
                                            </div>

                                            <div class="b-rd b-solid b-blueGray b-1 bg-#f8fafc">
                                                <div class="flex justify-between p-2">
                                                    <div v-if="!inCheckProgress && !verified"
                                                        class="pl-3 inline-flex items-center gap-2">
                                                        <Checkbox v-model="verified" @click="toggleVerified"></Checkbox>
                                                        <span class="text-15px text-coolGray-600">点击进行人机验证</span>
                                                    </div>
                                                    <div v-else-if="inCheckProgress && !verified"
                                                        class="pl-3 inline-flex items-center gap-2">
                                                        <ProgressSpinner class="!w-30px !h-30px" strokeWidth="3" />
                                                    </div>
                                                    <div v-else class="pl-3 inline-flex items-center gap-2">
                                                        <i class="pl-1 pi pi-check-circle text-emerald-500 
                                                        !text-20px"></i>
                                                    </div>
                                                    <div class="flex flex-col gap-1 justify-center items-center">
                                                        <Image imageClass="w-2rem h-2rem"
                                                            src="https://www.gstatic.cn/recaptcha/api2/logo_48.png">
                                                        </Image>
                                                        <div class="inline-flex items-center gap-1">
                                                            <span class="text-10px">隐私权 - 使用条款</span>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>

                                            <div class="flex justify-end">
                                                <span class="text-12px text-gray-500">已有帐户？<span
                                                        class="hover:text-blue-500 cursor-pointer"
                                                        @click="$router.push('/login')">登录</span></span>
                                            </div>
                                        </div>

                                        <div class="flex justify-end mt-2rem">
                                            <Button label="下一步" icon="pi pi-arrow-right" iconPos="right"
                                                @click="validate"></Button>
                                        </div>
                                    </template>
                                </StepperPanel>
                                <StepperPanel>
                                    <template #header="{ index, clickCallback }">
                                        <button class="bg-transparent border-none inline-flex flex-col gap-2"
                                            @click="clickCallback">
                                            <span
                                                :class="['b-rd b-solid w-3rem h-3rem inline-flex items-center justify-center', { 'b-blueGray': index >= active, 'bg-emerald !b-none': index < active }]">
                                                <i class="pi pi-id-card"></i>
                                            </span>
                                        </button>
                                    </template>
                                    <template #content="{ prevCallback }">
                                        <div class="flex flex-col gap-4 mx-auto"
                                            style="min-height: 16rem; max-width: 20rem">
                                            <div class="text-center mt-3 mb-3 text-xl font-semibold">设置用户资料</div>
                                            <div class="inline-flex items-center justify-between px-4rem">
                                                <span class="text-15px text-gray-500">上传头像</span>
                                                <ImgCutter :tool="false" :toolBoxOverflow="false" @cutDown="cutDown">
                                                    <template #open>
                                                        <div class="group w-5rem h-5rem inline-flex items-center justify-center
                                                    hover:bg-coolGray-400 bg-coolGray-200 cursor-pointer b-rd ">
                                                            <i v-if="!avatarUrl" class="pi pi-user"></i>
                                                            <img v-else :src="avatarUrl" alt="avatar"
                                                                class="w-full h-full object-cover b-rd">
                                                        </div>
                                                    </template>
                                                </ImgCutter>
                                            </div>
                                            <div class="field p-fluid">
                                                <Dropdown v-model="type" :options="typeOptions" placeholder="用户类型">
                                                </Dropdown>
                                            </div>
                                            <div class="field p-fluid">
                                                <IconField>
                                                    <InputIcon>
                                                        <i class="pi pi-phone"></i>
                                                    </InputIcon>
                                                    <InputText id="phone" v-model="phone" type="text"
                                                        placeholder="手机号" />
                                                </IconField>
                                            </div>
                                        </div>

                                        <div class="flex pt-4 justify-between mt-2rem">
                                            <Button label="上一步" severity="secondary" icon="pi pi-arrow-left"
                                                @click="prevCallback"></Button>
                                            <Button label="注册"
                                                :icon="(inProgress ? 'pi pi-spinner pi-spin' : 'pi pi-check')"
                                                iconPos="right" @click="register"></Button>
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
                                        <div class="flex flex-col gap-2 mx-auto"
                                            style="min-height: 16rem; max-width: 24rem">
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
                        </template>
                    </Card>
                </div>
            </main>
        </div>
    </section>
</template>

<style scoped>
:deep(.btn-xs) {
    display: none;
}

:deep(.copyright) {
    display: none !important;
}
</style>
