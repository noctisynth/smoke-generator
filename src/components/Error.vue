<script setup lang="ts">
defineProps(['code', 'desc'])
</script>

<template>
    <div class="grid h-full place-content-center bg-white px-4">
        <div class="text-center">
            <h1 class="text-9xl font-black text-gray-200">{{ code }}</h1>

            <p class="text-2xl font-bold tracking-tight text-gray-900 sm:text-4xl">Uh-oh!</p>

            <p class="mt-4 text-gray-500">{{ desc }}</p>

            <a @click="$router.push('/login')"
                class="cursor-pointer mt-6 inline-block rounded bg-indigo-600 px-5 py-3 text-sm font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring">
                返回主页
            </a>
        </div>
    </div>
</template>

<style scoped></style>