<script setup lang="ts">
import items from '@/scripts/items';
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
    <div class="flex flex-col w-full h-full">
        <TopBar></TopBar>
        <div class="flex flex-row w-full p-1rem gap-4 h-full bg-#f8fafc">
            <SidePanel></SidePanel>
            <Card class="w-full h-full">
                <template #title>
                    <h1 class="text-2xl font-bold m-0">错误</h1>
                </template>
                <template #content>
                    <Forbidden></Forbidden>
                </template>
            </Card>
        </div>
    </div>
</template>

<style scoped></style>