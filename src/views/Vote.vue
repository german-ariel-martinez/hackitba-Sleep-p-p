<template>
    <div class="postGrid">
        <div class="gridTitle">
            Vote for the subject of the month!
        </div>
        <div class="gridBody">
            <div class="voteCard">
                <span style="justify-self: start; padding-left: 5%">Cryptos</span>
                <button style="justify-self: end; margin-right: 2%" class="voteButton">Vote!</button>
            </div>
            <div class="voteCard">
                <span style="justify-self: start; padding-left: 5%">Trading</span>
                <button style="justify-self: end; margin-right: 2%" class="voteButton">Vote!</button>
            </div>
            <div class="voteCard">
                <span style="justify-self: start; padding-left: 5%">NFTs</span>
                <button style="justify-self: end; margin-right: 2%" class="voteButton">Vote!</button>
            </div>
            <div class="voteCard">
                <span style="justify-self: start; padding-left: 5%">Airlines</span>
                <button style="justify-self: end; margin-right: 2%" class="voteButton">Vote!</button>
            </div>
            <div class="voteCard">
                <span style="justify-self: start; padding-left: 5%">Tourism</span>
                <button style="justify-self: end; margin-right: 2%" class="voteButton">Vote!</button>
            </div>
            <div class="voteCard">
                <span style="justify-self: start; padding-left: 5%">Ecology</span>
                <button style="justify-self: end; margin-right: 2%" class="voteButton">Vote!</button>
            </div>
        </div>
    </div>
</template>

<style scoped>
    .voteButton {
        border: none;
        background-color: #c62034;
        width: 15vw;
        height: 8vh;
        color: white;
        border-radius: 15px
    }
    .voteCard {
        display: grid;
        grid-template-columns: 1fr 1fr;
        justify-items: center;
        align-items:center;
        width: 75vw;
        height: 10vh;
        background-color: white;
        border-radius: 15px;
        border: black 2px solid;
    }
    .postGrid {
        display: grid;
        justify-items: center;
        grid-template-rows: 1fr 11fr;
        height: 100vh;
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