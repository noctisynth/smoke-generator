<script setup lang="ts">
</script>

<template>
    <Announcement></Announcement>
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