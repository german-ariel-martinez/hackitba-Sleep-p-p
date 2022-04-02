<template>
    <div class="divider">
        <div class="divider-outline">
            {{title}}
        </div>
    </div>
</template>

<script>
export default {
  props: {
    title: String
  }
}
</script>

<style scoped>
.divider {
    background-color: #202844;
    height: 200px;
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}
.divider-outline {
    background-color: none;
    width: 100%;
    height: 90%;
    border-style: solid;
    border-color: white;
    border-right: none;
    border-left: none;
    text-justify: center;
    font-size: 2.5em;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    color: white;
}
</style>