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
                    <h1 class="text-2xl font-bold m-0">探索</h1>
                </template>
                <template #content>
                    <div class="flex flex-col gap-4">
                        <div class="grid grid-cols-2 gap-4">
                            <ColoredCard title="烟雾拼接" href="/dashboard/explore/synthesis/" tag="拼接"
                                class="w-full h-full">
                            </ColoredCard>
                            <ColoredCard title="烟雾生成" href="/dashboard/explore/generate/" tag="生成"
                                class="w-full h-full">
                            </ColoredCard>
                        </div>
                    </div>
                </template>
            </Card>
        </div>
    </div>
</template>

<style scoped></style>