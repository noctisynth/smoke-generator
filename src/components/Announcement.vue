<script setup lang="ts">
import { onMounted, ref } from 'vue';

// 公告内容
const announcement = ref<string>('');
const showAnnouncement = ref<boolean>(true);
async function fetchAnnouncement() {
    announcement.value = '公告内容';
}

onMounted(async () => {
    await fetchAnnouncement();
})
</script>

<template>
    <div :class="['fixed inset-x-0 bottom-0 p-4', (showAnnouncement ? '' : 'hidden')]">
        <div class="relative flex items-center justify-between rounded-lg bg-indigo-600 px-4 py-1 text-white shadow-lg">
            <p class="text-sm font-medium">
                {{ announcement }}
            </p>

            <Button @click="showAnnouncement = false" icon="pi pi-times text-coolGray hover:!text-white"
                class="hover:!bg-indigo-600 hover:!text-white" plain text>
            </Button>
        </div>
    </div>
</template>

<style scoped></style>