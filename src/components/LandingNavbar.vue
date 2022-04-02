<template>
    <div class="navbar">
        <div class="navbar-brand-col"><span class="brand">The Stocker.</span></div>
        <div class="links">
            <ul class="navbar_links">
                <li>
                    <span class="nav-button"><a class="aLink">About us</a></span>
                </li>
                <li>
                    <span class="nav-button"><router-link class="aLink" to="/signup">Sign up</router-link></span>
                </li>
                <li>
                    <span class="nav-button"><router-link class="aLink" to="/login">Log in</router-link></span>
                </li>
            </ul>
        </div>
    </div>
</template>

<style scoped>
    .aLink {
        text-decoration: none;
        cursor: pointer;
        color:white;
    }
    .brand {
        font-size: 5vh;
        color: white;
        font-family: 'Archivo Black', sans-serif;
    }
    .buttonDisplay {
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-content: center;
        height: 70%;
        width: 90%;
        border-style: solid;
        border-width: 2px;
        border-color: white;
        border-radius: 15px;
    }
    .navbar {
        background-color: #c62034;
        height: 9vh;
        display: flex;
        flex-direction: row;
        align-content: center;
        justify-content: center;
    }
    .navbar-brand-col {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: flex-start;
        width: 20%;
        margin-left: 2.5%;
    }
    .links {
        display: flex;
        flex-direction: row;
        justify-content: flex-end;
        align-items: center;
        width: 75%;
        height: 80%;
        margin-right: 10px;
        border-top-right-radius: 15px;
        border-bottom-right-radius: 15px;
    }
    .links:hover {
        color: white;
    }
    .navbar_links {
        list-style-type: none;
        display: flex;
        flex-direction: row;
        margin: 0;
    }
    .navbar_links li {
        display: inline-block;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        color: white;
        border-style: solid;
        border-left-style: none;
        border-width: 2px;
        transition: all 1s ease;
        height: 6vh;
        width: 10vw;
        transition: all 1s ease;
    }
    .navbar_links li:hover {
        background-color: white;
        transition: all 0.5s ease;
        color: white;
    }
    .navbar_links li a:hover {
        transition: all 0.5s ease;
        color: #c62034;
    }
    .link {
        height: 100%;
        width: 100%;
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        text-decoration: none;
        color: white;
        cursor: pointer;
    }
    .link a:hover {
        color: #c62034;
    }
    .navbar_links li:last-child {
        border-top-right-radius: 15px;
        border-bottom-right-radius: 15px;
    }
    .navbar_links li:first-child {
        border-top-left-radius: 15px;
        border-bottom-left-radius: 15px;
        border-left-style: solid;
    }
    .nav-button {
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-content: center;
    }
    .nav-button:hover {
        color: #c62034;
    }
</style>