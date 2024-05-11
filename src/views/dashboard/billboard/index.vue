<script setup lang="ts">
import { onMounted, ref } from "vue";
import { FilterMatchMode } from "primevue/api";

import axios from "@/axios";
import router from "@/router";

const announcements = ref<any>();
async function getAnnouncementData() {
    let res = await axios.get("/billboard/all");
    announcements.value = res.data.data;
}

onMounted(async () => {
    // 页面渲染完成后获取公告内容
    await getAnnouncementData();
});
</script>

<template>
    <div class="flex flex-col w-full h-full">
        <Announcement></Announcement>
        <Toast></Toast>
        <TopBar></TopBar>
        <div
            class="grid md:grid-cols-4 lg:grid-cols-5 w-full p-1rem gap-4 h-full bg-#f8fafc dark:bg-dark-900"
        >
            <SidePanel class="grid col-span-1"></SidePanel>
            <Card class="grid md:col-span-3 lg:md:col-span-4">
                <template #title>
                    <div
                        class="flex flex-row items-center justify-between gap-2"
                    >
                        <h1 class="text-2xl font-bold m-0">系统公告</h1>
                    </div>
                </template>

                <template #content>
                    <div v-for="a in announcements" class="mb-4">
                        <Panel toggleable>
                            <template #header>
                                <div class="flex align-items-center gap-2">
                                    <span class="font-bold">{{ a.title }}</span>
                                </div>
                            </template>
                            <template #footer>
                                <div
                                    class="flex flex-wrap align-items-center justify-content-between gap-3"
                                >
                                    <span class="p-text-secondary">{{
                                        a.date
                                    }}</span>
                                    <span class="p-text-secondary">{{
                                        a.author
                                    }}</span>
                                    <span
                                        class="p-text-secondary underline font-bold"
                                        @click="
                                            router.push(
                                                '/dashboard/billboard/' + a.id
                                            )
                                        "
                                    >
                                        详情</span
                                    >
                                </div>
                            </template>
                            <p class="m-0">
                                {{ a.intro }}
                            </p>
                        </Panel>
                    </div>
                </template>
            </Card>
        </div>
    </div>
</template>

<style scoped></style>
