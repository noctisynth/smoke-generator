<script setup lang="ts">
import Reveal from 'reveal.js';
import { onMounted } from 'vue';

// 局部导入 Reveal.js 样式
import "reveal.js/dist/reveal.css";
import "reveal.js/dist/theme/black.css";

// 页面跳转
function direct(to: string) {
    window.location.href = "/#" + to;
    window.location.reload(); // 确保 Reveal.js 在新页面中被销毁
}

onMounted(() => {
    // 初始化 Reveal.js
    Reveal.initialize({
        // 设置 Reveal.js 为垂直滚动模式
        view: 'scroll',
        // 设置 Reveal.js 展示页面顺序
        scrollProgress: true
    });
});
</script>

<template>
    <div>
        <div class="reveal">
            <div class="slides">
                <section data-auto-animate
                    data-background-image="https://images.unsplash.com/photo-1556388275-bb5585725aca?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D">
                    <div class="sl-block">
                        <div class="sl-block-content fragment semi-fade-out reduced-lh" data-placeholder-tag="p"
                            data-fragment-index="0">
                            <h2>欢迎使用</h2>
                        </div>
                    </div>
                    <div class="sl-block">
                        <div class="sl-block-content" data-placeholder-tag="p">
                            <h1 class="text-white text-5xl" data-fragment-index="1">烟雾拼接生成系统</h1>
                        </div>
                    </div>
                </section>
                <section data-auto-animate
                    data-background-image="https://images.unsplash.com/photo-1556388275-bb5585725aca?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D">
                    <div class="sl-block">
                        <div class="sl-block-content" data-placeholder-tag="p">
                            <h1 class="!text-red-200 text-5xl" data-fragment-index="0">烟雾拼接生成系统</h1>
                        </div>
                    </div>
                    <div class="sl-block">
                        <div class="sl-block-content fragment fade-in-then-semi-out reduced-lh" data-placeholder-tag="p"
                            data-fragment-index="1">
                            <div class="pt-5">
                                <i class="pi pi-arrow-down navigate-next"></i>
                            </div>
                        </div>
                    </div>
                </section>

                <section data-background-color="cool-gray" data-auto-animate>
                    <div class="sl-block">
                        <div class="sl-block-content fragment current-visible reduced-lh" data-placeholder-tag="p">
                            <h2>烟雾拼接</h2>
                        </div>
                    </div>
                    <div class="sl-block">
                        <div class="sl-block-content" data-placeholder-tag="p">
                            <img class="r-stretch" src="/images/nosmoke_baidu_1230_000014.jpg">
                            <p>上传图片</p>
                        </div>
                    </div>
                </section>

                <section data-background-color="cool-gray" data-auto-animate>
                    <div class="sl-block">
                        <div class="sl-block-content" data-placeholder-tag="p">
                            <img data-id="img" class="r-stretch" src="/images/nosmoke_baidu_1230_000014.jpg">
                            <p>上传图片</p>
                        </div>
                    </div>
                </section>

                <section data-background-color="#232121" data-auto-animate>
                    <div class="sl-block">
                        <div class="sl-block-content flex flex-row justify-between items-center"
                            data-placeholder-tag="p">
                            <img data-id="img" src="/images/nosmoke_baidu_1230_000014.jpg">
                            <i class="pi pi-plus"></i>
                            <img class="r-frame" src="/images/istockphoto-841821290-640_adpp_is_000120.jpg">
                        </div>
                        <div class="sl-block-content fragment fade-in-then-semi-out reduced-lh"
                            data-placeholder-tag="p">
                            <div class="pt-5"><i class="pi pi-arrow-down navigate-next"></i></div>
                        </div>
                    </div>
                </section>

                <section data-background-color="cool-gray" data-auto-animate>
                    <div class="sl-block">
                        <div class="sl-block-content" data-placeholder-tag="p">
                            <img data-id="img" src="/images/a.jpg" class="w-400px max-w-80%">
                        </div>
                        <div class="sl-block-content fragment fade-in-then-semi-out reduced-lh"
                            data-placeholder-tag="p">
                            <span>烟雾拼接合成</span>
                        </div>
                    </div>
                </section>

                <section data-background-color="#111111" data-auto-animate>
                    <div class="sl-block">
                        <div class="sl-block-content" data-placeholder-tag="p">
                            <h1 class="r-fit-text text-white text-5xl">任何人都可以免费注册</h1>
                        </div>
                    </div>
                </section>

                <section data-background-color="#111111" data-auto-animate>
                    <div class="sl-block">
                        <div class="sl-block-content" data-placeholder-tag="p">
                            <h1 class="r-fit-text text-white text-5xl">任何人都可以免费注册</h1>
                        </div>
                    </div>
                    <div class="sl-block">
                        <div class="sl-block-content mt-4rem flex flex-row gap-4rem items-center justify-start"
                            data-placeholder-tag="p">
                            <div @click="direct('/register')"
                                class="b-white hover:bg-dark hover:cursor-pointer b-8px b-solid flex justify-center items-center">
                                <h2 class="p-8px">免费注册</h2>
                            </div>
                            <div @click="direct('/login')"
                                class="bg-white hover:bg-coolGray hover:cursor-pointer sl-block-content flex justify-center items-center"
                                data-placeholder-tag="p">
                                <h2 class="!text-purple-700 p-16px">登录</h2>
                            </div>
                        </div>
                    </div>
                </section>
            </div>
        </div>
    </div>
</template>

<style scoped></style>