<script setup lang="ts">
const props = defineProps(['title', 'href', 'tag'])
</script>

<template>
    <article
        class="cursor-pointer hover:animate-background rounded-xl bg-gradient-to-r from-green-300 via-blue-500 to-purple-600 p-0.5 shadow-xl transition hover:bg-[length:400%_400%] hover:shadow-sm hover:[animation-duration:_4s]">
        <div class="rounded-[10px] bg-white dark:bg-gray-800 p-4 !pb-20 sm:p-6">
            <a class="underline-0" @click="$router.push(href)">
                <h3 class="mt-0.5 text-lg font-medium text-gray-900 dark:text-light">
                    {{ title }}
                </h3>
            </a>

            <div class="mt-4 flex flex-wrap gap-1">
                <span class="whitespace-nowrap rounded-full bg-purple-100 px-2.5 py-0.5 text-xs text-purple-600">
                    {{ tag }}
                </span>
            </div>
        </div>
    </article>
</template>

<style scoped></style>