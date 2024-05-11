<script setup lang="ts">
import { onMounted, ref } from "vue";
import items from "@/scripts/items";
import { FilterMatchMode } from "primevue/api";
// 右上角菜单
import DataTable from "primevue/datatable";
import Column from "primevue/column";
import axios from "@/axios";
const menu = ref();

// 公告内容
const announcement = ref<string>("");
const showAnnouncement = ref<boolean>(true);
async function fetchAnnouncement() {
    announcement.value = "公告内容";
}

const history_data = ref<any>();
const editingRows = ref<any>();
const visiables = ref([
    { label: "公开", value: true },
    { label: "私有", value: false },
]);
const visiable_list = ref([true, false]);
function getVisiable(e: any) {
    if (e) {
        return "公开";
    } else {
        return "私有";
    }
}
const filters = ref({
    global: { value: null, matchMode: FilterMatchMode.CONTAINS },
    name: { value: null, matchMode: FilterMatchMode.STARTS_WITH },
    date: { value: null, matchMode: FilterMatchMode.STARTS_WITH },
    visiable: { value: null, matchMode: FilterMatchMode.STARTS_WITH },
});

const onRowEditSave = (event: any) => {
    let { newData, index } = event;

    // post 修改值，图片url不会变，可依此 作为id
    history_data.value[index] = newData;
};
async function getHistoryData() {
    history_data.value = [
        {
            name: "2024_05_10_13_03_59zcLAn.jpg",
            user: "bash",
            type: "烟雾",
            date: "2024-05-10",
            url: "res/2024_05_10_13_03_59zcLAn.jpg",
            visiable: false,
        },
        {
            name: "2024_05_10_13_04_34A8paz.jpg",
            user: "bash",
            type: "烟雾",
            date: "2024-05-10",
            url: "res/2024_05_10_13_04_34A8paz.jpg",
            visiable: false,
        },
        {
            name: "2024_05_10_13_06_52RHxaL.jpg",
            user: "bash",
            type: "烟雾",
            date: "2024-05-10",
            url: "res/2024_05_10_13_06_52RHxaL.jpg",
            visiable: false,
        },
    ];
}

onMounted(async () => {
    // 页面渲染完成后获取公告内容

    await fetchAnnouncement();
    await getHistoryData();
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
                <DataTable
                    v-model:filters="filters"
                    :value="history_data"
                    dataKey="id"
                    filterDisplay="row"
                    :globalFilterFields="['name', 'date', 'visiable']"
                    v-model:editingRows="editingRows"
                    editMode="row"
                    @row-edit-save="onRowEditSave"
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
                    <Column field="url" header="图片">
                        <template #body="slotProps">
                            <Image
                                :src="slotProps.data.url"
                                :alt="123"
                                image-class="w-6rem b-rd"
                                class="w-6rem b-rd"
                                preview
                            />
                        </template>
                    </Column>
                    <Column field="name" header="名称">
                        <template #filter="{ filterModel, filterCallback }">
                            <InputText
                                v-model="filterModel.value"
                                type="text"
                                @input="filterCallback()"
                                class="p-column-filter"
                                placeholder="Name"
                            />
                        </template>
                        <template #editor="{ data, field }">
                            <InputText v-model="data[field]" />
                        </template>
                    </Column>
                    <Column field="date" header="日期">
                        <template #filter="{ filterModel, filterCallback }">
                            <InputText
                                v-model="filterModel.value"
                                type="text"
                                @input="filterCallback()"
                                class="p-column-filter"
                                placeholder="Date"
                            /> </template
                    ></Column>

                    <Column field="visiable" header="可见性">
                        <template #body="{ data }">
                            <Tag :value="getVisiable(data.visiable)" />
                        </template>
                        <template #filter="{ filterModel, filterCallback }">
                            <Dropdown
                                v-model="filterModel.value"
                                @change="filterCallback()"
                                :options="visiable_list"
                                placeholder="Select One"
                                :showClear="true"
                            >
                                <template #option="slotProps">
                                    <Tag
                                        :value="getVisiable(slotProps.option)"
                                    />
                                </template>
                            </Dropdown>
                        </template>

                        <template #editor="{ data, field }">
                            <Dropdown
                                v-model="data[field]"
                                :options="visiables"
                                optionLabel="label"
                                optionValue="value"
                                placeholder="Select a Status"
                            >
                            </Dropdown>
                        </template>
                    </Column>
                    <Column
                        :rowEditor="true"
                        style="width: 20%; min-width: 8rem"
                        bodyStyle="text-align:center"
                    ></Column>
                </DataTable>
            </div>
        </div>
    </div>
</template>

<style scoped></style>
