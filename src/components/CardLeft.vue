<template>
    <div class="custom_card">
        <div class="card_body">
            <div class="card_body_inner_row">
                <div class="card_body_inner_col_text">
                    <div class="card_title"><b>{{this.title}}</b></div>
                    <div class="card_divider"></div>
                    <div class="card_text">
                        {{this.text}}
                    </div>
                </div>
                <div class="card_body_inner_col_img">
                    <img class="card_img" :src="require('@/assets/' + img + '')" alt="">
                </div>
              </div>
          </div>
      </div>
</template>

<script>
export default {
    props: {
        title: String,
        text: String,
        img: String
    }
}
</script>

<style scoped>
.custom_card {
    height: 50vh;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}
.card_body {
    border-left-style: solid;
    border-left-width: 5px;
    border-left-color: #c62034;
    width: 90%;
    display: flex;
    flex-direction: column;
}
.card_body_inner_row {
    display: flex;
    flex-direction: row;
    justify-content:center;
    align-items:center;
}
.card_body_inner_col_text {
    display: flex;
    flex-direction: column;
    width: 75%;
}
.card_body_inner_col_img {
    display: flex;
    flex-direction: column;
    width: 25%;
}
.card_img {
    height: 80%;
    width: 80%;
}
.card_title {
    display: flex;
    flex-direction: row;
    align-items: center;
    height: 20%;
    width: 90%;
    font-size: 3em;
    margin: 0 4vw;
}
.card_divider {
    width: 88%;
    border-style: solid;
    border-color: rgba(0, 0, 0, 0.2);
    border-width: thin;
    display: flex;
    flex-direction: row;
    margin: 0 4vw;
}
.card_text {
    margin: 0 4vw;
    padding: 10px 0;
    text-align: justify;
}
</style>