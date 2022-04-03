<template>
    <div class="postGrid">
        <div class="gridTitle">
            Posts
        </div>
        <div class="gridBody">
            <div v-for="post in posts" :key="post.id">
                <div class="postCard">
                    <div class="postCardTitle">
                        <span style="justify-self: start; margin-left: 2%">{{post.title}}</span>
                        <span style="justify-self: end; margin-right: 2%">by {{post.author}} - ({{post.score}}<b-icon icon="star" style="color:#c62034;"></b-icon>)</span>
                    </div> 
                    <div class="postCardText">{{post.text}}</div>
                    <div class="postCardButtons">
                        <div><b-icon class="h2" icon="arrow-up-square" style="color:green;"></b-icon></div>
                        <div><b-icon class="h2" icon="arrow-down-square" style="color:#c62034"></b-icon></div>
                    </div>
                    <div class="postCardComments">
                        <div v-for="com in post.comments" :key="com.id">
                            <span>Comment by {{com.author}}: {{com.text}} - <b-icon icon="arrow-up-square" style="color:green;"></b-icon> <b-icon icon="arrow-down-square" style="color:#c62034;"></b-icon> - ({{com.score}}<b-icon icon="star" style="color:#c62034;"></b-icon>)</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>    
    </div>
</template>

<style scoped>
    .postCardComments {
        display: grid;
        justify-items: center;
        align-items: center;
    }
    .postCardButtons {
        display: grid;
        grid-template-columns: 1fr 1fr;
        justify-items: center;
        align-items: center;
        margin-top: 1%;
        color: black;
        border-bottom: #c62034 2px solid;
    }
    .postCardText {
        display: grid;
        justify-items: center;
        align-items: center;
        text-align: justify;
        padding: 2%;
        border-bottom: #c62034 2px solid;
    }
    .postCardTitle {
        display: grid;
        grid-template-columns: 1fr 1fr;
        padding: 1%;
        color: black;
        border-bottom: #c62034 2px solid;
    }
    .postCard {
        display: grid;
        grid-template-rows: 1fr 4fr 1fr 1fr;
        grid-auto-rows: auto;
        width: 70vw;
        background-color: white;
        margin-bottom: 2%;
    }
    .postCard:first-child {
        margin-top: 2%;
    }
    .gridTitle {
        display: grid;
        justify-items: start;
        align-items: center;
        width: 96%;
        margin-right: 2%;
        margin-left: 2%;
        font-size: 5vh;
        color: black;
        border-bottom: #c62034 2px solid;
    }
    .gridBody {
        display: grid;
        justify-items: center;
        align-items: center;
        height: 100vh;
    }
</style>

<script>
import axios from "axios"
export default {
    data() {
        return {
            posts: []
        }
    },
    methods: {
        getPosts() {
            axios.get( "/posts" )
                 .then( res => {
                     this.posts = res.data;
                 }).catch(e => {console.log(e)})
        },
    },
    mounted() {
        this.getPosts()
    }
}
</script>