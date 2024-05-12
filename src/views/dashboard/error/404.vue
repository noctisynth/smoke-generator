<script setup lang="ts">
</script>

<template>
    <Announcement></Announcement>
    <div class="flex flex-col w-full h-full">
        <TopBar></TopBar>
        <div class="grid md:grid-cols-4 lg:grid-cols-5 w-full p-1rem gap-4 h-full bg-#f8fafc dark:bg-dark-900">
            <SidePanel class="grid col-span-1"></SidePanel>
            <Card class="grid md:col-span-3 lg:md:col-span-4">
                <template #title>
                    <h1 class="text-2xl font-bold m-0">错误</h1>
                </template>
                <template #content>
                    <Error :code="404" desc="页面未找到"></Error>
                </template>
            </Card>
        </div>
    </div>
</template>

<style scoped></style>