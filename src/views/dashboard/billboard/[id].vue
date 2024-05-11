<script setup lang="ts">
import axios from "@/axios";
import { onMounted, ref } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();
const a = ref<any>();
async function getA() {
    let res = await axios.get(`/billboard/get/${route.params.id}`);

    if (res.data.status == 404) {
    } else {
        let data = res.data;
        a.value = data.data;
    }
}
onMounted(async () => {
    await getA();
});
</script>
<template>
    <div class="flex flex-col w-full h-full">
        <Announcement></Announcement>
        <Toast></Toast>
        <TopBar></TopBar>
        <Card v-if="a" class="mt-5 ml-10 mr-10 mb-5 h-full">
            <template #title>
                <div class="flex justify-center items-center">
                    {{ a.title }}
                </div>
                <div class="ml-15 mt-5 text-sm">{{ a.date }}</div>
                <Divider />
            </template>
            <template #content>
                <ScrollPanel style="width: 100%; height: 200px">
                    <div class="ml-30 mr-30">
                        <p>{{ a.content }}</p>
                    </div>
                </ScrollPanel>
            </template>
        </Card>
    </div>
</template>

<style scoped></style>
