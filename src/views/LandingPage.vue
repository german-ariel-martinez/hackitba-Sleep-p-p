<template>
    <div>
        <!-- NAVBAR -->
        <landingNavbar/>
        <!-- BODY -->
        <div class="welcome-img">
            <div class="welcome-img-container">
                <span class="welcome-img-legend">Learn form the best. Be the best.</span>
            </div>
        </div>
        <divider title="How to get started"/>
        <!-- HOW TO GET STARTED CARDS -->
        <cardRight title="1. Create an account" 
                   text="It's simple, to create an account just go to the top right corner of your screen and click on the 'Sign up' button.  It will glow in white when you can click it." 
                   img="signupSS.png"/>
        <div class="htgs-img">
        </div>
        <cardLeft title="2. Complete the form" 
                   text="We would love to know more about you! Complete this form so your account registration is completed. We will ask you to verify your email, just log in into your email service provider and don't forget to check your spam box if the mail doesn't arrive, it might take a minute." 
                   img="signupSS.png"/>
        <!-- HOW DOES IT WORK -->
        <divider title="How does it work"/>
        <div class="card-body">
            <div class="card-text">
                Lorem ipsum dolor sit amet consectetur, adipisicing elit. Repellat voluptatum rerum labore, aut corporis numquam reprehenderit in dolore, eaque similique dolorem placeat voluptatem fugit culpa tenetur distinctio fuga est. Doloremque.
                Lorem ipsum dolor sit, amet consectetur adipisicing elit. Commodi excepturi mollitia nobis atque repellendus numquam facilis pariatur quos at quasi debitis, labore reiciendis, suscipit ex unde dignissimos similique vero ad.
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde facilis veritatis soluta! Ipsum, corporis unde eos quidem accusantium iure omnis ratione velit id quia blanditiis libero quaerat harum sapiente delectus!
            </div>
        </div>
        <!-- Footer -->
        <footer class="custom_footer">
            <div class="inner_footer">
                <div class="footer_col">
                    <div class="footer_title"> Made by </div> 
                    <div class="footer_text">
                        <div class="footer_text_style">German Ariel Martinez</div>
                        <div class="footer_text_style">Santiago Preusche</div>
                        <div class="footer_text_style">Agustin Roca</div>
                    </div>
                </div>
                <div class="footer_col">
                    <div class="footer_title"> Contact information </div> 
                    <div class="footer_text">
                        <div class="footer_text_style"><b-icon icon="telephone" style="color: white;margin-right:5px;"></b-icon>15-5555-555</div>
                        <div class="footer_text_style"><b-icon icon="envelope" style="color: white;margin-right:5px;"></b-icon>contact@thestocker.com</div>
                        <div class="footer_text_style"><b-icon icon="map" style="color: white;margin-right:5px;"></b-icon>40 W 37th St, New York, NY 10018, United States</div>
                    </div>
                </div>
            </div>
        </footer>
     </div>
</template>

<style scoped>
    .htgs-img {
        background-image: url("../assets/buildingsLP.jpeg");
        min-height: 400px; 
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        /* Set a specific height */
        min-height: 400px; 

        /* Create the parallax scrolling effect */
        background-attachment: fixed;
        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;

        display: flex;
        flex-direction: row;
        justify-content: center; 
        align-items: center;
    }
    .custom_footer {
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        color: white;
        background-color: #c62034;
        height: 30vh;
    }
    .inner_footer {
        border-top-style: solid;
        border-bottom-style: solid;
        border-top-width: 3px;
        border-bottom-width: 3px;
        border-top-color: white;
        border-bottom-color: white;
        height: 90%;
        width: 100%;
        display: flex;
        flex-direction: row;
        justify-content: space-around;
        align-items: center;
    }
    .footer_col {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .footer_title {
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        color: black;
        background-color: white;
        border-radius: 10px;
        margin: 5px;
        padding: 5px 10px;
    }
    .footer_text {
        display: flex;
        flex-direction: column;
        height: 100%;
        margin: 10px;
    }
    .footer_text_style {
        display: flex;
        flex-direction: row;
        align-items: center;
        margin: 5px;
    }
    .landing-footer {
        background-color: #202844;
    }

    .card-body {
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        height: 50vh;
    }
    .card-text {
        text-align: justify;
        width: 90%;
        border-bottom-style: solid;
        border-bottom-width: 2px;
        border-bottom-color: #c62034;
        padding-bottom: 5vh;
    }
    .welcome-img {
        background-image: url("../assets/stocksLPCut.png");
        min-height: 400px; 
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        /* Set a specific height */
        min-height: 400px; 

        /* Create the parallax scrolling effect */
        background-attachment: fixed;
        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;

        display: flex;
        flex-direction: row;
        justify-content: center; 
        align-items: center;
    }
    .welcome-img-container {
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        height: 10vh;
        width: 95%;
    }
    .welcome-img-legend {
        width: 30%;
        padding-bottom: 1.5vh;
        border-bottom-style: solid;
        border-bottom-color: #c62034;
        border-bottom-width: 3px;
        font-size: 3.5vh;
        color: white;
    }
</style>

<script>
// @ is an alias to /src
import landingNavbar from '@/components/LandingNavbar.vue'
import divider from '@/components/LandingDivider.vue'
import cardRight from '@/components/CardRight.vue'
import cardLeft from '@/components/CardLeft.vue'

export default {
  name: 'LandingPage',
  components: {
    landingNavbar,
    divider,
    cardRight,
    cardLeft
  }
}
</script>