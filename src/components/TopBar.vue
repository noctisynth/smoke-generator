<script setup lang="ts">
import items from '@/scripts/items';
import { ref } from 'vue';

const menu = ref();
const theme = ref('light');

const toggle = (event: any) => {
    menu.value.toggle(event);
};

function changeTheme() {
    if (theme.value === 'light') {
        theme.value = 'dark';
        document.documentElement.classList.add('dark');
    } else {
        theme.value = 'light';
        document.documentElement.classList.remove('dark');
    }
}
</script>

<template>
    <Toolbar class="!border-rd-none">
        <template #start>
            <div class="pl-3 cursor-pointer">
                <span class="text-lg font-bold" @click="$router.push('/dashboard')">控制台</span>
            </div>
        </template>
        <template #end>
            <div class="inline-flex items-center gap-2">
                <Button :icon="(theme === 'light' ? 'pi pi-sun' : 'pi pi-moon')" @click="changeTheme" plain
                    text></Button>
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