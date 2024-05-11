<script setup lang="ts">
import items from '@/scripts/items';
</script>

<template>
    <PanelMenu :model="items" class="w-full h-full">
        <template #item="{ item }">
            <a v-ripple class="flex items-center px-3 py-2 cursor-pointer">
                <span :class="[item.icon, 'text-primary']"></span>
                <span :class="['ml-2', { 'font-semibold': item.items }]">{{ item.label }}</span>
            </a>
        </template>
    </PanelMenu>
</template>

<style scoped></style>