<template>
    <div class="grid">
        <div>
            <div class="sideBar-links">
                <div class="sideBar-header">
                    <div class="sideBar-header-title">
                        <div class="sideBar-brand"><span class="brand">The Stocker.</span></div>
                    </div>
                    <div class="sideBar-header-pic">
                        <b-icon class="h1" style="margin-bottom:0; color: white" icon="person-circle"/>
                    </div>
                </div>
                <div class="sideBar-buttons">
                    <div class="sideBar-button">
                        <div class="button-icon">
                            <b-icon class="h4" style="margin-bottom:0; color: #c62034" icon="view-list"/>
                        </div>
                        <div class="button-text">Feed</div>
                    </div>
                    <div class="sideBar-button">
                        <div class="button-icon">
                            <b-icon class="h4" style="margin-bottom:0; color: #c62034" icon="chevron-double-up"/>
                        </div>
                        <div class="button-text">Trending</div>
                    </div>
                    <div class="sideBar-button">
                        <div class="button-icon">
                            <b-icon class="h4" style="margin-bottom:0; color: #c62034" icon="search"/>
                        </div>
                        <div class="button-text">Explore</div>
                    </div>
                    <div class="sideBar-button">
                        <div class="button-icon">
                            <b-icon class="h4" style="margin-bottom:0; color: #c62034" icon="graph-up"/>
                        </div>
                        <div class="button-text">Simulator</div>
                    </div>
                    <div class="sideBar-button">
                        <div class="button-icon">
                            <b-icon class="h4" style="margin-bottom:0; color: #c62034" icon="envelope"/>
                        </div>
                        <div class="button-text">Messages</div>
                    </div>
                </div>
                <div class="sideBar-footer">
                    <div class="logout">Log out</div>
                </div>
            </div>
        </div>
        <div class="postFeed"></div>
    </div>
</template>

<style scoped>
    .logout {
        border: white 2px solid;
        border-radius: 15px;
        height: 80%;
        width: 95%;
        display: grid;
        justify-items: center;
        align-items: center;
        color: white;
        transition: all 0.5s ease;
    }
    .logout:hover {
        border: #c62034 2px solid;
        background-color: white;
        color: #c62034;
        transition: all 0.5s ease;
    }
    .sideBar-footer {
        display: grid;
        justify-items: center;
        align-items: center;
    }
    .button-text {
        display: grid;
        justify-items: start;
        align-items: center;
        margin-left: 1vw;
    }
    .button-icon {
        display: grid;
        justify-items: center;
        align-items: center;
    }
    .sideBar-button {
        display: grid;
        grid-template-columns: 1fr 3fr;
        transition: all .5s ease;
    }
    .sideBar-button:hover {
        transition: all .5s ease;
        background-color: rgba(198, 32, 52, .2);
    }
    .sideBar-brand {
        display: grid;
        justify-items: start;
        align-content: center;
        height: 100%;
        margin-left: 1vw;
    }
    .brand {
        font-size: 3vh;
        color: white;
        font-family: 'Archivo Black', sans-serif;
    }
    .sideBar-buttons {
        display: grid;
        grid-template-rows: 1fr 1fr 1fr 1fr 1fr 5fr;
    }
    .sideBar-header-title {
        background-color: #c62034;
    }
    .sideBar-header-pic {
        background-color: #c62034;
        display: grid;
        justify-items: center;
        align-content: center;
        height: 100%;
    }
    .sideBar-header {
        background-color: #c62034;
        display: grid;
        grid-template-columns: 3fr 1fr;
    }
    .sideBar-footer {
        background-color: #c62034;
    }
    .grid {
        display: grid;
        grid-template-columns: 1fr 4fr;
        height: 100vh;
        overflow: hidden;
    }
    .sideBar-links {
        display: grid;
        grid-template-rows: 1fr 10fr 1fr;
        height: 100vh;
    }
    .postFeed {
        background-color: rgba(0, 0, 0, .1);
        overflow-y: scroll;
    }
</style>