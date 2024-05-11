<script setup lang="ts">
import { onMounted, ref } from "vue";
import items from "@/scripts/items";
import { FilterMatchMode } from "primevue/api";
import { useToast } from "primevue/usetoast";
import { useTokenStore } from "@/stores/token";

const toast = useToast();
const useToken = useTokenStore();

import axios from "@/axios";
const menu = ref();

// 公告内容
const announcement = ref<string>("");
const showAnnouncement = ref<boolean>(true);
async function fetchAnnouncement() {
    announcement.value = "公告内容";
}

const announcements = ref<any>();
async function getAnnouncementData() {
    let res = await axios.get("/billboard/all");
    announcements.value = res.data.data;
    console.log(announcements);
}
const filters = ref({
    global: { value: null, matchMode: FilterMatchMode.CONTAINS },
    name: { value: null, matchMode: FilterMatchMode.STARTS_WITH },
    author: { value: null, matchMode: FilterMatchMode.STARTS_WITH },
    date: { value: null, matchMode: FilterMatchMode.STARTS_WITH },
});
onMounted(async () => {
    // 页面渲染完成后获取公告内容

    await fetchAnnouncement();
    await getAnnouncementData();
});
</script>

<template>
    <div class="flex flex-col w-full h-full">
        <Announcement></Announcement>
        <Toast></Toast>
        <TopBar></TopBar>
        <div
            class="grid grid-cols-4 w-full p-1rem gap-4 h-full bg-#f8fafc dark:bg-dark-900"
        >
            <SidePanel class="grid col-span-1"></SidePanel>
            <Card class="grid col-span-3">
                <template #title>
                    <div
                        class="flex flex-row items-center justify-between gap-2"
                    >
                        <h1 class="text-2xl font-bold m-0">系统公告</h1>
                        <IconField iconPosition="left">
                            <InputIcon class="flex items-center justify-center">
                                <i class="pi pi-search"></i>
                            </InputIcon>
                            <InputText
                                v-model="filters['global'].value"
                                placeholder="关键词搜索"
                            />
                        </IconField>
                    </div>
                </template>

                <template #content>
                    <DataTable
                        v-model:filters="filters"
                        :value="announcements"
                        dataKey="id"
                        filterDisplay="row"
                    >
                        <template #empty>
                            <h2>暂无公告</h2>
                        </template>
                        <template #header>
                            <div class="flex justify-end"></div>
                        </template>
                        <Column field="title" header="标题"></Column>
                        <Column field="author" header="发布者"></Column>
                        <Column field="date" header="日期"></Column>
                    </DataTable>
                </template>
            </Card>
        </div>
    </div>
</template>

<style scoped></style>
