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
    <div
        :class="[
            'fixed inset-x-0 bottom-0 p-4',
            showAnnouncement ? '' : 'hidden',
        ]"
    >
        <div
            class="relative flex items-center justify-between rounded-lg bg-indigo-600 px-4 py-1 text-white shadow-lg"
        >
            <p class="text-sm font-medium">
                {{ announcement }}
            </p>

            <Button
                @click="showAnnouncement = false"
                icon="pi pi-times text-coolGray hover:!text-white"
                class="hover:!bg-indigo-600 hover:!text-white"
                plain
                text
            >
            </Button>
        </div>
    </div>
    <div class="flex flex-col w-full h-full">
        <TopBar></TopBar>
        <div class="flex flex-row w-full p-1rem gap-4 h-full bg-#f8fafc">
            <SidePanel></SidePanel>
            <Card class="w-full h-full">
                <template #title>
                    <h1 class="text-2xl font-bold m-0">系统公告</h1>
                </template>
                <template #content>
                    <DataTable
                        v-model:filters="filters"
                        :value="announcements"
                        dataKey="id"
                        filterDisplay="row"
                    >
                        <template #header>
                            <div class="flex justify-content-end">
                                <IconField iconPosition="left">
                                    <InputIcon>
                                        <i class="pi pi-search" />
                                    </InputIcon>
                                    <InputText
                                        v-model="filters['global'].value"
                                        placeholder="Keyword Search"
                                    />
                                </IconField>
                            </div>
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
