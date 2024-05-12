<script setup lang="ts">
import axios from '@/axios';
import { useAnnounceStore } from '@/stores/announce';
import { onMounted, ref } from 'vue';

const announceStore = useAnnounceStore();

// 公告内容
const announcement = ref<string>('');
const showAnnouncement = ref<boolean>(!announceStore.closed);
async function fetchAnnouncement() {
    axios.post('/billboard/latest').then(res => {
        if (res.data.status === 200) {
            announcement.value = res.data.data.content;
            showAnnouncement.value = true;
        } else {
            showAnnouncement.value = false;
        }
    }).catch(err => {
        showAnnouncement.value = false;
        console.error(err);
    });
    announcement.value = '公告内容';
}
function closeAnnouncement() {
    announceStore.close();
    showAnnouncement.value = false;
}

onMounted(async () => {
    await fetchAnnouncement();
})
</script>

<template>
    <div :class="['fixed inset-x-0 bottom-0 p-4 z-10000', { 'hidden': !showAnnouncement }]">
        <div class="relative flex items-center justify-between rounded-lg bg-indigo-600 px-4 py-1 text-white shadow-lg">
            <p class="text-sm font-medium">
                {{ announcement }}
            </p>

            <Button @click="closeAnnouncement" icon="pi pi-times text-coolGray hover:!text-white"
                class="hover:!bg-indigo-600 hover:!text-white" plain text>
            </Button>
        </div>
    </div>
</template>

<style scoped></style>