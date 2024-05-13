<script setup lang="ts">
import { onMounted, ref } from "vue";
import { FilterMatchMode } from "primevue/api";
import { useToast } from "primevue/usetoast";
import { useTokenStore } from "@/stores/token";

const toast = useToast();
const useToken = useTokenStore();
// 右上角菜单
import DataTable from "primevue/datatable";
import Column from "primevue/column";
import axios from "@/axios";

const history_data = ref<any>();
const editingRows = ref<any>();
const visibilities = ref([
    { label: "公开", value: true },
    { label: "私有", value: false },
]);
const visibleList = ref([true, false]);
function getVisible(e: any) {
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
    visible: { value: null, matchMode: FilterMatchMode.STARTS_WITH },
});

const onRowEditSave = (event: any) => {
    let { newData, index } = event;

    let url = history_data.value[index].url;
    let type = history_data.value[index].type;
    let name = newData.name;
    let visible = newData.visible;
    axios
        .post("/smoke/update", {
            token: useToken.token,
            url: url,
            type: type,
            name: name,
            visible: visible,
        })
        .then((res) => {
            let data = res.data;
            if (data.status == 200) {
                toast.add({
                    severity: "success",
                    summary: "成功",
                    detail: "修改成功！",
                    life: 3000,
                });
                // post 修改值，图片url不会变，可依此 作为id
                history_data.value[index] = newData;
            } else {
                toast.add({
                    severity: "error",
                    summary: "错误",
                    detail: "修改失败",
                    life: 3000,
                });
            }
        });
};
async function getHistoryData() {
    let res = await axios.post("/smoke/generate_history", {
        token: useToken.token,
    });
    history_data.value = res.data.records;
}
async function deleteHistory(data: any) {
    let res = await axios.post("/smoke/delete", {
        token: useToken.token,
        type: data.type,
        url: data.url,
    });
    console.log(res);
    if (res.data.status == 200) {
        console.log(123);
        toast.add({
            severity: "success",
            summary: "成功",
            detail: "删除成功！",
            life: 3000,
        });
    }
    await getHistoryData();
}

onMounted(async () => {
    await getHistoryData();
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
                        <h1 class="text-2xl font-bold m-0">烟雾生成历史</h1>
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
                        :value="history_data"
                        dataKey="id"
                        filterDisplay="row"
                        :globalFilterFields="['name', 'date', 'visible']"
                        v-model:editingRows="editingRows"
                        editMode="row"
                        @row-edit-save="onRowEditSave"
                    >
                        <template #empty>
                            <h2>暂无历史数据</h2>
                        </template>
                        <template #header>
                            <div class="flex justify-end"></div>
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
                                    class="p-column-filter min-w-10rem"
                                    placeholder="名称"
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
                                    class="p-column-filter min-w-10rem"
                                    placeholder="时间"
                                />
                            </template>
                        </Column>

                        <Column field="visible" header="可见性">
                            <template #body="{ data }">
                                <Tag :value="getVisible(data.visible)" />
                            </template>
                            <template #filter="{ filterModel, filterCallback }">
                                <Dropdown
                                    v-model="filterModel.value"
                                    @change="filterCallback()"
                                    :options="visibleList"
                                    placeholder="选择"
                                    :showClear="true"
                                >
                                    <template #option="slotProps">
                                        <Tag
                                            :value="
                                                getVisible(slotProps.option)
                                            "
                                        />
                                    </template>
                                </Dropdown>
                            </template>

                            <template #editor="{ data, field }">
                                <Dropdown
                                    v-model="data[field]"
                                    :options="visibilities"
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
                        >
                        </Column>
                        <Column
                            header="删除"
                            style="width: 10%; min-width: 8rem"
                        >
                            <template #body="slotProps">
                                <Button
                                    @click="deleteHistory(slotProps.data)"
                                    label="删除"
                                ></Button>
                            </template>
                        </Column>
                    </DataTable>
                </template>
            </Card>
        </div>
    </div>
</template>

<style scoped></style>
