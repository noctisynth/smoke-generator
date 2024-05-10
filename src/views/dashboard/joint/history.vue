<script setup lang="ts">
import { onMounted, ref } from "vue";
import items from "@/scripts/items";
import { FilterMatchMode } from "primevue/api";
// 右上角菜单
import DataTable from "primevue/datatable";
import Column from "primevue/column";
const menu = ref();

// 公告内容
const announcement = ref<string>("");
const showAnnouncement = ref<boolean>(true);
async function fetchAnnouncement() {
    announcement.value = "公告内容";
}

onMounted(async () => {
    // 页面渲染完成后获取公告内容
    await fetchAnnouncement();
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
            <div class="card w-full h-full">
                <DataTable :globalFilterFields="['name', 'date', 'visiable']">
                    <Column field="pic" header="图片"> </Column>
                    <Column field="name" header="名称">
                        <template #filter="{ filterModel, filterCallback }">
                            <InputText
                                v-model="filterModel.value"
                                type="text"
                                @input="filterCallback()"
                                class="p-column-filter"
                                placeholder="Search by name"
                            /> </template
                    ></Column>
                    <Column field="date" header="日期"></Column>
                    <Column field="visiable" header="可见性"></Column>
                </DataTable>
            </div>
        </div>
    </div>
</template>

<style scoped></style>
