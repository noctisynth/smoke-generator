<script setup lang="ts">

</script>

<template>
    <div class="flex flex-col w-full h-full">
        <Announcement></Announcement>
        <Toast></Toast>
        <TopBar></TopBar>
        <div class="flex flex-row w-full p-1rem gap-4 h-full bg-#f8fafc dark:bg-dark-900">
            <SidePanel></SidePanel>
            <Card class="w-full h-full">
                <template #title>
                    <h1 class="text-2xl font-bold m-0">修改密码</h1>
                </template>
                <template #content>

                </template>
            </Card>
        </div>
    </div>
</template>

<style scoped></style>