<template>
    <div class="postForm">
        <div class="postCard">
            <div class="title">Create a post</div>
            <div class="form">
                <input class="pt" type="text" placeholder="Post title">
                <textarea rows="16" cols="100" class="textArea" placeholder="Description" wrap=""/>
            </div>
            <div class="buttons">
                <button class="postAPost">Post</button>
            </div>
        </div>
    </div>
</template>

<style scoped>
    .buttons {
        display: grid;
        justify-items: center;
        align-items: center;
    }
    .postAPost {
        width: 95%;
        margin: auto;
        border: none;
        padding: 1%;
        background-color: #c62034;
        color: white;
    }
    .pt {
        width: 95%;
        height: 3vh;
        padding: 2%
    }
    .textArea {
      width: 95%;
      border-radius: 10px;
      border-style: solid;
      border-color: rgba(0, 0, 0, .2);
      padding-left: 1vw;
      padding-top: 1vh;
      resize: none;
      margin-bottom: 1vh;
    }
    .form {
        display: grid;
        grid-template-rows: 1fr 4fr;
        justify-items: center;
        align-items: center;
    }
    .title {
        display: grid;
        justify-items: start;
        align-items: center;
        font-size: 5vh;
        width: 100%;
        border-bottom: #c62034 2px solid;
        padding-left: 2%;
    }
    .postCard {
        display: grid;
        width: 70vw;
        height: 80vh;
        background-color: white;
        grid-template-rows: 1fr 4fr 1fr;
    }
    .postForm {
        display: grid;
        justify-items: center;
        align-items: center;
        height: 100vh;
    }
</style>