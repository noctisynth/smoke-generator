<script setup lang="ts">
import items from '@/scripts/items';
import { ref } from 'vue';

const menu = ref();

const toggle = (event: any) => {
    menu.value.toggle(event);
};
</script>

<template>
    <Toolbar class="!border-rd-none">
        <template #start>
            <div class="pl-3">
                <span class="text-lg font-bold">控制台</span>
            </div>
        </template>
        <template #end>
            <div class="inline-flex items-center gap-2">
                <IconField iconPosition="left">
                    <InputIcon>
                        <i class="pi pi-search"></i>
                    </InputIcon>
                    <InputText placeholder="搜索" />
                </IconField>
                <Button type="button" severity="secondary" icon="pi pi-ellipsis-v" @click="toggle" aria-haspopup="true"
                    aria-controls="overlay_menu"></Button>
                <Menu ref="menu" id="overlay_menu" :model="items" :popup="true"></Menu>
            </div>
        </template>
    </Toolbar>
</template>

<style scoped></style>